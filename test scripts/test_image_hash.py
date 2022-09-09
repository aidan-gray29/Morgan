#!/usr/bin/python

import sys
sys.path.append("..")

from image_hash import *

# This is all driver test code for the hash function
# None of this will be needed in the final project

# Use a selected number of questions/answers to generate the desired hash input
questions = int(input("Number of questions: "))
answers = int(input("Number of answers: "))
quizResults = 0

# Print basic questions and accept basic input in numbers
# The actual quiz will be formatted more nicely, this is just to test input formatting for the hash
for q in range(1, questions+1):
    print("Question " + str(q) + ":")
    print("Answers:")

    for a in range(1, answers+1):
        print("  ", a)

    choice = int(input(""))

    # Shift the result int 3 bits left to make room for the new answer.
    # Can be shifted by the number of answers if we want each bit to be unique.
    # ie, choice 1 is 00001, choice 2 is 00010, etc
    quizResults <<= 3

    # Bitwise-OR the choice into the results.
    # This isn't different from adding the choice if the above shifting is large enough.
    quizResults |= choice

print()
print("Quiz results:")
print("Binary:", bin(quizResults))
print("Decimal:", quizResults)
print("Hexadecimal:", hex(quizResults))

imageHash = generateHash(quizResults)
print()
print("Hash result:")
print(imageHash)
