class Calculator:
    def __init__(self):
        self.first_number = None
        self.operator = None
        self.second_number = None

    def get_operation(self):
        try: 
            self.first_number = int(input("Enter The first number: "))
            self.operator = input("Enter Your operator: ")
            self.second_number = int(input("Enter The secon number: "))
        except ValueError:
            print("Invalude Input try again please!")
            
    def calculate(self):
        if self.operator == "+":
            return self.first_number + self.second_number
        elif self.operator == "-":
            return self.first_number - self.second_number
        elif self.operator == "/":
            if self.second_number == 0:
                print("Invalude Input")
            else:
                return self.first_number / self.second_number
        elif self.operator == "x":
            return self.first_number * self.second_number
        elif self.operator == "pow":
            return pow(self.first_number, self.second_number)
        else:
            print("Invalid Operation")

        
calc = Calculator()

while True:
    print("Calculator")
    calc.get_operation()
    result = calc.calculate()
    print(f"Result {result}")
    print()