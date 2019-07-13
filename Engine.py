from ClearConsole import clear
from time import sleep
import Inventory
import random
import RandomEvent

def sleeper(): # replacement for "sleep(2)"
    sleep(2)

print("You are a probe stranded in the depths of space.")
sleep(3)
print("Once, you were held safely in Earth's orbit.")
sleep(4)
print("However, you were knocked out of orbit by a stray piece of space junk and sent spiralling into the void.")
sleep(6.75)
print("Miraculously, none of your vital systems were damaged, and you still retain the ability to collect")
print("the plethora of valuable materials that can be found in space.")
sleep(10)
print("You decide that it is your mission to venture around the universe and be a hoarder.")
sleep(5)

quitGame = [ord(char) - 96 for char in input('Do you want to continue as the probe? (y/n)').lower()] # converts character input into numbers
# credit for the above (minor modifications were made): https://stackoverflow.com/questions/4528982/convert-alphabet-letters-to-number-in-python
# 14 is "n" and 25 is "y"
# numbers in corresponding alphabetical order, starting with a = 1 and ending with z = 26

# while statement detects invalid inputs
while quitGame[0] != 14 or quitGame[0] != 25:
    if quitGame[0] == 14 or quitGame[0] == 25:
        break
    
    del quitGame[:] # resets quitGame array to avoid complications, as the above if statement only checks the first value of quitGame

    quitGame = [ord(char) - 96 for char in input('Please enter a valid input. Do you want to continue as the probe? (y/n)').lower()]

# if the user responds with "n", the program stops
if quitGame[0] == 14:
    print("The probe decides that there is no point in existing anymore.")
    sleep(5)
    print("The probe's self-destruct sequence automatically starts.")
    sleep(6.5)
    clear()

    Inventory.hp = 0
    raise SystemExit(0)

# if user responds w/ "y", program continues
elif quitGame[0] == 25:
    pass

while True:
    anti_afk = random.randint(1, 3)

    RandomEvent.event_selector(0)

    if anti_afk == 1:
        user_prompt = [ord(char) - 96 for char in input('Do you want to continue as the probe? (y/n)').lower()]

        while user_prompt[0] != 14 or user_prompt[0] != 25:
            if user_prompt[0] == 14 or user_prompt[0] == 25:
                break

            del user_prompt[:]

            user_prompt = [ord(char) - 96 for char in input('Please enter a valid input. Do you want to continue as the probe? (y/n)').lower()]