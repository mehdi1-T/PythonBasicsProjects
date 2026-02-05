import bubble_sort  
import selection_sort
import binary_sort


LIST = input("Enter list of numbers separed by spaces: ").split()
LIST = [int(x) for x in LIST]

print("1. Bubble sort Algorithm")
print("2. binary Sort Algorithm")
print("3. Selection Sort Algorithm")
selected_algorithm =  int(input("What is the sorting Algorithm that you want to apply"))

if selected_algorithm == 1:
    pass
elif selected_algorithm == 2:
    pass
elif selected_algorithm == 3:
    pass
else:
    print("Invalid Inputs")