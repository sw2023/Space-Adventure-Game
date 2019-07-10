from clearConsole import clear
from intro import sleeper
from time import sleep
import Inventory
import RandomEvent

def part_1_event_1():
    clear()
    sleeper()
    print("After millenia of slow travel in hibernation, the probe awakens from its sleep.")
    sleeper()
    print("Hoping against hope, it trains its receiver on the direction of Earth's sun, but")
    sleeper()
    print("it is as silent as any of the myriad of dead stars surrounding it.")
    sleep(5)
    clear()
    print("Suddenly, something pops up on one of the multitudes of sensors the probe boasts. The probe scans")
    print("the energy signatures the strange object is emitting and cannot match them with one in its databases.")
    sleeper()
    print("The object is unlike any that had been encountered by Earth scientists.")
    sleeper()
    print("")
    print("Suddenly, the object turns towards the probe, emitting large amounts of energy.")
    sleep(3.25)
    print("The strange object seems to be trying to send a message to the probe, but the probe can't decode the message.")
    sleep(3.25)
    print("The probe focuses its visual sensors on the odd object. The object seems to be made of some sort of")
    print("shiny metal. It's roughly spherical in shape and 10 meters in diameter, with some odd portruding metal")
    print("spikes that seem to be sensing devices. The probe its observations to its database.")
    sleep(5)
    print("Suddenly, a strange light starts emanating from the odd object. The probe prepares for the worst and readies")
    print("its limited arsenal of weaponry. But there is no need for that. The strange object instead suddenly warps away, ")
    print("leaving the probe behind. The probe notes that the strange object is capable of faster-than-light travel.")
    sleep(12)
    clear()

def part_1_event_2():
    sleeper()
    print("The probe encounters another similar object exhibiting similar behaviours, except this time, the object seemed")
    print("to scan the probe before warping away.")
    sleeper()
    print("Confused, the probe decides to head on its way.")
    sleep(6)
    clear()
    print("Sensors on the probe indicate that there's something that can be scanned nearby. If the probe decides to scan the nearby ")
    print("object or phenomenon, it could potentially gain some materials.")
    sleep(7)
    print("At the very least, it could gain some knowledge.")
    sleep(4)
    RandomEvent.scan_object(0)
    sleep(5)
    clear()

    print("The probe comes across a completely empty part of space, devoid of everything except the probe.")
    sleep(3)
    print("The probe accelerates and clears the empty space.")
    
    # this bit of code is to give the user a sense that they're actually doing something instead of reading text on a screen
    # if they wanted to read text on a screen, they could just read a(n) (e)book
    continueStory = [ord(char) - 96 for char in input('Continue? (y/n)').lower()]

    while continueStory[0] != 14 or continueStory[0] != 25:
        if continueStory[0] == 14 or continueStory[0] == 25:
            break
        
        del continueStory[:] # resets continueStory array to avoid complications, as the above if statement only checks the first value of continueStory

        continueStory = [ord(char) - 96 for char in input('Please enter a valid input. Continue? (y/n)').lower()]

    # if the user responds with "n", the program stops
    if continueStory[0] == 14:
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
    elif continueStory[0] == 25:
        pass
    
    print("The probe approaches a crossroads.")
    sleep(2)
    print("There are three possible paths for the probe to take, but all of them are unknown.")
    sleep(4)
    print("The probe could also turn back and head another direction?")
    pathSelect = input("Which path do you want to take?")