import hashlib


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
            Raise(f"{hash_function} is an invalid hash function")

    return readable_hash
