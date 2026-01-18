import colorama

colorama.init(autoreset=True)

print(f"{colorama.Fore.YELLOW}Which area do you calculate? (circle/square/triangle):{colorama.Style.RESET_ALL} ")

def Calculate_area():
    while True:
        user = input("Enter (c/s/r): ")

        if user.lower() == 'c':
            raduis = float(input("Enter the raduis of the circule: "))
            area = 3.14 * raduis ** 2 
            print(f"the area of the circle is {area}")
        
        elif user.lower() == 's':
            side = float(input("Enter the side length of the square: "))
            area = side ** 2
            print(f"The area of the square is {area}")

        elif user.lower() == 'r':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = 0.5 * base * height
            print(f"the area of the triangle is {area}")


        continue_calculation = input("Do you want to calculate another area? (yes/no): ")
        if continue_calculation.lower() != 'yes':
            print("Thank you for using the area calculator!")
            break

if __name__ == "__main__":
    Calculate_area()