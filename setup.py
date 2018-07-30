# BlazeBot first-time setup (Python 3)
# Updated 30/07/2018

# BlazeBot version
ver = "1.6"
import os
import platform

f = open('logo.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()
print("Now with more code!!")
print("")
print("========================================")
print("BlazeBot version " + ver + " setup application")
print("https://icrazyblaze.github.io/BlazeBot")
print("========================================")
print("")
print("Welcome to the BlazeBot setup program! Make sure you have read the README carefully, so you know what you're doing. Remember, you will have to manually edit the 'config.py' file to change the bot's prefix and desciption.")
print("")

# Read config file and add to a variable
file = open('config.py', 'r')
config_lines = file.readlines()
file.close()

# Get input from user
print("Please enter your bot token (required):")
tokenset = input("> ")
print("")
print("Please enter your YouTube API Key (optional):")
keyset = input("> ")

# Part 1: Write lines lines 2, 3, 4 and 5 to file
try:
    config_lines[3] = 'bbtoken = "' + tokenset + '" #REMOVE TOKEN BEFORE SYNC!! -Blaze' + '\n'
    config_lines[4] = '\n'
    config_lines[5] = '# YouTube API key (https://console.developers.google.com/apis/credentials/key)' + '\n'
    config_lines[6] = 'key = "' + keyset + '" #REMOVE KEY BEFORE SYNC!! -Blaze' + '\n'

    with open('config.py', 'w') as file:
        file.writelines(config_lines)
    print("")
    print("Successfully wrote to the config file!")
except:
    print("ERROR: Couldn't write to 'config.py'! Does it exist?")

file.close()

# Part 2: Install requirements from text file using pip (updated for Windows and Python 3.7)
print("")
print("== PIP START == ")
print("")

try:
    if not os.name == 'nt': # If the script is not running on Windows
        try:
            print("Using pip method...")
            os.system("pip install -r requirements.txt")
        except:
            print("Using pip3 method...")
            os.system("pip3 install -r requirements.txt")
    else: # If the script is running on Windows
        try:
            print("Using Python 3.7 method...")
            os.system("py -m pip install -r requirements.txt") # Python 3.7 command - if this fails (user does not have 3.7), use the old command
        except:
            try:
                print("Using legacy Python method...")
                os.system("python -m pip install -r requirements.txt")
            except:
                print("ERROR: Could not install dependencies!")
                print("Please check that your Python version is compatible:")
                print("Python " + platform.python_version())
except:
    print("ERROR: Could not install dependencies!")
    print("Please check that your Python version is compatible:")
    print("Python " + platform.python_version())

print("")
print("== PIP END ==")
print("")

print("")
print("== Setup has finished! ==")
print("You can now close this window and launch BlazeBot.")
print("")
print("")
