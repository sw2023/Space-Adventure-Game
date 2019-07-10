# imports that don't consist of code that is used in the actual story
from clearConsole import clear
from time import sleep
import Inventory

# imports that contain the story
from intro import display_intro, sleeper
from StoryOne import part_1_event_1, part_1_event_2

display_intro() # pretty self-explanatory, just displays the intro found in intro.py

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
    print("The probe decides it has no purpose and fries all its electronics, leaving a dead husk to drift through ")
    print("the endless void. Perhaps another spacecraft will stumble upon its wreckage sometime in the future.")
    sleep(4)
    print("In addition to this, the probe's self-destruct sequence automatically starts.")
    sleep(5)
    print("The probe begins self-destruction.")
    sleep(2.5)

    for i in range(0, 3):
        print("Danger! Probe health low!")
        sleep(3)

    Inventory.probeHealth = 0

# if user responds w/ "y", program continues
elif quitGame[0] == 25:
    pass

# continuing the story
part_1_event_1()