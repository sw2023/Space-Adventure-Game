import random
import Inventory
from Intro import sleeper
from ClearConsole import clear
from time import sleep

temp = 0 # temp variable

def event_selector(selectEvent):
    # randomly selects event
    # function may not be used in final game
    
    eventHappens = random.randint(1, 3)

    if (eventHappens == 1 and selectEvent == 0) or (selectEvent == 1):
        materials_found()
    elif (eventHappens == 2 and selectEvent == 0) or (selectEvent == 2):
        scan_object(0)
    elif (eventHappens == 3 and selectEvent == 0) or (selectEvent == 3):
        object_found()

def materials_found():
    # function, when called, gives user a random amount of a random material
    # the 4 materials are found in Inventory.py

    materialType = random.randint(1, 55)
    materialAmount = random.randint(10, 30)
    matsGainedUnobtanium = random.randint(1, 5) # unobtanium is rare and comes in sparse quantities, so a seperate RNG variable is required
    
    if materialType >= 1 and materialType <= 12:
        temp = Inventory.iron
        Inventory.iron += materialAmount
        print("You just got ", (Inventory.iron - temp), " iron!")
    elif materialType >= 25 and materialType <= 33:
        temp = Inventory.gold
        Inventory.gold += materialAmount
        print("You just got ", (Inventory.gold - temp), " gold!")
    elif materialType >= 13 and materialType <= 24:
        temp = Inventory.copper
        Inventory.copper += materialAmount
        print("You just got ", (Inventory.copper - temp), " copper!")
    elif materialType >= 34 and materialType <= 42:
        temp = Inventory.platinum
        Inventory.platinum += materialAmount
        print("You just got ", (Inventory.platinum - temp), " platinum!")
    elif materialType >= 43 and materialType <= 45:
        temp = Inventory.unobtanium
        Inventory.unobtanium += matsGainedUnobtanium
        print("You just got ", (Inventory.unobtanium - temp), " unobtanium!")
    elif materialType >= 46 and materialType <= 55:
        temp = Inventory.nickel
        Inventory.nickel += materialAmount
        print("You just got ", (Inventory.nickel - temp), " nickel!")

