items = {
    "apple": 0.5,
    "banana": 0.3,
    "bread": 1.2,
    "milk": 0.9,
    "eggs": 2.5,
    "rice": 3.0,
    "chicken": 5.8,
    "cheese": 2.9,
    "tomato": 0.4,
    "water": 0.6
}

def add_product():
    item = input("Enter product name: ")
    cart["item"].append(item)
    cart["price"].append(item[])



def remove_product():
    pass

def total_products():
    pass

def most_expensive():
    pass

while True:
    print("Shoping cart system")
    print("1. Add producte")
    print("2. Remove producte")
    print("3. Total product")
    print("4. Most expensive item")
    print("5. Exit")

    user = int(input("Select one of the options: "))

    cart = {
        "item":[],
        "price":[]
    }

    if user == 1:
        add_product()
    elif user == 2:
        remove_product()
    elif user == 3:
        total_products()
    elif user == 4:
        most_expensive()
    elif user == 5:
        True

