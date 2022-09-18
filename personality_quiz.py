from random import sample

with open("quiz_questions.txt", "r") as questionsfile:
    questions = questionsfile.readlines()

def assignbit(intval, index):
    return intval | (1 << index)
answerhex = 0x0000

qstack = sample(range(64), k=16)
print("Please answer 'yes' or 'no' to the following questions to initialize your digital pet :)")

for i in range(16):
    answerhex = assignbit(answerhex, i) if input(questions[qstack[i]]).lower() in ['yes', 'y', 'sure', 'yep'] else answerhex

print("Answer as hex: % s" % hex(answerhex))
