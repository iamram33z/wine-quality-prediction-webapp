"""
This is the main module of the project.
"""


def add_numbers(a, b):
    """Add two numbers."""
    return a + b


def subtract_numbers(a, b):
    """Subtract two numbers."""
    return a - b


if __name__ == "__main__":
    X = 5
    Y = 3
    print(f"Addition of {X} and {Y}: {add_numbers(X, Y)}")
    print(f"Subtraction of {X} and {Y}: {subtract_numbers(X, Y)}")
