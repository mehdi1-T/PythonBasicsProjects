from module import generate_symbols
import random



while True:
    print('')
    print("")
    print("YOU ARE WELCOME IN SLOTH MACHINE")
    user_name = input("Enter your name : ")
    carts = int(input("Enter HOw much money do you want to play with : "))
    if carts >= 100:
        print("YOHHOOO, LET'S GET STARTED") 
    else:
        print('invalide carts') 
        exit()

    spine = input("Do you want spine the sloth machine(yes/not) : ").lower().strip()

    if spine == 'yes':
        generate_symbols(carts,user_name)
        print(generate_symbols(carts))
        


    elif spine == "not" or spine == ('Q').lower().split():
        break
    else:
        print("Invalide inputs")
        print("Please Try again")
    continue
