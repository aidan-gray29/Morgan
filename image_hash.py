import hashlib
from datetime import datetime

# Generate md5 hash from input
def generateHash(dataToHash):
    dataEncoded = str(dataToHash).encode("utf-8")
    md5Hash = hashlib.md5(dataEncoded)
    return md5Hash.hexdigest()


# Custom hash algorithm using the current time as a salt
def generateHash2(dataToHash):
    mask = 0xFFFFFFFF
    A = int(dataToHash)
    B = int(datetime.now().timestamp() * 1000)
    C = (A ^ B) & mask
    D = C << 16
    E = C ^ D
    F = hex(E & mask)
    return F[2:]

