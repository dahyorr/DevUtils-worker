import os
import sys
import pathlib
from checksum_generator import generate_checksum

BASE_PATH = pathlib.Path().resolve()


def main():
    filename = sys.argv[1]
    filepath = os.path.join(BASE_PATH, filename)

    if(not os.path.isfile(filepath)):
        raise FileNotFoundError(f'invalid file path "{filepath}"')

    checksum = get_checksum(filepath, 'sha256')
    print(checksum)


if(__name__ == "__main__"):
    main()
