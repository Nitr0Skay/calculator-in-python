def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            continue

def get_operator(prompt):
    while True:
        operator = input(prompt)
        if operator in ['+', '-', '*', '/', ':', '%', '**']:
            return operator