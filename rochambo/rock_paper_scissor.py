import random

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

def is_lose(player, opponent):
    if (opponent == 'r' and player == 's') or (opponent == 's' and player == 'p') or (opponent == 'p' and player == 'r'):
        return True

imojis = {
    'r' : "✊",
    'p' : "✋",
    "s" : "✌️"
}

while True:
    user = input("enter your choice (r/p/S): ")
    computer = random.choice(('r', 'p', 's'))
    print("="*30)

    print(f"you chose {imojis[user]}\ncomputer chose {imojis[computer]}")

    if user == computer:
        print("it's a tie!🤝🤝🤝")

    if is_win(user, computer):
        print("pkayer wins!🎉🎉🎉")
    elif is_lose(user, computer):
        print('computer wins!🤖🤖🤖')

    ask = input("do you want to play again? (y/n): ").lower()
    if ask != 'y':
        break

    
        




