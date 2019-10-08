import random

mobs = ["zombie","witch","spider","skeleton","creeper", "ender dragon"]
inventory = ["health potion","smoked trout", "50 gold pieces"]
loot_table = ["rotting flesh","spider fang","linen cloth","sorcerer's robes of the bear","thigh bone","one-handed sword", "1 gold piece"]

# Encounter a mob
mob = mobs[random.randint(0,len(mobs)-1)]
print("Fighting " + mob)

# Kill the mob
print("Killed " + mob)

# Loot the mob
print("Loot " + mob)
drops = random.randint(2,4)
loot = []
for i in range(drops):
    loot.append(loot_table[random.randint(0,len(loot_table)-1)])

print("Drops: ", loot)

inventory += loot
print("Inventory: ", inventory)

