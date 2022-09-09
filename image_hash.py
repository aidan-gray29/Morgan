import hashlib

# Generate hash from input
def generateHash(dataToHash):
    dataEncoded = str(dataToHash).encode("utf-8")
    md5Hash = hashlib.md5(dataEncoded)
    return md5Hash.hexdigest()

