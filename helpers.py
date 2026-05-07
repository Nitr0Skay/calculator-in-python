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