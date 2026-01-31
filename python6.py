"""
#
# Functions
# 
"""

def myFullName(firstName="Unknown", lastName="Forger"):
    return firstName + " " + lastName

print(myFullName("Tanjiro", "kamado"))
print(myFullName(firstName="Loid"))
print(myFullName())
print(myFullName(lastName="Smith"))
print(myFullName("Anna", "forger"))
print(myFullName("Yor", "forger"))
print(myFullName("Bond", "forger"))

def redPotion(hp):
    return hp + 50
def bluePotion(hp):
    return mp + 50

current_hp = 70
print("Current HP:", current_hp)
current_hp = redPotion(current_hp)
print("After using Red Potion, HP:", current_hp)