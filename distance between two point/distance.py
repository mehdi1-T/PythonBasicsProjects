import math

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

while True:
    #  get point adress from the user
    try:
        point_1 = input("Point 1 (x, y) or exit: ")    
        if point_1 == "exit":
            print("Exition...")
            break
        point_2 = input("Point 2 (x, y): ")
    except TypeError:
        print("invlide Data Type.")

    # convert strings into tuples
    point_1 = tuple(int(x) for x in point_1.split(','))
    point_2 = tuple(int(x) for x in point_2.split(','))

    # calculate result
    result = distance(point_1, point_2)

    # show the user the result 
    print(result)