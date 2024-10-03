import requests
import time

pip = input("You must have pip installed to use this program! Do you have pip installed? y/n ")

if pip == "n":
    exit()

elif pip == "y":
    print()

else:
    exit()

log = "https://raw.githubusercontent.com/appmaker999/Loggy/refs/heads/main/log.csv"
crashlog = "https://raw.githubusercontent.com/appmaker999/Loggy/refs/heads/main/crashlog.csv"
readme = "https://raw.githubusercontent.com/appmaker999/Loggy/refs/heads/main/README.md"
loggy = "https://raw.githubusercontent.com/appmaker999/Loggy/refs/heads/main/Loggy.py"

#Download log
response = requests.get(log)
with open("log.csv", "wb") as file:
    file.write(response.content)

print("Downloading log.csv...")
time.sleep(5)
print()

#Download crashlog
response = requests.get(crashlog)
with open("crashlog.csv", "wb") as file:
    file.write(response.content)

print("Downloading crashlog.csv...")
time.sleep(5)
print()

#Downloading readme
response = requests.get(readme)
with open("readme.md", "wb") as file:
    file.write(response.content)

print("Downloading readme.md...")
time.sleep(1)
print()

#Download loggy
response = requests.get(loggy)
with open("loggy.py", "wb") as file:
    file.write(response.content)

print("Downloading loggy.py...")
time.sleep(10)
print()

#Success!
print("Cleaning up...")
time.sleep(8)
print("Program closing in 5")
time.sleep(1)
print(4)
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("Program closing...")
time.sleep(1)