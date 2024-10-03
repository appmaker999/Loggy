#This is the loggy app! 

#Beta version 1.0

#import dependencies
from datetime import datetime
import csv
from pathlib import Path
import sys

#Get time and format to H M S
time = datetime.now().time()
time = time.strftime("%H:%M:%S")

#Get date and format
date = datetime.now()
date =date.strftime("%d/%m/%y")

#Get game
game = input("What game are you playing? ")

#Get start or stop
s = input("Are you starting or ending your time? s/e ")

if s == "s":
    s2 = "Start"

elif s == "e":
    s2 = "End"

else:
    sys.exit("Invalid input. Please use s for starting and e for end!")

#Make data variable for ease of use
data = [date, "", time, "", game, "", s2]

#Check if file exists
path = Path("log.csv")

#Write to csv if exists, cancel if not!
if path.exists():
    with open('log.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
    
        # Write a single row
        writer.writerow(data)
    
    print("Logged succesfuly!")

else:
    print("log.csv does not exist! Please delete all files for loggy and run the installer!!")