'''inputs'''

answer = input("What is the answer?")
OUT_STRING = "{} is the wrong answer!"
try:
    num = int(answer)
    print(OUT_STRING.format(num))
except ValueError:
    print("I can't convert that to a number!!!!!!!!!")


MY_STRING = "The real answer is {answer}, every {} should know that!"
print(MY_STRING.format("fool", answer="42"))
