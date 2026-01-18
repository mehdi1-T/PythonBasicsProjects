# Simple Calculator
# importing colorama for colored text output
import colorama
from colorama import Fore, Back, Style

def Calculator():
    while True:
        print(f"\n{Fore.GREEN}      Simple Calculator{Fore.RESET}\n")
        # getting numbers and operator from user
        first_number = int(input("Enter the first number : "))
        operator = input("Enter an operator : ")
        second_number = int(input("Enter the second number : "))

        match operator:
            case "+":
                result = first_number + second_number
            case "-":
                result = first_number - second_number
            case "*":
                result = first_number * second_number
            case "/" if second_number != 0:
                result = first_number / second_number       
            case _:
                print("invalide operator")
                continue    

        print(f"{Fore.YELLOW}result :{Fore.RESET} {result}")
        print("")

if __name__ == "__main__":
    colorama.init(autoreset=True)
    Calculator()