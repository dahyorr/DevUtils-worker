import os
import sys
import pathlib
import pika
from checksum_generator.generate import get_checksum

BASE_PATH = pathlib.Path().resolve()


def main():
    filename = sys.argv[1]
    filepath = os.path.join(BASE_PATH, filename)

    if(not os.path.isfile(filepath)):
        raise FileNotFoundError(f'invalid file path "{filepath}"')

    checksum = get_checksum(filepath, 'sha256')
    print(checksum)


if(__name__ == "__main__"):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    main()
    connection.close()