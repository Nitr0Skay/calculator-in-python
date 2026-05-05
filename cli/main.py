from calculator import Calculator as calc

def main():
    repeat = True
    print("Welcome to my Calculator")
    step = 0
    while repeat:
        step += 1
        number = get_number("Enter number: ")
        operator = get_operator("Pick your operator: ")

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

if __name__ == "__main__":
    main()