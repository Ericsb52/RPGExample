import random
from Armor4_5 import *

class Hero(object):
    RACELIST = ["Human","Elf","Dwarf","Dog"]
    CLASSLIST = ["Warrior","Mage","Hunter","Dog"]

    def __init__(self):
        # class setup String values
        self.isAlive = True
        self.level = 1
        self.race = self.pickRace()
        self.playerClass = self.pickClass()
        self.name = self.enterName()
        # class setup starting XP and leveling vallues
        self.xp = 0
        self.xpToLevelUp = 90 + (self.level * 10)
        # hero health initial setup
        self.healthMod = 10
        self.maxHealth = self.level * self.healthMod
        self.healAct = self.maxHealth
        # hero Mana inatial setup
        self.manaMod = 10
        self.maxmana = self.level * self.manaMod
        self.manaAct = self.maxmana
        # hero stat modifiers
        self.deff = 0
        self.atk = 0
        self.luck = 0
        self.stamina = 0
        self.iq = 0
        self.agi = 0
        # seting base values based on class and race
        self.setMods()

        #setup hero inventorys
        self.inventory = []
        self.maxinv = 10
        self.helmeq = []
        self.chesteq = []
        self.legeq = []
        self.gloveseq = []
        self.bootseq = []
        self.righthandwep = []
        self.lefthandwep = []
        self.popInv()

    def popInv(self):
        # give some random pots
        x = random.randint(0,4)
        for i in range(x):
            y = random.randint(0, 1)
            if y == 1:
                self.addToInv("Health potion")
            else:
                self.addToInv("Mana potion")
        helm = Helm()
        chest = Chest()
        legs = Legs()
        boots = Boots()
        gloves = Gloves()
        x = random.randint(0, 7)
        if x == 0:
            weapon = Sword()
        elif x == 1:
            weapon = Gun()
        elif x == 2:
            weapon = Bow()
        elif x == 3:
            weapon = Axe()
        elif x == 4:
            weapon = Mace()
        elif x == 5:
            weapon = Wand()
        elif x == 6:
            weapon = Staff()
        else:
            weapon = Dagger()
        self.addToInv(helm)
        self.addToInv(chest)
        self.addToInv(legs)
        self.addToInv(boots)
        self.addToInv(gloves)
        self.addToInv(weapon)

    def addToInv(self,item):
        if len(self.inventory) < self.maxinv:
            self.inventory.append(item)
        else:
            print("no room in inventory")
            return

    def setMods(self):
        #this method sets the starting modifyer values for your hero
        if self.playerClass == "Warrior":
            self.deff = random.randint(5, 20)
            self.atk = random.randint(5, 15)
            self.luck = random.randint(1, 4)
            self.stamina = random.randint(15, 20)
            self.iq = 1
            self.agi = random.randint(1, 5)
            self.maxmana = 0
        if self.playerClass == "Mage":
            self.deff = random.randint(5, 10)
            self.atk = random.randint(10, 20)
            self.luck = random.randint(1, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint(5, 20)
            self.agi = random.randint(1, 5)
            self.manaMod = random.randint(15,20)
        if self.playerClass == "Hunter":
            self.deff = random.randint(5, 15)
            self.atk = random.randint(8, 18)
            self.luck = random.randint(5, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint(5, 12)
            self.agi = random.randint(5, 15)
        if self.playerClass == "Dog":
            self.deff = random.randint(90,100)
            self.atk = 100
            self.luck = 100
            self.stamina = 100
            self.iq = 100
            self.agi = 100
        if self.race == "Elf":
            self.stamina -= 2
            self.iq += 2
        if self.race == "Dwarf":
            self.stamina += 2
            self.iq -= 2
        if self.race == "Dog":
            self.atk += 10
            self.deff += 10
            self.luck += 10
            self.stamina += 10
            self.iq += 10
            self.agi += 10

    def __str__(self):
        # provides a String representation of the object
        return """
        Name: {} \t Race: {} \t Class: {} \t Level: {}
        Health: {} \t Mana: {} \t Xp: {}
        Atack: {} \t Deffence: {}
        Luck: {} \t Stamina: {}
        IQ: {}     \t Agility: {}
        """.format(self.name, self.race, self.playerClass, self.level, self.healAct, self.manaAct, self.xp, self.atk,
                   self.deff, self.luck, self.stamina, self.iq, self.agi)

    def pickRace(self):
        # allows us to pick our race from the class race list
        while True:
            try:
                print(Hero.RACELIST)
                x = input("pick your Race")
                if x in Hero.RACELIST:
                    return x
            except:
                print("Not a good option")

    def pickClass(self):
        # allows us to pick our class from the class list
        while True:
            try:
                print(Hero.CLASSLIST)
                x = input("pick your Race")
                if x in Hero.CLASSLIST:
                    return x
            except:
                print("Not a good option")

    def enterName(self):
        # lets us set up our hero's name
        name = ""
        while name == "":
            name = input("What would you like to name this character")
        return name

    def die(self):
        if self.healAct <= 0:
            self.isAlive = False
            # we need to unequip all items and put back in inventory
            dropXp = 10 * self.level
            dropitem = random.choice(self.inventory)

            return dropXp, dropitem

        else:
            return "",""

    def levelUp(self):

        if self.xp >= self.xpToLevelUp:
            print("Ding Level up")
            print(self)
            remxp = self.xp - self.xpToLevelUp
            self.level += 1
            self.xpToLevelUp = 90 + (self.level * 10)
            self.xp = remxp

            self.healthMod = self.healthMod + self.level
            self.maxHealth = self.level * self.healthMod
            self.healAct = self.maxHealth
            if self.playerClass != "Warrior":
                self.manaMod = self.manaMod + self.level
                self.maxmana = self.level * self.manaMod
                self.manaAct = self.maxmana
            self.levelMod()
        else:
            return

    def levelMod(self):
        points = random.randint(1, self.level+1)
        while points > 0:
            print("""
                Luck: {}
                Stamina: {}
                IQ: {}
                Agility: {}""".format(self.luck, self.stamina, self.iq, self.agi))
            x = input("what Stat would you like to add points to")
            y = int(input(self.name+" you have " + str(points) + " points to spend how many would you like to put in " + x))
            if x == "Stamina":
                self.stamina += y
                points -= y
            elif x == "Luck":
                self.luck += y
                points -= y
            elif x == "IQ":
                self.iq += y
                points -= y
            elif x == "Agility":
                self.agi += y
                points -= y
            else:
                print("not an option")

    def collectXp(self,xp):
        print("you picked up "+str(xp)+"xp")
        self.xp += xp
        self.levelUp()

    def equipGloves(self):
        for i in self.inventory:
            x = type(i)
            if "Gloves" in str(x):
                if len(self.gloveseq) < 1:
                    print("you equiped a set of gloves")
                    print(i)
                    self.gloveseq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.gloveseq[0].armor
                    self.luck += self.gloveseq[0].luck
                    self.stamina += self.gloveseq[0].stamina
                    self.iq += self.gloveseq[0].iq
                    self.agi += self.gloveseq[0].agi
                else:
                    print("you are wearing a pair of gloves")
                    print(self.gloveseq[0])
                    print("would you like to replace them with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your gloves")
                            self.deff -= self.gloveseq[0].armor
                            self.luck -= self.gloveseq[0].luck
                            self.stamina -= self.gloveseq[0].stamina
                            self.iq -= self.gloveseq[0].iq
                            self.agi -= self.gloveseq[0].agi
                            self.gloveseq.remove(self.gloveseq[0])
                            self.gloveseq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.gloveseq[0].armor
                            self.luck += self.gloveseq[0].luck
                            self.stamina += self.gloveseq[0].stamina
                            self.iq += self.gloveseq[0].iq
                            self.agi += self.gloveseq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equipHelm(self):
        for i in self.inventory:
            x = type(i)
            if "Helm" in str(x):
                if len(self.helmeq) < 1:
                    print("you equiped a  helm")
                    print(i)
                    self.helmeq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.helmeq[0].armor
                    self.luck += self.helmeq[0].luck
                    self.stamina += self.helmeq[0].stamina
                    self.iq += self.helmeq[0].iq
                    self.agi += self.helmeq[0].agi
                else:
                    print("you are wearing a p helm")
                    print(self.helmeq[0])
                    print("would you like to replace it with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your helm")
                            self.deff -= self.helmeq[0].armor
                            self.luck -= self.helmeq[0].luck
                            self.stamina -= self.helmeq[0].stamina
                            self.iq -= self.helmeq[0].iq
                            self.agi -= self.helmeq[0].agi
                            self.helmeq.remove(self.helmeq[0])
                            self.helmeq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.helmeq[0].armor
                            self.luck += self.helmeq[0].luck
                            self.stamina += self.ghelmq[0].stamina
                            self.iq += self.helmeq[0].iq
                            self.agi += self.helmeq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equipChest(self):
        for i in self.inventory:
            x = type(i)
            if "Chest" in str(x):
                if len(self.chesteq) < 1:
                    print("you equiped a Chest")
                    print(i)
                    self.chesteq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.chesteq[0].armor
                    self.luck += self.chesteq[0].luck
                    self.stamina += self.chesteq[0].stamina
                    self.iq += self.chesteq[0].iq
                    self.agi += self.chesteq[0].agi
                else:
                    print("you are wearing a Chest")
                    print(self.chesteq[0])
                    print("would you like to replace it with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your Chest")
                            self.deff -= self.chesteq[0].armor
                            self.luck -= self.chesteq[0].luck
                            self.stamina -= self.chesteq[0].stamina
                            self.iq -= self.chesteq[0].iq
                            self.agi -= self.chesteq[0].agi
                            self.chesteq.remove(self.chesteq[0])
                            self.chesteq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.chesteq[0].armor
                            self.luck += self.chesteq[0].luck
                            self.stamina += self.chesteq[0].stamina
                            self.iq += self.chesteq[0].iq
                            self.agi += self.chesteq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equipLegs(self):
        for i in self.inventory:
            x = type(i)
            if "Legs" in str(x):
                if len(self.legeq) < 1:
                    print("you equiped a Legs")
                    print(i)
                    self.legeq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.legeq[0].armor
                    self.luck += self.legeq[0].luck
                    self.stamina += self.legeq[0].stamina
                    self.iq += self.legeq[0].iq
                    self.agi += self.legeq[0].agi
                else:
                    print("you are wearing a Legs")
                    print(self.legeq[0])
                    print("would you like to replace it with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your Legs")
                            self.deff -= self.legeq[0].armor
                            self.luck -= self.legeq[0].luck
                            self.stamina -= self.legeq[0].stamina
                            self.iq -= self.legeq[0].iq
                            self.agi -= self.legeq[0].agi
                            self.legeq.remove(self.legeq[0])
                            self.gloveseq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.legeq[0].armor
                            self.luck += self.legeq[0].luck
                            self.stamina += self.legeq[0].stamina
                            self.iq += self.legeq[0].iq
                            self.agi += self.legeq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equipBoots(self):
        for i in self.inventory:
            x = type(i)
            if "Boots" in str(x):
                if len(self.bootseq) < 1:
                    print("you equiped a Boots")
                    print(i)
                    self.bootseq.append(i)
                    self.inventory.remove(i)
                    self.deff += self.bootseq[0].armor
                    self.luck += self.bootseq[0].luck
                    self.stamina += self.bootseq[0].stamina
                    self.iq += self.bootseq[0].iq
                    self.agi += self.bootseq[0].agi
                else:
                    print("you are wearing a Boots")
                    print(self.bootseq[0])
                    print("would you like to replace it with")
                    print(i)
                    while True:
                        x = input("yes or no")
                        if x == "yes":
                            print("you replaced your Boots")
                            self.deff -= self.bootseq[0].armor
                            self.luck -= self.bootseq[0].luck
                            self.stamina -= self.bootseq[0].stamina
                            self.iq -= self.bootseq[0].iq
                            self.agi -= self.bootseq[0].agi
                            self.bootseq.remove(self.bootseq[0])
                            self.gloveseq.append(i)
                            self.inventory.remove(i)
                            self.deff += self.bootseq[0].armor
                            self.luck += self.bootseq[0].luck
                            self.stamina += self.bootseq[0].stamina
                            self.iq += self.bootseq[0].iq
                            self.agi += self.bootseq[0].agi

                            break
                        elif x == "no":
                            self.inventory.remove(i)
                            break

    def equipWeapon(self):
        for i in self.inventory:
            x = type(i)
            if ("Sword" in str(x) or "Gun" in str(x) or "Bow" in str(x) or "Axe" in str(x)or
                "Mace" in str(x) or "Wand" in str(x) or "Staff" in str(x) or "Dagger" in str(x)):
                while True:
                    x = input("would you like to equip the weppon in your right or left hand")
                    if x == "right":
                        if len(self.righthandwep) < 1:
                            print("you equiped a weapon in your right hand")
                            print(i)
                            self.righthandwep.append(i)
                            self.inventory.remove(i)
                            self.atk += self.righthandwep[0].damage
                            self.luck += self.righthandwep[0].luck
                            self.stamina += self.righthandwep[0].stamina
                            self.iq += self.righthandwep[0].iq
                            self.agi += self.righthandwep[0].agi
                            break
                        else:
                            print("you allredy have a weapon in that hand")
                            print(self.righthandwep[0])
                            print("would you like to replace it with")
                            print(i)
                            while True:
                                x = input("yes or no")
                                if x == "yes":
                                    print("you replaced your Boots")
                                    self.atk -= self.righthandwep[0].damage
                                    self.luck -= self.righthandwep[0].luck
                                    self.stamina -= self.righthandwep[0].stamina
                                    self.iq -= self.righthandwep[0].iq
                                    self.agi -= self.righthandwep[0].agi
                                    self.righthandwep.remove(self.righthandwep[0])
                                    self.righthandwep.append(i)
                                    self.inventory.remove(i)
                                    self.atk += self.righthandwep[0].damage
                                    self.luck += self.righthandwep[0].luck
                                    self.stamina += self.righthandwep[0].stamina
                                    self.iq += self.righthandwep[0].iq
                                    self.agi += self.righthandwep[0].agi

                                    break
                                elif x == "no":
                                    self.inventory.remove(i)
                                    break
                                break

                    elif x == "left":
                        if len(self.lefthandwep) < 1:
                            print("you equiped a weapon in your right hand")
                            print(i)
                            self.lefthandwep.append(i)
                            self.inventory.remove(i)
                            self.atk += self.lefthandwep[0].damage
                            self.luck += self.lefthandwep[0].luck
                            self.stamina += self.lefthandwep[0].stamina
                            self.iq += self.lefthandwep[0].iq
                            self.agi += self.lefthandwep[0].agi
                            break
                        else:
                            print("you allredy have a weapon in that hand")
                            print(self.lefthandwep[0])
                            print("would you like to replace it with")
                            print(i)
                            while True:
                                x = input("yes or no")
                                if x == "yes":
                                    print("you replaced your Boots")
                                    self.atk -= self.lefthandwep[0].damage
                                    self.luck -= self.lefthandwep[0].luck
                                    self.stamina -= self.lefthandwep[0].stamina
                                    self.iq -= self.lefthandwep[0].iq
                                    self.agi -= self.lefthandwep[0].agi
                                    self.lefthandwep.remove(self.lefthandwep[0])
                                    self.lefthandwep.append(i)
                                    self.inventory.remove(i)
                                    self.atk += self.lefthandwep[0].damage
                                    self.luck += self.lefthandwep[0].luck
                                    self.stamina += self.lefthandwep[0].stamina
                                    self.iq += self.lefthandwep[0].iq
                                    self.agi += self.lefthandwep[0].agi

                                    break
                                elif x == "no":
                                    self.inventory.remove(i)
                                    break
                                break
                    else:
                        print ("not an option")

    def equipAll(self):
        self.equipChest()
        self.equipHelm()
        self.equipGloves()
        self.equipLegs()
        self.equipBoots()
        self.equipWeapon()

    def attack(self):
        pass

    def defend(self):
        pass

    def useHpPotion(self):
        pass

    def useMpPotion(self):
        pass



