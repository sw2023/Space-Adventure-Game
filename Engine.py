# imports that don't consist of code that is used in the actual story
from ClearConsole import clear
from time import sleep
import Inventory

def sleeper(): # didn't want to write `sleep(2)`
    sleep(2)

quitGame = [ord(char) - 96 for char in input('Do you want to continue as the probe? (y/n)').lower()] # converts character input into numbers
# credit for the above (minor modifications were made): https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python
# 14 is "n" and 25 is "y"
# numbers in corresponding alphabetical order, starting with a = 1 and ending with z = 26

# while statement detects invalid inputs
while quitGame[0] != 14 or quitGame[0] != 25:
    if quitGame[0] == 14 or quitGame[0] == 25:
        break
    
    del quitGame[:] # resets quitGame array to avoid complications, as the above if statement only checks the first value of quitGame

    quitGame = [ord(char) - 96 for char in input('Do you want to continue as the probe? (y/n)').lower()]

# if the user responds with "n", the program stops
if quitGame[0] == 14:
    print("The probe's self-destruct sequence automatically starts.")
    sleep(7)
    
    Inventory.probeHealth = 0

# if user responds w/ "y", program continues
elif quitGame[0] == 25:
    pass