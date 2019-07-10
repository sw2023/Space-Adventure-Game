from ClearConsole import clear
from time import sleep

iron = 0 # iron is a common material that can be used to add to or reinforce the probe
nickel = 0 # nickel is a common material used to reinforce the probe
gold = 0 # gold is a semi-common material that can be used to upgrade sections of the probe and trade to other ships
copper = 0 # copper is a common material used to upgrade the ship and sometimes trade to other ships
platinum = 0 # platinum is an uncommon material used to upgrade the ship and trade
avorion = 0 # avorion is an extremely rare metal used to upgrade, reinforce, and add to the ship. Also tradable.

probeHealth = 250 # probe's health that can be added to or subtracted, if health reaches 0, game ends
# max hp is 1000 and requires extremely good rng to get it
hullShield = 0 # max shield is 7
healthRegen = 10 # hp slowly regens over time

if probeHealth == 0:
    print("The probe has sustained too much damage and can't sustain itself any longer.")
    sleep(10)
    clear()

    raise SystemExit(0)

# dictionaries used to represent inventory slots
slot1 = {
    "Type": "null", 
    "Tier": 0, 
    "Durability": 0
}
slot2 = {
    "Type": "null", 
    "Tier": 0, 
    "Durability": 0
}
slot3 = {
    "Type": "null", 
    "Tier": 0, 
    "Durability": 0
}
slot4 = {
    "Type": "null", 
    "Tier": 0, 
    "Durability": 0
}
slot5 = {
    "Type": "null", 
    "Tier": 0, 
    "Durability": 0
}