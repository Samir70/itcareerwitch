'''conditionals'''
X = 56
res = print("X is 5") if X == 5 else print("X is not 5")
print(res)


temps = [10, 4, 7, 8, 9, 13]

def describe(temp):
    '''Silly function'''
    if temp < 5:
        print(F"It's {temp}, that's cold")
    elif temp <= 10:
        print(F"It's {temp}, that's warm")
    else:
        print(F"It's {temp}! Anything 11 or more is definitely too hot!!!!")

for t in temps:
    describe(t)
