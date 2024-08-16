class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError(f"The second number - {b}, must not be zero")
        return a / b

    def sign_change(self, a, b):
        if a != 0 and b != 0:
            return -a, -b
        else: 
            raise ValueError(f"The numbers - {a, b} must be different from 0")