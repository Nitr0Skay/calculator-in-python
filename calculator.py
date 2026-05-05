class Calculator:

    def __init__(self):
        self.history = []

    def add(self, n1, n2):
        return n1 + n2

    def subtract(self, n1, n2):
        return n1 - n2

    def multiply(self, n1, n2):
        return n1 * n2

    def divide(self, n1, n2):
        if n2 == 0:
            raise ZeroDivisionError
        return n1 / n2

    def modulo(self, n1, n2):
        return n1 % n2

    def exp(self, n1, n2):
        result = 0
        for _ in range(n2):
            result *= n1

        return result