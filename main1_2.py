from Hero1_2 import *
from Armor1_2 import *


player = Hero()
print(player.inventory)
for i in player.inventory:
    print(i)
player.equipGloves()
print(player.inventory)
print(player.gloveseq[0])
print(player.inventory)
gloves = Gloves()
player.inventory.append(gloves)
player.equipGloves()
print(player.gloveseq[0])

# print(player)
# while player.level < 5:
#     xp = random.randint(10, 50)
#     player.addXp(xp)





