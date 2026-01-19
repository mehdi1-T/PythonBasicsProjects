from module import generate_symbols
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

while True:
    print(f"{Fore.GREEN}\n      SLOTH MACHINE")

    user_name = input("Enter your name: ").strip()
    carts = int(input("Enter how much money you want to play with: "))

    if carts < 100:
        print(f"{Fore.RED}Invalid carts (minimum is 100)")
        break

    print("LET'S GET STARTED!")

    spin = input("Do you want to spin the slot machine (yes/no): ").lower().strip()

    if spin == "yes":
        generate_symbols(carts, user_name)

    elif spin in ("no", "q"):
        print(f"{Fore.GREEN}Goodbye!")
        break

    else:
        print(f"{Fore.RED}Invalid input, please try again")
