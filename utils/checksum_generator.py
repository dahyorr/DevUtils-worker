import hashlib
from utils.s3_client import stream_file

def generate_checksum(filepath, hash_function):
    """Generate checksum for file baed on hash function (MD5 or SHA256)"""
    hash_function = hash_function.lower()
    with open(filepath, "rb") as f:
        bytes = f.read()  # read file as binary
        if hash_function == 'md5':
            readable_hash = hashlib.md5(bytes).hexdigest()
        elif hash_function == "sha256":
            readable_hash = hashlib.sha256(bytes).hexdigest()
        else:
            raise(f"{hash_function} is an invalid hash function")

    return readable_hash

def generate_checksum_bucket(file_id, hash_function):
    """Generate checksum for file baed on hash function (MD5 or SHA256)"""
    hash_function = hash_function.lower()
    bytes = stream_file(file_id)
    if not(bytes):
        raise('Invalid File ID')
    if hash_function == 'md5':
        readable_hash = hashlib.md5(bytes).hexdigest()
    elif hash_function == "sha256":
        readable_hash = hashlib.sha256(bytes).hexdigest()
    else:
        raise(f"{hash_function} is an invalid hash function")

    return readable_hash
