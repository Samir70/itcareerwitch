'''datetime'''
import os
from datetime import date
# from datetime import time
from datetime import datetime

today = date.today()
date_time = datetime.now()

print("Today's date is: ", today)
print("Can you be more specific please? ", date_time)
print("Break it down....")
print("The hour ", date_time.hour)
print("The minute ", date_time.minute)
print("The seconds ", date_time.second)

#Working directory
print("\n")

dirpath = os.getcwd()
print("Your current working directory is: " + dirpath)

foldername = os.path.basename(dirpath)
print("The specific folder is: " + foldername)

print("=========================")
print(os.stat("m25_datetime.py"))
