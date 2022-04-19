import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_USER = os.environ.get('RABBITMQ_DEFAULT_USER');
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_DEFAULT_PASS');
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST');
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT');
REDIS_HOST = os.environ.get('REDIS_HOST');
REDIS_PORT = os.environ.get('REDIS_PORT');
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD');
RABBITMQ_PROTOCOOL = os.environ.get('RABBITMQ_PROTOCOOL')
S3_ENDPOINT = os.environ.get('S3_ENDPOINT')
S3_UPLOAD_KEY = os.environ.get('S3_UPLOAD_KEY')
S3_UPLOAD_SECRET = os.environ.get('S3_UPLOAD_SECRET')
S3_UPLOAD_BUCKET = os.environ.get('S3_UPLOAD_BUCKET')

AMPQ_URL = f'{RABBITMQ_PROTOCOOL}://{RABBITMQ_USER}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}'
REDIS_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}'
UPLOAD_PATH = '/uploads'
FILE_DURATION = int(os.environ.get('FILE_DURATION'))
