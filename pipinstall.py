import os
import subprocess
import urllib.request

# Download get-pip.py
url = 'https://bootstrap.pypa.io/get-pip.py'
filename = 'get-pip.py'

print("Downloading get-pip.py...")
urllib.request.urlretrieve(url, filename)

# Run the get-pip.py script
print("Installing pip...")
subprocess.run([os.sys.executable, filename])

# Clean up the get-pip.py file after installation
os.remove(filename)
print("Pip installation complete and cleaned up!")
