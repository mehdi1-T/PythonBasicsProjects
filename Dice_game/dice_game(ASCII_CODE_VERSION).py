import random

DICE_ASCII = {
    1: """
 ┌─────────┐
 │         │
 │    ●    │
 │         │
 └─────────┘
""",
    2: """
 ┌─────────┐
 │  ●      │
 │         │
 │      ●  │
 └─────────┘
""",
    3: """
 ┌─────────┐
 │  ●      │
 │    ●    │
 │      ●  │
 └─────────┘
""",
    4: """
 ┌─────────┐
 │  ●   ●  │
 │         │
 │  ●   ●  │
 └─────────┘
""",
    5: """
 ┌─────────┐
 │  ●   ●  │
 │    ●    │
 │  ●   ●  │
 └─────────┘
""",
    6: """
 ┌─────────┐
 │  ●   ●  │
 │  ●   ●  │
 │  ●   ●  │
 └─────────┘
"""
}


nbr1 = random.randint(1, 6)   # First dice
nbr2 = random.randint(1, 6)   # Second dice

dice1 = DICE_ASCII[nbr1].strip().split("\n")  # Makes a list of 5 lines
dice2 = DICE_ASCII[nbr2].strip().split("\n")  # Same for second dice

for i in range(5):  # There are 5 lines in each dice
    print(dice1[i] + "     " + dice2[i])
