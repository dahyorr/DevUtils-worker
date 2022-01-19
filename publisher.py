import pika, os, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)
username = 'dahyor'
password = 'IsThIsREaLLySecuRE???'
hostname = 'localhost'
port = '5672'

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=hostname,
        port=port,
        credentials=credentials
    )
)

channel = connection.channel() # start a channel
# channel.queue_declare(queue='hashing-queue') # Declare a queue
channel.exchange_declare('hashing-exchange', durable=True)
# send a message

channel.basic_publish(exchange='hashing-exchange', routing_key='hashing-queue', body='{"pattern":"uuid", "data", "we8hshy7fgisuetgebrfegsryyh"')
print ("[x] Message sent to consumer")
connection.close()