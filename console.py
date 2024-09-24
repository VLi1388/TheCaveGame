import sys
import time

# prints out text letter by letter
def delayPrint(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

# prints out text word by word on the same row
def delayPrintWord(text):
    for word in text.split(' '):  # using '-' so that the spaces will be kept
        sys.stdout.write(word + " ")
        sys.stdout.flush()
        time.sleep(0.3)

# prints out text word by word each on a new row
def delayPrintRow(text):
    for word in text.split(' '):
        print(word)
        time.sleep(0.4)

# prints out separations
def printSeparation():
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")

# prints out sub separations within a body
def printSubSep():
    print("-----------------------------------------------------------")