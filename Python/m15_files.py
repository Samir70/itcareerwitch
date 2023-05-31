'''files'''
# demo_file = open("m13_loops.py", "r", encoding="utf-8")
# print(demo_file.read())
# print(demo_file.readline())
# demo_file.close()

with open("m13_loops.py", encoding="utf-8") as myfile:
    contents = myfile.read()
print(contents)

file2 = open("rubbish.txt", "a", encoding="utf-8")
file2.write("Count the lines to see how many times the file has been run\n")
file2.close()
