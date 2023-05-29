'''test'''
colours = ['red', 'orange', 'black', 'green']
colours[2] = 'yellow'
print(colours)

colours += ['blue']
extras = ['indigo', 'violet']
colours += extras
print(colours)

colours.insert(3, 'grey')

print(colours)
del colours[3]
print(colours)
colours.remove('blue')
print(colours)

for c in colours:
    print(F"{c} is in colours")
