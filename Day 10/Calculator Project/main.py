from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

repeat = True
while repeat:
    print("\n" * 20)
    print(logo)
    first_number = int(input("Please enter a number: "))
    second_number = int(input("Please enter another number: "))
    operator = input("Please enter a operator: ")
    print(calculation[operator](first_number, second_number))

    repeat = input("Would you like to repeat? (y/n): ") == "y"
