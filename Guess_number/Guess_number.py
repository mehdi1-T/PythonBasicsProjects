import random
import colorama
from colorama import Fore, Style

#init colorama
colorama.init(autoreset=True)

def guess_number_game():
    while True:
        #generate a random number between 1 and 100
        number_to_guess = random.randint(1, 100)
        attempts = 0

        print(Fore.CYAN + "Guess The Number Game!")

        while True:
            
            try:
                guess = int(input("Your guess: "))
            except ValueError:
                print(Fore.YELLOW + "Please enter a valid number!")
                continue

            attempts += 1

            if guess < number_to_guess:
                print(Fore.RED + "Too low!")
            elif guess > number_to_guess:
                print(Fore.RED + "Too high!")
            else:
                print(
                    Fore.GREEN
                    + f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts."
                )
                break

        #check if the player wants to play again
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing 👋")
            break


if __name__ == "__main__":
    guess_number_game()