def scan_object(scanObject):
    # random object passing by, gives user the choice to scan or not
    # very small chance of craft being damaged during scan

    # variable scanObject is used to give the developer control over what kind of object is scanned
    # created for debugging purposes

    typeOfObject = random.randint(1, 3) # decides what the object being scanned is
    craftDamaged = random.randint(1, 50) # decides if the probe gets damaged or not

    asteroidSize = random.randint(1, 2) # decides whether resources can be pulled from asteroid
    asteroidType = random.randint(1, 110) # types of asteroids in order from most common to rarest: iron, nickel, copper, gold, platinum, unobtanium
    matsGained = random.randint(10, 30) # amount of materials gained
    unobtaniumGained = random.randint(1, 5) # amount of unobtanium gained

    # same code used in engine.py, only modifications are the parameters of input() and addition of nested while loops
    scanOrNot = [ord(char) - 96 for char in input('Do you want to scan? (y/n)').lower()]

    while scanOrNot[0] != 14 or scanOrNot != 25:
        if scanOrNot[0] == 14 or scanOrNot[0] == 25:
            break
        
        del scanOrNot[:]

        scanOrNot = [ord(char) - 96 for char in input('Do you want to scan? (y/n)').lower()]
    
    while scanOrNot[0]==14 or scanOrNot[0]==25:
        # user responds w/ no
        if scanOrNot[0] == 14:
            break
        # user responds w/ yes
        elif scanOrNot[0] == 25:
            sleeper()

            if (typeOfObject == 1 and scanObject == 0) or (scanObject == 1):
                # object scanned is an accretion disk around a star
                print("The probe conducts a scan and matches up the results with a phenomenon called an accretion disk around a star.")
                sleeper()
                print("The disk, over a period of thousands if not millions of years, will be pulled together by gravity into planets.")
                sleep(6)
                
                if craftDamaged >= 1 and craftDamaged <= 48:
                    # chooses whether craft is damaged
                    print("The probe completes the scan and heads on its way through the endless void.")
                    sleep(5)
                    clear()

                    break
                elif craftDamaged >= 49 and craftDamaged <= 50:
                    # very small chance of craft being damaged
                    print("Suddenly, a tiny fragment of material from the disk is sent flying towards the probe.")
                    sleeper()
                    print("The probe desperately tries to avoid the speck of dust, as even the smallest debris could potentially cause catastrophic")
                    print("damage to the craft if allowed to hit it.")
                    sleeper()
                    print("But its maneuvers are to no avail, and the craft sustains a hit. Fortunately, the craft sustains only minimal damage.")
                    sleeper()

                    if Inventory.hullShield == 0:
                        temp = Inventory.hp
                        Inventory.hp -= 20
                        print("The probe took ", (temp-Inventory.hp), " damage!")
                    elif Inventory.hullShield == 1:
                        temp = Inventory.hp
                        Inventory.hp -= 15
                        print("The probe's shields absorb some of the damage, but the probe still takes ", (temp-Inventory.hp), " damage!")
                    elif Inventory.hullShield == 2:
                        temp = Inventory.hp
                        Inventory.hp -= 10
                        print("The probe's shields absorb some of the damage, but the probe still takes ", (temp-Inventory.hp), " damage!")
                    elif Inventory.hullShield == 3:
                        temp = Inventory.hp
                        Inventory.hp -= 5
                        print("The probe's shields absorb most of the damage, but the probe still takes ", (temp-Inventory.hp), " damage!")
                    elif Inventory.hullShield >= 4:
                        print("The probe's shields are strong enough to absorb all of the impact!")

                    sleep(7.5)
                    clear()
                    break
            elif (typeOfObject == 2 and scanObject == 0) or (scanObject == 2):
                # probe encounters an asteroid
                print("The probe conducts a scan and matches up the results with an iron-rich asteroid.")
                sleeper()
                    
                if asteroidSize == 1: # if the asteroid is small
                    print("The probe determines the asteroid is safe to approach and starts mining materials from it.")

                    if asteroidType >= 1 and asteroidType <= 25:
                        temp = Inventory.iron
                        sleeper()
                        Inventory.iron += matsGained
                        print("You got ", (Inventory.iron - temp), " iron!")
                        sleep(3)
                        print("The probe decides it's finished and heads on its way.")

                        break
                    elif asteroidType >= 26 and asteroidType <= 50:
                        temp = Inventory.nickel
                        sleeper()
                        Inventory.nickel += matsGained
                        print("You got ", (Inventory.nickel - temp), " nickel!")
                        sleep(3)
                        print("The probe decides it's finished and heads on its way.")

                        break
                    elif asteroidType >= 51 and asteroidType <= 75:
                        temp = Inventory.copper
                        sleeper()
                        Inventory.copper += matsGained
                        print('You got ', (Inventory.copper - temp), ' copper!')
                        sleep(3)
                        print("The probe decides it's finished and heads on its way.")

                        break
                    elif asteroidType >= 76 and asteroidType <= 91:
                        temp = Inventory.gold
                        sleeper()
                        Inventory.copper += matsGained
                        print('You got', (Inventory.gold - temp), ' gold!')
                        sleep(3)
                        print("The probe decides it's finished and heads on its way.")

                        break
                    elif asteroidType >= 92 and asteroidType <= 106:
                        temp = Inventory.platinum
                        sleeper()
                        Inventory.copper += matsGained
                        print('You got', (Inventory.platinum - temp), ' platinum!')
                        sleep(3)
                        print("The probe decides it's finished and heads on its way.")

                        break
                    elif asteroidType >= 107 and asteroidType <= 110:
                        temp = Inventory.unobtanium
                        sleeper()
                        Inventory.unobtanium += unobtaniumGained
                        sleeper()
                        print("The probe has to pause for a moment to comprehend what its sensors are detecting.")
                        sleeper()
                        print("If nothing is faulty, the probe has indeed just stumbled on unobtanium, the rarest material in the universe.")
                        sleep(3)
                        print("Taking extra care to extract the material, the probe finally manages to transfer some to its storage.")
                        sleep(3)
                        print("You got", (Inventory.unobtanium - temp), " unobtanium! Congratulations!")
                        sleep(6.75)
                        print("The probe decides it's finished and heads on its way.")

                        break
                elif asteroidSize == 2: # if asteroid is big
                    print("Unfortunately, the probe can't get close enough to the asteroid to mine the metals, as the asteroid's gravity could")
                    print("pull the probe towards it and send it hurtling towards the surface below.")

                    break
    
            elif (typeOfObject == 3 and scanObject == 0) or (scanObject == 3):
                print("The probe conducts a scan and cannot match up the results with anything in its database.")
                sleeper()
                print("Upon further analysis, the probe realizes it's encountered alien ship wreckage.")
                sleeper()
                print("Although the probe can't salvage anything from the wreckage, it still takes it as a stark reminder that ")
                print("it is not alone in this universe.")
                sleep(5.5)

                break

