from colorama import Fore
import colorama

colorama.init(autoreset=True)

tasks = []

def addtask():
    task = input("Enter your task: ")
    tasks.append(task)
    print(Fore.GREEN+"your task added sucesseful")

def deletetask():
    task = input("Enter your task to delete it: ")
    if task in tasks:
        tasks.remove(task)
        print(Fore.GREEN+"your task deleted sucessful")
    else:
        print(Fore.RED+"invalide input")

def viewtasks():
    print()
    for i, task in enumerate(tasks, start=1):
        print(f"taks number {i} : {tasks}")

while True:
    print(Fore.YELLOW+"========= TO DO LIST CLI APPLICATION ===========")
    print("1. add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print(Fore.RED+"4. Quit")

    select = input("Enter your choice: ")

    if select == "1":
        addtask()

    elif select == "2":
        deletetask()

    elif select == "3":
        viewtasks()

    elif select == "4":
        print("Exiting...")
        exit()
    else:
        print(Fore.RED+"invalide input, please try again.")

    print()
    print()