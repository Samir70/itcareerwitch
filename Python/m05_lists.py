'''test'''
colours = ['red', 'orange', 'black', 'green']
colours[2] = 'yellow'
# print(colours)
# ['red', 'orange', 'yellow', 'green']

colours += ['blue']
extras = ['indigo', 'violet']
colours += extras
# print(colours)
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

colours.insert(3, 'grey')

# print(colours)
# ['red', 'orange', 'yellow', 'grey', 'green', 'blue', 'indigo', 'violet']
del colours[3]
# print(colours)
# ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colours.remove('blue')
# print(colours)
# ['red', 'orange', 'yellow', 'green', 'indigo', 'violet']

# for c in colours:
#     print(F"{c} is in colours")

colours.sort()
# print(colours)
# ['green', 'indigo', 'orange', 'red', 'violet', 'yellow']
colours.sort(reverse=True)
# print(colours)
# ['yellow', 'violet', 'red', 'orange', 'indigo', 'green']
print(colours)

nums = [11, 2, 3, 4]
# print(nums.reverse(), nums)
# None [4, 3, 2, 11]

# But try
# print(sorted(nums), nums)
# [2, 3, 4, 11] [11, 2, 3, 4]

# ##################################
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(nums[2:5])
print(nums[0::2])
