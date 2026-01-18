import random

def generate_symbols(carts, user_name):
    imojis = ["🍒", "🍋", "🍊", "🍉", "🍇", "7️⃣", "⭐", "💎", "🔔", "🍀"]
    sym1 = random.choice(imojis)
    sym2 = random.choice(imojis)
    sym3 = random.choice(imojis)

    

    sloth_machine = [sym1,sym2,sym3]
    print(sloth_machine)

    if sym1 == sym2 == sym3:
        print(f"{user_name}, you hit the JACKPOT! 🎉")
        carts += carts
    elif (sym1 == sym2) or (sym1 == sym3) or (sym2 == sym3):
        print(f"{user_name}, you won a smaller prize! 🪙")
        carts += carts / 2
    else:
        print(f"{user_name}, you lose. 😢")
        carts -= carts / 2

    return carts