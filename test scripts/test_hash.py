#!/usr/bin/python

import time
import sys
sys.path.append("..")

from image_hash import *

results1="325231352"
results2="443123551"

print("1st results input:", results1)
print("hash():", generateHash(results1))
print("hash2():", generateHash2(results1))
print()
print("2nd results input:", results2)
print("hash():", generateHash(results2))
print("1st hash2():", generateHash2(results2))
time.sleep(0.1)
print("2nd hash2():", generateHash2(results2), "(after 100ms delay)")
