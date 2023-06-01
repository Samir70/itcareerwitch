'''cmd line args'''
import sys

print(F"The name of this module is: {sys.argv[0]}")

if len(sys.argv) > 1:
    NUM = int(sys.argv[1]) or 0
    print(F"The square of {NUM} is {NUM * NUM}")
else:
    print("You didn't give me a number to square")
