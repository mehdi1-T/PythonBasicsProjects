try:
    target = int(input("Target: "))
except ValueError:
    print("Please enter an integer number")
    
even_number = [num for num in range(target) if num % 2 == 0]
print(even_number)

odd_number = [num  for num in range(target) if num % 2 != 0]
print(odd_number)
