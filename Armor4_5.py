import random


class Equipment(object):
    RARITY = ["Trash","Common","Rare","Epic","Legendary"]

    def __init__(self,eqType):
        self.rarityLevel, self.rareMod = self.pickRare()
        self.eqType = eqType

    def pickRare(self):
        x = random.randint(1, 10)
        if x >= 1 and x <= 2:
            return Equipment.RARITY[0],2
        elif x > 2 and x <= 5:
            return Equipment.RARITY[1],4
        elif x > 5 and x < 8:
            return Equipment.RARITY[2],8
        elif x >= 8 and x <= 9:
            return Equipment.RARITY[3],16
        elif x == 10:
            return Equipment.RARITY[4],32

class Armor(Equipment):
    ARMORTYPE = ["Helm", "Chest", "Legs", "Boots", "Gloves"]

    def __init__(self,aType):
        super(Armor,self).__init__("Armor")
        self.armorType = aType
        self.armor = 0
        self.stamina = 0
        self.agi = 0
        self.iq = 0
        self.luck = 0

    def __str__(self):
        return """
            armorType: {}
            Rarity Level: {}
            Armor: {}
            Luck: {}
            Stamina: {}
            IQ: {}
            Agility: {}
            """.format(self.armorType, self.rarityLevel, self.armor, self.luck, self.stamina, self.iq, self.agi)

class Helm(Armor):
    def __init__(self):
        super(Helm,self).__init__(Armor.ARMORTYPE[0])
        self.armor = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(0, 8) + self.rareMod
        self.agi = random.randint(0, 8) + self.rareMod
        self.iq = random.randint(0, 8) + self.rareMod
        self.luck = random.randint(0, 8) + self.rareMod

class Chest(Armor):
    def __init__(self):
        super(Chest,self).__init__(Armor.ARMORTYPE[1])
        self.armor = random.randint(5, 25) * self.rareMod
        self.stamina = random.randint(0, 25) + self.rareMod
        self.agi = random.randint(0, 25) + self.rareMod
        self.iq = random.randint(0, 25) + self.rareMod
        self.luck = random.randint(0, 25) + self.rareMod

class Legs(Armor):
    def __init__(self):
        super(Legs,self).__init__(Armor.ARMORTYPE[2])
        self.armor = random.randint(5, 15) * self.rareMod
        self.stamina = random.randint(0, 15) + self.rareMod
        self.agi = random.randint(0, 15) + self.rareMod
        self.iq = random.randint(0,15) + self.rareMod
        self.luck = random.randint(0, 15) + self.rareMod

class Boots(Armor):
    def __init__(self):
        super(Boots,self).__init__(Armor.ARMORTYPE[3])
        self.armor = random.randint(5, 10) * self.rareMod
        self.stamina = random.randint(0, 8) + self.rareMod
        self.agi = random.randint(0, 8) + self.rareMod
        self.iq = random.randint(0, 8) + self.rareMod
        self.luck = random.randint(0, 8) + self.rareMod

class Gloves(Armor):
    def __init__(self):
        super(Gloves,self).__init__(Armor.ARMORTYPE[4])
        self.armor = random.randint(5, 8) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod

class Weapon(Equipment):
    WEAPONTYPE = ["Sword","Gun","Bow","Axe","Mace","Wand","Staff","Dagger"]

    def __init__(self, wType):
        super(Weapon, self).__init__("Weapon")
        self.weaponType = wType
        self.damage = 0
        self.stamina = 0
        self.agi = 0
        self.iq = 0
        self.luck = 0

    def __str__(self):
        return """
                weaponType: {}
                Rarity Level: {}
                Damage: {}
                Luck: {}
                Stamina: {}
                IQ: {}
                Agility: {}
                """.format(self.weaponType, self.rarityLevel, self.damage, self.luck, self.stamina, self.iq, self.agi)

class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__("Sword")
        self.damage = random.randint(5, 8) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod

class Gun(Weapon):
    def __init__(self):
        super(Gun, self).__init__("Gun")
        self.damage = random.randint(3, 10) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod

class Bow(Weapon):
    def __init__(self):
        super(Bow, self).__init__("Bow")
        self.damage = random.randint(5, 8) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod

class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__("Axe")
        self.damage = random.randint(3, 10) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod

class Mace(Weapon):
    def __init__(self):
        super(Mace, self).__init__("Mace")
        self.damage = random.randint(2, 12) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod

class Wand(Weapon):
    def __init__(self):
        super(Wand, self).__init__("Wand")
        self.damage = random.randint(5, 8) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod

class Staff(Weapon):
    def __init__(self):
        super(Staff, self).__init__("Staff")
        self.damage = random.randint(8, 10) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod

class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__("Dagger")
        self.damage = random.randint(5, 7) * self.rareMod
        self.stamina = random.randint(0, 5) + self.rareMod
        self.agi = random.randint(0, 5) + self.rareMod
        self.iq = random.randint(0, 5) + self.rareMod
        self.luck = random.randint(0, 5) + self.rareMod
