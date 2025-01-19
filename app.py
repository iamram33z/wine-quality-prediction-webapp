"""
Sample application to demonstrate the usage of the Calculator class.
"""


class Calculator:
    """A simple calculator class."""

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


if __name__ == "__main__":
    calculator = Calculator()
    print(f"Multiplication of 6 and 4: {calculator.multiply(6, 4)}")
    print(f"Division of 10 by 2: {calculator.divide(10, 2)}")
