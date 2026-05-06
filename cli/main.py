from calculator import Calculator
from helpers import *
from dispatcher import *

def main():
    calc = Calculator()
    repeat = True
    print("Welcome to my Calculator")
    step = 0
    while repeat:
        step += 1
        number = get_number("Enter number: ")
        op = get_operator("Pick your operator: ")
        result = None

        if(result is not None):
            print(f"Your result is {result}")
        else:
            print("Wasted")

        shall_we_continue = input("Shall we continue? (y/n): ")
        if shall_we_continue.lower() in ("y", "ye", "yes"):
            print("ok")
        else:
            print("oh")
            repeat = False

if __name__ == "__main__":
    main()