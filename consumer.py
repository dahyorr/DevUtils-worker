"""Consumer for File hash generator"""
import os
import sys
import time
import json
import pika
from utils.checksum_generator import generate_checksum
from utils.file_validator import validate_file

UPLOAD_PATH = '/uploads'

# declaring credentials
def connect():
    """Returns connection to rabbitmq server"""
    user_name = os.environ.get('RABBITMQ_DEFAULT_USER')
    password = os.environ.get('RABBITMQ_DEFAULT_PASS')
    host_name = os.environ.get('RABBITMQ_HOST')
    port = os.environ.get('RABBITMQ_PORT')
    credentials = pika.PlainCredentials(user_name, password)
    return pika.BlockingConnection(
        pika.ConnectionParameters(
            host=host_name,
            port=port,
            credentials=credentials
        )
    )

connection = None
connection_retrys = 0

while connection_retrys < 5:
    try:
        if connection_retrys > 0:
            print('Waiting 5 seconds before retry...')
            time.sleep(5)
        connection = connect()
        break
    except pika.exceptions.AMQPConnectionError as err:
        print('Connection Error')
        print(err)
        connection_retrys += 1
        continue
    except Exception as err:
        print('Unexpected Error')
        print(err)
        connection_retrys += 1
        continue
else:
    print('Failed to connect')
    print('Exiting...')
    sys.exit(1)

print('Connected...')

channel = connection.channel()

# split message into multiple queues for future modification
channel.queue_declare('hashing-queue', durable=True)
channel.exchange_declare('hashing-exchange', durable=True)

channel.queue_bind(exchange='hashing-exchange', queue='hashing-queue')

def hash_file(ch, method, properties, body):
    """Callback for hashing_queue"""
    try:
        content = json.loads(body.decode())
        hash_type = content['pattern']
        file_name = content['data']
        print(f'Received request to hash {file_name} as {hash_type}')
        file_path = validate_file(UPLOAD_PATH, file_name)

        if not file_path:
            raise FileNotFoundError('The requested file was not found')

        hash = generate_checksum(file_path, hash_type)
        print(hash) # TODO: do something with hash and store
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as err:
        print('***Failed to complete task')
        print(err)



channel.basic_consume('hashing-queue', hash_file)

print('Waiting for messages...')

channel.start_consuming()
