import random
from messages import wrong_operator_messages

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Division by Zero")

    return n1 / n2

def modulo(n1, n2):
    return n1 % n2

repeat = True
print("Welcome to my Calculator")

while repeat:
    number1 = float(input("Enter your first number: "))
    operator = input("Pick your operator: ")
    number2 = float(input("Enter your second Number: "))
    result = None

    match operator:
        case "+":
            result = add(number1, number2)
        case "-":
            result = subtract(number1, number2)
        case "*":
            result = multiply(number1, number2)
        case "/" | ":":
            result = divide(number1, number2)
        case "%":
            result = modulo(number1, number2)
        case _:
            print(random.choice(wrong_operator_messages))

    if(result is not None):
        print(f"Your result is {result}")
    else:
        print("Wasted")

    shall_we_continue = input("Shall we continue? (y/n): ")
    if shall_we_continue.lower() in ("y", "ye", "yes"):
        print("Ah shit, here we go again...")
    else:
        print("Respect +")
        repeat = False