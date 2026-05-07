from decimal import Decimal
from calculator import Calculator
from helpers import *
from dispatcher import *

def main():
    calc = Calculator()
    repeat = True
    print("Welcome to my Calculator")
    math_operation = ""
    step = 0
    result = 0

    while repeat:
        step += 1

        if step == 1:
            result = Decimal(str(get_number("Enter your number: ")))
            op = get_operator("Pick your operator: ")
            number = Decimal(str(get_number("Enter next number: ")))
        else:
            op = get_operator("Pick your operator: ")
            number = Decimal(str(get_number("Enter next number: ")))

        old_result = result
        result = operation[op](result, number)

        math_operation = f"{old_result} {op} {number} = {result}"
        calc.history.append(math_operation)

        print(math_operation)

        shall_we_continue = input("Shall we continue? (y/n): ")
        if shall_we_continue.strip().lower() in ("y", "ye", "yes"):
            same_result = input("Do you want to continue on your result or start new calculation ? (y/n): ")
            if same_result.strip().lower() in ("y", "ye", "yes"):
                print(f"Your last operation was: {math_operation}")
            else:
                step = 0
                result = 0

        else:
            print("oh")
            repeat = False

if __name__ == "__main__":
    main()