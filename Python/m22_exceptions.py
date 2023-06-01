'''handling exceptions'''

try:
    [a, b] = [int(x) for x in input("Give me two space seprated numbers to divide: ").split(" ")]
    print(F"The quotient of {a} and {b} is {a/b}")
except ZeroDivisionError:
    print("I don't know how to divide by zero")
except ValueError:
    print("Either you didn't give me two space seperated numbers, or one of them was letters not digits")
