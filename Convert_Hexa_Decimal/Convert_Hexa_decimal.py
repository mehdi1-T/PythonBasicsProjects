# this code converts hexadecimal numbers to decimal numbers
values = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
}

def convert_hexa_decimal(array):
    # convert hecadecimal to decimal number
    total = 0
    n = len(array)
    for i in range(n):
       number =  values[array[i].upper()]
       power = n - i - 1
       total += number * (16 ** power)
    return total

def get_hexa_number():
    # get hexadecimal from user
    hexa_number = input("HexaNumber: ")
    return hexa_number

def convert_number_list(number):
    # convert hexadecimal to string list
    numbers = [0] * len(number)
    for i in range(len(number)):
        numbers[i] = number[i]
    return numbers

def manage_functions():
    # 1) get number as string from user
    hexa_number = get_hexa_number()
    # 2) convert this string to list
    list_hexa_numbers = convert_number_list(hexa_number)
    # 3) convert this list to decimal using a dictionary
    decimal_value = convert_hexa_decimal(list_hexa_numbers)

    # print decimal value
    print(f"decimal : {decimal_value}")


if __name__ == "__main__":
    manage_functions()