def object_found():
    
    objectType = random.randint(1, 3) # 3 types of objects: weapons, upgrade modules (which can be used to upgrade/repair a part of the ship for free), and resource bundles (packages of free resources)

    # what type of weapon, weapon tier, etc.
    weaponType = random.randint(1, 3) # selects between 3 weapon types: lasers, railguns, and missiles
    weaponTier = random.randint(1, 54) # tiers 1-5 for weapons
    weaponUsed = random.randint(1, 10) # decides if weapon is used
    durability = random.randint(500, 5500) # each object will have a full durability of 5500

    #variables used to determine what type of upgrade the upgrade module is, what it upgrades, etc.
    upgradeTier = random.randint(1, 36) # upgrade tier selector
    upgradeType = random.randint(1, 3) # 3 types of upgrades: hull reinforcement (reduced damage), healing (if hp is full then increases total hp), weapon tier upgrade

    # variables used to determine whether certain materials are in resource bundles or not
    bundleGen1 = random.randint(1, 500)
    bundleGen2 = random.randint(1, 500)
    bundleGen3 = random.randint(1, 2500)
    bundleGen4 = random.randint(1, 5000)
    bundleGen5 = random.randint(1, 50)

    # variables all used to decide whether each resource bundle has a certain material or not
    # very small chance of a bundle containing nothing
    ironInBundle = bundleGen1 > bundleGen2
    nickelInBundle = bundleGen1 > bundleGen2
    copperInBundle = bundleGen1 > bundleGen2
    goldInBundle = bundleGen1 > bundleGen2
    platinumInBundle = bundleGen1 > bundleGen2
    unobtaniumInBundle = (bundleGen1>bundleGen2 and bundleGen1+bundleGen2>=bundleGen4 and bundleGen4<=bundleGen3) or (bundleGen5 <= bundleGen1+bundleGen2+bundleGen3+bundleGen4)

    # variable used to prevent user from getting too many different materials in one bundle
    amountGained = 0

    matsGained = random.randint(10, 30) # amount of materials gained
    unobtaniumGained = random.randint(1, 5) # amount of unobtanium gained

    if objectType == 1: # if object is a weapon

        if weaponTier >= 1 and weaponTier <= 19:
            if weaponType == 1:
                pass
            elif weaponType == 2:
                pass
            else:
                pass
        elif weaponTier >= 20 and weaponTier <= 34:
            if weaponType == 1:
                pass
            elif weaponType == 2:
                pass
            else:
                pass
        elif weaponTier >= 35 and weaponTier <= 45:
            if weaponType == 1:
                pass
            elif weaponType == 2:
                pass
            else:
                pass
        elif weaponTier >= 46 and weaponTier <= 51:
            if weaponType == 1:
                pass
            elif weaponType == 2:
                pass
            else:
                pass
        elif weaponTier <= 52 and weaponTier <= 54:
            if weaponType == 1:
                pass
            elif weaponType == 2:
                pass
            else:
                pass

    elif objectType == 2: # if object is an upgrade

        if upgradeTier >= 1 and upgradeTier <= 19: # tier 1

            if upgradeType == 1: # shield upgrade module
                print("The probe finds a module floating in space.")
                sleep(3.3)
                print("Upon further analysis, the probe finds that the module can be used to upgrade its shields.")
                sleep(2.75)

                if Inventory.hullShield > 6 and Inventory.hullShield < 7:
                    temp = Inventory.hullShield
                    Inventory.hullShield = 7
                    print("+", (Inventory.hullShield-temp), "Shield!")
                elif Inventory.hullShield <= 6:
                    Inventory.hullShield += 1
                    print("+1 Shield!")
                else:
                    print("Your shield is already maxed out (7 Shield), so you can't get any more.")

                sleep(6)
                clear()
            elif upgradeType == 2: # hull reinforcement module
                print("The probe finds a module floating in space.")
                sleep(3.3)
                print("Upon further analysis, the probe finds that the module can be used to")
                print("repair and reinforce its hull.")
                sleep(2.75)

                if Inventory.hp > 970 and Inventory.hp < 1000:
                    temp = Inventory.hp
                    Inventory.hp = 1000
                    print("+", (Inventory.hp-temp), " HP!")
                elif Inventory.hp <= 970:
                    Inventory.hp += 30
                    print("+30 HP!")
                else:
                    print("Your HP is already maxed (1000 HP), so you can't get any more.")
                
                sleep(6)
                clear()
            else: # hp regen module
                print("The probe finds a module floating in space.")
                sleep(3.3)
                print("Upon further analysis, the probe finds that the module can be used to")
                print("boost the probe's regeneration.")
                sleep(2.75)

                if Inventory.healthRegen > 29 and Inventory.healthRegen < 30:
                    temp = Inventory.healthRegen
                    Inventory.healthRegen = 30
                    print("+", (Inventory.healthRegen-temp), "Regen!")
                elif Inventory.healthRegen <=29:
                    Inventory.healthRegen += 1
                    print("+1 Regen!")
                else:
                    print("HP Regen is already maxed out (30), so you can't get any more.")
            
        elif upgradeTier >= 20 and upgradeTier <= 31: # tier 2
            if upgradeType == 1: # shield upgrade module
                print("The probe finds a module floating in space.")
                sleep(3.3)
                print("Upon further analysis, the probe finds that the module can be used to upgrade its shields.")
                sleep(2.75)

                if Inventory.hullShield > 5 and Inventory.hullShield < 7:
                    temp = Inventory.hullShield
                    Inventory.hullShield = 7
                    print("+", (Inventory.hullShield-temp), "Shield!")
                elif Inventory.hullShield <= 5:
                    Inventory.hullShield += 2
                    print("+2 Shield!")
                else:
                    print("Your shield is already maxed out (7 Shield), so you can't get any more.")

                sleep(6)
                clear()
            elif upgradeType == 2: # hull reinforcement module
                print("The probe finds a module floating in space.")
                sleep(3.3)
                print("Upon further analysis, the probe finds that the module can be used to")
                print("repair and reinforce its hull.")
                sleep(2.75)

                if Inventory.hp > 930 and Inventory.hp < 1000:
                    temp = Inventory.hp
                    Inventory.hp = 1000
                    print("+", (Inventory.hp-temp), " HP!")
                elif Inventory.hp <= 930:
                    Inventory.hp += 70
                    print("+70 HP!")
                else:
                    print("Your HP is already maxed (1000 HP), so you can't get any more.")
                
                sleep(6)
                clear()
            else: # hp regen module
                print("The probe finds a module floating in space.")
                sleep(3.3)
                print("Upon further analysis, the probe finds that the module can be used to")
                print("boost the probe's regeneration.")
                sleep(2.75)

                if Inventory.healthRegen > 27 and Inventory.healthRegen < 30:
                    temp = Inventory.healthRegen
                    Inventory.healthRegen = 30
                    print("+", (Inventory.healthRegen-temp), "Regen!")
                elif Inventory.healthRegen <=27:
                    Inventory.healthRegen += 3
                    print("+3 Regen!")
                else:
                    print("HP Regen is already maxed out (30), so you can't get any more.")

        else: # tier 3
            if upgradeType == 1: # shield upgrade module
                print("The probe finds a module floating in space.")
                sleep(3.3)
                print("Upon further analysis, the probe finds that the module can be used to upgrade its shields.")
                sleep(2.75)

                if Inventory.hullShield > 4 and Inventory.hullShield < 7:
                    temp = Inventory.hullShield
                    Inventory.hullShield = 7
                    print("+", (Inventory.hullShield-temp), "Shield!")
                elif Inventory.hullShield <=4:
                    Inventory.hullShield += 3
                    print("+2 Shield!")
                else:
                    print("Your shield is already maxed out (7 Shield), so you can't get any more.")
                
                sleep(6)
                clear()
            elif upgradeType == 2: # hull reinforcement module
                print("The probe finds a module floating in space.")
                sleep(3.3)
                print("Upon further analysis, the probe finds that the module can be used to")
                print("repair and reinforce its hull.")
                sleep(2.75)

                if Inventory.hp > 900 and Inventory.hp < 1000:
                    temp = Inventory.hp
                    Inventory.hp = 1000
                    print("+", (Inventory.hp-temp), " HP!")
                elif Inventory.hp <= 900:
                    Inventory.hp += 100
                    print("+100 HP!")
                elif Inventory.hp == 1000:
                    print("Your HP is already maxed-out (1000 HP), so you can't get any more.")
                
                sleep(6)
                clear()
            else: # health regen module
                print("The probe finds a module floating in space.")
                sleep(3.3)
                print("Upon further analysis, the probe finds that the module can be used to boost its")
                print("hull regeneration.")
                sleep(2.75)

                if Inventory.healthRegen < 30:
                    Inventory.healthRegen += 5
                    print("+5 Regen!")
                else:
                    print("HP Regen is already maxed out (30), so you can't get any more.")
                
                sleep(6)
                clear()

    elif objectType == 3: # if object is a resource bundle

        while amountGained <= 3:

            if ironInBundle==True and amountGained<=3:
                temp = Inventory.iron
                Inventory.iron += matsGained
                amountGained += 1
                print("You got ", (Inventory.iron - temp), " iron!")
            elif ironInBundle==False and amountGained<=3:
                pass
            elif ironInBundle==False and amountGained>=3:
                break
            
            if nickelInBundle==True:
                temp = Inventory.nickel
                Inventory.nickel += matsGained
                amountGained += 1
                print("You got ", (Inventory.nickel - temp), " nickel!")
            elif nickelInBundle==False and amountGained<=3:
                pass
            elif nickelInBundle==False and amountGained>=3:
                break
                
            if copperInBundle==True:
                temp = Inventory.copper
                Inventory.copper += matsGained
                amountGained += 1
                print("You got ", (Inventory.copper), " copper!")
            elif copperInBundle==False and amountGained<=3:
                pass
            elif copperInBundle==False and amountGained>=3:
                break
                
            if goldInBundle==True:
                temp = Inventory.copper
                Inventory.gold += matsGained
                amountGained += 1
                print("You got ", (Inventory.gold), " gold!")
            elif goldInBundle==False and amountGained<=3:
                pass
            elif goldInBundle==False and amountGained>=3:
                break
                
            if platinumInBundle==True:
                temp = Inventory.platinum
                Inventory.platinum += matsGained
                amountGained += 1
                print("You got ", (Inventory.platinum), " platinum!")
            elif platinumInBundle==False and amountGained<=3:
                pass
            elif platinumInBundle==False and amountGained>=3:
                break
                
            if unobtaniumInBundle==True:
                temp = Inventory.unobtanium
                Inventory.platinum += matsGained
                unobtaniumGained += 1
                sleeper()
                print("The probe has to pause for a moment to comprehend what its sensors are detecting.")
                sleeper()
                print("If nothing is faulty, the probe has indeed just stumbled on unobtanium, the rarest material in the universe.")
                sleep(3)
                print("Taking extra care to extract the material, the probe finally manages to transfer some to its storage.")
                sleep(3)
                print("You got", (Inventory.unobtanium - temp), " unobtanium!")
                sleep(6.75)
                print("The probe decides it's finished and heads on its way.")
            elif unobtaniumInBundle==False and amountGained<=3:
                pass
            elif unobtaniumInBundle==False and amountGained>=3:
                break