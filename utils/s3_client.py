import boto3
from botocore.errorfactory import ClientError
from settings import S3_ENDPOINT, S3_UPLOAD_SECRET, S3_UPLOAD_KEY, S3_UPLOAD_BUCKET


client = boto3.client(
    's3',
    aws_access_key_id=S3_UPLOAD_KEY,
    aws_secret_access_key=S3_UPLOAD_SECRET,
    endpoint_url=S3_ENDPOINT,
)

# def download_file(file_id):
#     return client.download_file(Bucket=bucket, Key=key)['Body'].read()

def stream_file(file_id):
    return client.get_object(Bucket=S3_UPLOAD_BUCKET, Key=file_id)['Body'].read()


def validate_file(file_id):
    try:
        client.head_object(S3_UPLOAD_BUCKET, file_id)
        return True
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            return False
        else:
            # Something else has gone wrong.
            raise("s3-client: Unknown error")
    else:
        return False