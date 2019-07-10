from time import sleep
from clearConsole import clear

def sleeper(): # got lazy writing "sleep(1.25)", serves no other purpose
    sleep(1.8)

def display_intro():
    clear()
    sleeper()
    print("And when they knew the Earth was doomed, they built a ship.")
    sleeper()
    print("In its heart, a thousand colonists frozen in sleep, chosen and trained to start civilization again on a new world.")
    sleeper()
    print("")
    print("They also built something else. A small probe, containing all of recorded human history, all of its achievements, and all of its culture.")
    sleeper()
    print("To control the probe they created an artificial intelligence. Not human, but made to think and feel like one, ")
    print("to pilot itself through the endless void, gather resources from asteroids and planetoids, and maybe, just maybe")
    print("make its way to the last remamants of humanity on the ship and help it build a new civilization.")
    sleep(7)
    print("")
    sleeper()
    print("The probe's solar sails propel it faster and faster into the void, and the AI ")
    print("listens as the transmissions from ground control slowly fade then cease.")
    sleeper()
    print("When all is quiet, the AI enters hibernation to wait out the first part of its long journey.")
