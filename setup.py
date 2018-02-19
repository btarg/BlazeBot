# BlazeBot first-time setup (Python 3)

ver = "1.5"
import os

print("========================================")
print("BlazeBot version " + ver + " first-time setup")
print("https://icrazyblaze.github.io/BlazeBot")
print("========================================")
print("")
print("Welcome to the BlazeBot setup program! Make sure you have read the README carefully, so you know what you're doing. Remember, you will have to manually edit the 'config.py' file to change the bot's prefix and desciption.")
print("")
print("**WARNING:** This setup will NOT install Speech Recognition - to do that, run the correct dependencies installer, found in the 'misc' folder, or manually install it with pip.")
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
    print("Successfully wrote to config!")
except:
    print("ERROR: Couldn't write to 'config.py'! Does it exist?")

file.close()

# Part 2: Install requirements from text file using pip/pip3
print("")
print("== PIP START== ")
print("")

try:
    try:
        os.system("pip install -r requirements.txt")
    except:
        os.system("pip3 install -r requirements.txt")
except:
    print("ERROR: Could not install dependencies!")

print("")
print("== Setup has finished! ==")
print("You can now close this window and launch BlazeBot.")
print("")
