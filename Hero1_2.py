import random
from Armor1_2 import *

class Hero(object):
    RACELIST = ["Human","Elf","Dwarf","Dog"]
    CLASSLIST = ["Warrior","Mage","Hunter","Dog"]

    def __init__(self):
        self.isAlive = True
        self.level = 1
        self.race = self.pickRace()
        self.playerClass = self.pickClass()
        self.name = self.enterName()

        self.xp = 0
        self.levelup = 90 + (self.level * 10)

        self.healthMod = 10
        self.maxHealth = self.level * self.healthMod
        self.healAct = self.maxHealth

        self.manaMod = 10
        self.maxmana = self.level * self.manaMod
        self.manaAct = self.maxmana

        self.deff = 0
        self.atk = 0
        self.luck = 0
        self.stamina = 0
        self.iq = 0
        self.agi = 0
        self.atklist = []
        self.setMods()

        self.inventory = []
        self.maxInv = 10
        self.headeq = []
        self.chesteq = []
        self.legseq = []
        self.bootseq = []
        self.gloveseq = []
        self.righHandeq = []
        self.leftHandeq = []
        self.popInv()

    def popInv(self):

        helm = Helm()
        chest = Chest()
        legs = Legs()
        boots = Boots()
        gloves = Gloves()
        x = random.randint(0,7)
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
        x = random.randint(0, 3)
        for i in range(x):
            self.addToInv("Health potion")
        x = random.randint(0, 3)
        for i in range(x):
            self.addToInv("Mana potion")

    def addToInv(self, item):
        if len(self.inventory) < self.maxInv:
            self.inventory.append(item)
        else:
            print("you have to many items in your inventory")
            return

    def setMods(self):
        if self.playerClass == "Warrior":
            self.atklist = ["normal","med","strong"]
            self.deff = random.randint(5, 20)
            self.atk = random.randint(5, 15)
            self.luck = random.randint(1, 4)
            self.stamina = random.randint(15, 20)
            self.iq = 1
            self.agi = random.randint(1, 5)
            self.maxmana = 0
        if self.playerClass == "Mage":
            self.atklist = ["normal", "FireBall", "Arcane Blast"]
            self.deff = random.randint(5, 10)
            self.atk = random.randint(10, 20)
            self.luck = random.randint(1, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint(5, 20)
            self.agi = random.randint(1, 5)
            self.manaMod = random.randint(15,20)
        if self.playerClass == "Hunter":
            self.atklist = ["normal", "Aimed shot", "Volly"]
            self.deff = random.randint(5, 15)
            self.atk = random.randint(8, 18)
            self.luck = random.randint(5, 10)
            self.stamina = random.randint(5, 10)
            self.iq = random.randint(5, 12)
            self.agi = random.randint(5, 15)
        if self.playerClass == "Dog":
            self.atklist = ["normal", "Bark", "Bite"]
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
        return"""
        Name: {} \t Race: {} \t Class: {} \t Level: {}
        Health: {} \t Mana: {} \t Xp: {}
        Atack: {} \t Deffence: {}
        Luck: {} \t Stamina: {}
        IQ: {}     \t Agility: {}
        """.format(self.name,self.race,self.playerClass,self.level,self.healAct,self.manaAct,self.xp,self.atk,self.deff,self.luck,self.stamina,self.iq,self.agi)

    def pickRace(self):
        while True:
            try:
                print(Hero.RACELIST)
                x = input("pick your Race")
                if x in Hero.RACELIST:
                    return x
            except:
                print("Not a good option")

    def pickClass(self):
        while True:
            try:
                print(Hero.CLASSLIST)
                x = input("pick your Race")
                if x in Hero.CLASSLIST:
                    return x
            except:
                print("Not a good option")

    def enterName(self):
        name = ""
        while name == "":
            name = input("What would you like to name this character")
            return name

    def die(self):
        self.isAlive = False
        dropxp = 10 * self.level
        #self.unequipAll() #add in latter with inventory system
        item = random.choice(self.inventory)
        return dropxp, item

    def levelding(self):
        print("Ding you have Leveled up")
        print(self)
        if self.xp >= self.levelup:
            self.level += 1
            remxp = self.xp - self.levelup
            self.xp = remxp
            self.levelup = 90 + (self.level * 10)
            self.healthMod += self.level
            self.maxHealth = self.level * self.healthMod
            self.healAct = self.maxHealth
            if self.playerClass != "Warrior":
                self.manaMod += self.level
                self.maxmana = self.level * self.manaMod
                self.manaAct = self.maxmana
            self.levUpMod()

    def levUpMod(self):
        points = random.randint(1,self.level)
        while points > 0:
            print("""
            Luck: {}
            Stamina: {}
            IQ: {}
            Agility: {}
            """.format(self.luck,self.stamina,self.iq,self.agi))
            x = input("what Stat would you like to add points to")
            y = 0
            while y == 0:
                try:
                    y = int(input("you have " + str(points) + " points to spend how many would you like to put in " + x))
                except:
                    print("that wasn't a number")
                    y = 0
            if y <= points:
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
            else:
                print("you dont have that manny points")

    def addXp(self,xp):
        print("picked up "+str(xp)+"xp")
        self.xp += xp
        if self.xp >= self.levelup:
            self.levelding()



    def attack(self):
        pass

    def defend(self):
        pass

    def equipHead(self):

        pass

    def equipChest(self):
        pass

    def equipLegs(self):
        pass

    def equipBoots(self):
        pass

    def equipGloves(self):
        if len(self.gloveseq) < 1:
            for i in self.inventory:
                x = type(i)
                if "Gloves" in str(x):
                    print("you equiped a set of gloves")
                    print(i)
                    self.gloveseq.append(i)
                    self.inventory.remove(i)
        else:
            print("you need to remove your equipt gloves first")







    def useHpPotion(self):
        pass

    def useMpPotion(self):
        pass




