# this project convert numbers from base to another.

print("Base Converter.")
print("1. Base 2 (Binary)")
print("2. Base 8 (Octal)")
print("3. Base 16 (Hexa decimal)")
print("4. Exit")

while True:
    try:    
        select = int(input("Please select wich destinarion you to convert to: "))
        user_number = int(input("Enter an integer number: "))
    except ValueError:
        print("Invalude value please enter integer value (decimal).")

    if select == 1:
        output = bin(user_number)
    elif select == 2:
        output = oct(user_number)
    elif select == 3:
        output = hex(user_number)
    elif select == 4:
        break
    else:
        output = "Invalude Input"

    print(f"Here's your number in base 2: {output}")