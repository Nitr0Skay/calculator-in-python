import csv

def get_number(prompt):
    """Accept only numbers entered by the user. If user enter some text, this function will try ask for the number again"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            continue

def get_operator(prompt):
    """Accepted operators: + - * ** / : %"""
    while True:
        operator = input(prompt)
        if operator in ['+', '-', '*', '/', ':', '%', '**']:
            return operator


def get_file_extension(prompt):
    """Accept only the file extension entered by the user (txt or csv"""
    while True:
        extension = input(prompt)
        if extension.endswith("txt") or extension.endswith("csv"):
            return extension

def get_file_name(prompt):
    """Accept the name of the user choice. If user wont enter any text, it will return the default file name"""
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

def write_to_file(math_operation):
    file_extension = get_file_extension("Pick your file extension (.txt or .csv): ")
    file_name = get_file_name("You can type here the file name where you want to store this result or left it blank for default file name: ")
    save_operation(math_operation, file_name, file_extension)