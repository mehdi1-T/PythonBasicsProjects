import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    dice = [dice1, dice2]

    print(f"{dice}")


while True:
    roll = input("Do you wanna roll the dice(y/n): ")

    if roll == "y":
        roll_dice()

    elif roll == "n":
        print("its okay")
        break

    else:
        print("Invalude input")

    cont = input("Continue(y/n): ")

    if cont.lower() != "y":
        print("Exeting...")
        break
        
    