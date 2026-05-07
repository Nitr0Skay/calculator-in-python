from helpers import *

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
        return n1 ** n2

    def add_to_history(self, operation):
        self.history.append(operation)

    def save_history(self):
        write_to_file(self.history)