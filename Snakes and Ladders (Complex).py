import random
print("Welcome to Snakes & Ladders.")
print("The rules are as follows: ")
def rules():
    print("1. There are two players in this game.")
    print(" ")
    print("2. The game starts with players at starting postion, which is, 0.")
    print(" ")
    print("3. The players roll the dice turn by turn and move according to the number on the dice. ")
    print(" ")
    print("4. If you land at the bottom of a ladder, you must move up.")
    print(" ")
    print("5. If you land on the mouth of a snake, you must move down. ")
    print(" ")
    print("6. If one of the players reaches the top, they win!")
    print(" ")
rules()
name1 = input("Enter name of first player: ")
name2 = input("Enter name of second player: ")
if name1 == "":
    print("Please enter something.")
    name1 = input("Enter name of first player again: ")
if name2 == "":
    print("Please enter something.")
    name2 = input("Enter name of second player again: ")
print("Deciding which player will play first...")
print(name1, "or", name2, "?")
if len(name1) >= len(name2):
    print(name1, "is 1st Player.")
else:
    print(name2, "is 1st Player.")
snakes = {
    7: 2,
    15: 4,
    27: 11,
    34: 6,
    32: 10,
    48: 26,
    88: 24,
    63: 18,
    95: 56,
    97: 78,
    98: 14
}
ladders = {
    1:38,
    4:14,
    8: 30,
    21: 42,
    28: 76,
    50: 67,
    71: 92,
    88: 99
}
snake_bite = ["Bad luck! You've been bitten by a snake! You'd have to go down.",
              "Horrible luck! A snake has bitten you!",
              "Tough luck! The snake got you. You have to go down!",
              "What a tragedy, player! You have to go down. A snake bit you!"]
ladder_jump = ["Woah! You've found a ladder! Go up!",
               "You're a champion! Climb the ladder!",
               "Hurrahh! You've done it champ. You found a ladder!.",
               "That was epic luck! Go get on that ladder!"]
dice = 0
def diceface():
    if dice == 1:
        print("|---------|")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("|---------|")
    elif dice == 2:
        print("|---------|")
        print("| 0       |")
        print("|         |")
        print("|       0 |")
        print("|---------|")
    elif dice == 3:
        print("|---------|")
        print("| 0       |")
        print("|    0    |")
        print("|       0 |")
        print("|---------|")
    elif dice == 4:
        print("|---------|")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("|---------|")
    elif dice == 5:
        print("|---------|")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("|---------|")
    elif dice == 6:
        print("|---------|")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print("|---------|")
    print("You got a", dice, "!")
print("Press ENTER to roll the dice...")
input("_")
dice = random.randint(1, 6)
diceface()
pos2 = 0
pos1 = dice
newpos1 = 0
newpos2 = 0
def check1(pos1):
    if pos1 in snakes.keys():
        return(snakes[pos1])
    elif pos1 in ladders.keys():
        return(ladders[pos1])
    else:
        return(pos1)
def positions1(newpos1):
    print("Player-1 position: ", newpos1)

def positions2(newpos2):
    print("Player-2 position: ", newpos2)
if pos1 in snakes.keys():
    print(random.choice(snake_bite))
elif pos1 in ladders.keys():
    print(random.choice(ladder_jump))
a1 = check1(pos1)
positions1(a1)
def check2(pos2):
    if pos2 in snakes.keys():
        return(snakes[pos2])
    elif pos2 in ladders.keys():
        return(ladders[pos2])
    else:
        return(pos2)
print("Player 2's chance...")
print("Press ENTER to roll the dice...")
input("_")
dice = random.randint(1, 6)
diceface()
pos2 = dice
b1 = check2(pos2)
if pos2 in snakes.keys():
    print(random.choice(snake_bite))
elif pos2 in ladders.keys():
    print(random.choice(ladder_jump))
positions2(b1)
positions1(a1)
while a1 < 100 or b1 < 100:
    if a1 >= 100 or b1 >= 100:
        if a1 == 100:
            print(name1, "WINS!")
        elif b1 == 100:
            print(name2, "WINS!")
        elif a1 > 100:
            print(name1, "WINS!")
        elif b1 > 100:
            print(name2, "WINS!")
        break
    else:
        print(name1, "'s chance...")
        print("Press ENTER to roll the dice...")
        input("_")
        dice = random.randint(1, 6)
        diceface()
        a1 += dice
        if a1 in snakes.keys():
            print(random.choice(snake_bite))
        elif a1 in ladders.keys():
            print(random.choice(ladder_jump))
        a1 = check1(a1)
        positions1(a1)
        positions2(b1)
        if a1 == 100:
            print(name1, "WINS!")
            break
        elif a1 > 100:
            print(name1, "WINS!")
            break
        print(name2,"'s chance...")
        print("Press ENTER to roll the dice...")
        input("_")
        dice = random.randint(1, 6)
        diceface()
        b1 += dice
        if b1 in snakes.keys():
            print(random.choice(snake_bite))
        elif b1 in ladders.keys():
            print(random.choice(ladder_jump))
        b1 = check2(b1)
        positions2(b1)
        positions1(a1)
