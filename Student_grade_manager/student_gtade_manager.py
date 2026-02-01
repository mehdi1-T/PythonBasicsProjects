import time
import colorama
from colorama import Fore, Style
import subprocess

colorama.init(autoreset=True)

students = {}

def add_student():
    print(Fore.CYAN + "\n➕ Add New Student")
    name = input(Fore.YELLOW + "Enter student's name: ")
    grade = float(input(Fore.YELLOW + "Enter student's grade: "))
    students[name] = grade
    print(Fore.GREEN + "✔ Student added successfully!")

def show_student():
    print(Fore.CYAN + "\n📋 Students List")
    if not students:
        print(Fore.RED + "No students found.")
    else:
        for name, grade in students.items():
            print(Fore.WHITE + f"- {name}: {Fore.GREEN}{grade}")

def show_top_student():
    if not students:
        print(Fore.RED + "No students found.")
    else:
        top = max(students, key=students.get)
        print(Fore.MAGENTA + f"🏆 Top student: {top} ({students[top]})")

def show_average_grade():
    if not students:
        print(Fore.RED + "No students found.")
    else:
        avg = sum(students.values()) / len(students)
        print(Fore.BLUE + f"📊 Average grade: {avg:.2f}")

while True:
    print(Fore.WHITE + "\n=====================================")
    print(Fore.YELLOW + "🎓 STUDENT GRADE MANAGER")
    print(Fore.WHITE + "=====================================")
    print(Fore.CYAN + "1️⃣ Add a new student")
    print(Fore.CYAN + "2️⃣ Show all students")
    print(Fore.CYAN + "3️⃣ Show average grade")
    print(Fore.CYAN + "4️⃣ Show top student")
    print(Fore.RED + "5️⃣ Exit")
    print(Fore.WHITE + "=====================================")

    try:
        user = int(input(Fore.YELLOW + "Select an option: "))
    except ValueError:
        print(Fore.RED + "Invalide Input Please enter a number!")
        continue

    if user == 5:
        print(Fore.GREEN + "👋 Goodbye!")
        break
    elif user == 1:
        add_student()
    elif user == 2:
        show_student()
    elif user == 3:
        show_average_grade()
    elif user == 4:
        show_top_student()
    else:
        print(Fore.RED + "Invalid option!")
        
    subprocess.Popen("clear.bat", shell=True)
    print("Python is still running!")

    time.sleep(1)


