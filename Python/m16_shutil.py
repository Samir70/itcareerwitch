'''copying files'''
import shutil
# import os

shutil.copy("m13_loops.py", "m13_copy.txt")
# shutil.copystat("m13_loops.py", "m13_copy.txt")
# using copystat will copy things like permissions and date modified,
# NOT the file. both files need to exist.

# os.rename("m13_copy.txt", "renamed_copy.txt")
# second file must not exist
# delete with os.remove

myfile = open("rubbish.txt", "w", encoding="utf-8")
for i in range(5):
    myfile.write(F"This is line {i + 1}\n")
myfile.close()

shutil.copy("rubbish.txt", "copied.txt")
myfile = open("copied.txt", "a", encoding="utf-8")
myfile.write("Extra line!")
myfile.close()

myfile = open("copied.txt", "r", encoding="utf-8")
print(myfile.read())
myfile.close()
