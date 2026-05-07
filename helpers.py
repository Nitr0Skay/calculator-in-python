import csv
from decimal import Decimal

def get_number(prompt):
    """Accept only numbers entered by the user. If user enter some text, this function will try ask for the number again"""
    while True:
        try:
            return Decimal(input(prompt))
        except ValueError:
            continue

def get_operator(prompt):
    """Accepted operators: + - * ** / : %"""
    while True:
        operator = input(prompt)
        if operator in ['+', '-', '*', '/', ':', '%', '**']:
            return operator


def get_file_extension(prompt):
    """Accept only the file extension entered by the user (txt or csv)"""
    while True:
        extension = input(prompt)
        if extension.endswith("txt") or extension.endswith("csv"):
            return extension

def get_file_name(prompt):
    """Accept the name of the user choice. If user doesn't enter any text, it will return the default file name"""
    file_name = input(prompt)
    if len(file_name.strip()) == 0:
        file_name = "calculations"

    return file_name


def save_operation(operation, file_name, file_extension):
    """Save mathematical operation to file with provided name and extension"""
    full_file_name = f"{file_name}.{file_extension}"
    if file_extension == "txt":
        with open(full_file_name, "a") as file:
            file.write(f"{operation}\n")

    elif file_extension == "csv":
        operation, result = operation.split(" = ")
        n1, op, n2 = operation.split()
        with open(full_file_name, "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["number1", "operator", "number2", "result"], delimiter=";")

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({
                "number1": n1,
                "operator": op,
                "number2": n2,
                "result": result
            })

def write_to_file(math_operations):
    if isinstance(math_operations, str):
        math_operations = [math_operations]

    file_extension = get_file_extension("Pick your file extension (.txt or .csv): ")
    file_name = get_file_name("You can type here the file name where you want to store this result or left it blank for default file name: ")

    for operation in math_operations:
        save_operation(operation, file_name, file_extension)