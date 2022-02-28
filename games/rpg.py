
def fight(p1, p2):
    if p1.attack > p2.defense:
        p2.health = 0


class Character:
    name = None
    attack = 0
    defense = 0
    health = 0


c1 = Character()
c1.name = input("what is first character name")
c1.attack = int(input(f"what is {c1.name}'s attack:"))
c1.defense = int(input(f"what is {c1.name}'s defense  "))
c1.health = int(input(f"what is {c1.name}'s health "))

c2 = Character()
c2.name = input("what is second character name")
c2.attack = int(input(f"what is {c2.name}'s attack:"))
c2.defense = int(input(f"what is {c2.name}'s defense  "))
c2.health = int(input(f"what is {c2.name}'s health "))

if c1.attack > c2.defense:
    c2.health = 0

if c2.attack > c1.defense:
    c1.health = 0

if c1.health == 0:
    print(f"{c1.name} is dead")

if c2.health == 0:
    print(f"{c2.name} is dead")

