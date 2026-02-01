tasks = []


def addtask():
    task = input("Enter your task: ")
    tasks.append(task)
    print("your task added sucesseful")

def deletetask():
    task = input("Enter your task to delete it: ")
    if task in tasks:
        tasks.remove(task)
        print("your task deleted sucessful")
    else:
        print("invalide input")

def viewtasks():
    print(f"here's your tasks : {tasks}")



while True:
    print("========= TO DO LIST APPLICATION ===========")
    print("1. add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Quit")

    select = input("Enter your choice: ")

    if select == "1":
        addtask()

    elif select == "2":
        deletetask()

    elif select == "3":
        viewtasks()

    elif select == "4":
        exit()
    else:
        print("invalide input, please try again.")