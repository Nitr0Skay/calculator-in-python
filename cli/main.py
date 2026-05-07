from calculator import Calculator
from helpers import *
from dispatcher import *

def main():
    repeat = True
    calc = Calculator()
    print("Welcome to my Calculator")
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
        calc.add_to_history(math_operation)

        print(math_operation)
        write = input("Would you like to save that calculation in the file ? (y/n): ")
        if write.strip().lower() in ("y", "ye", "yes"):
            write_to_file(math_operation)

        shall_we_continue = input("Shall we continue? (y/n): ")
        if shall_we_continue.strip().lower() in ("y", "ye", "yes"):
            same_result = input("Do you want to continue on your result or start new calculation ? (y/n): ")
            if same_result.strip().lower() in ("y", "ye", "yes"):
                print(f"Your last operation was: {math_operation}")
            else:
                step = 0
                result = 0

        else:
            print("Thank you and have a nice day :)")
            calc.save_history()
            repeat = False

if __name__ == "__main__":
    main()