"""Factorial of a number (default: 5)."""


def factorial(n: int) -> int:
    """Return n! using an iterative approach."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    number = 5
    steps = " x ".join(str(i) for i in range(number, 0, -1))
    print(f"Calculating factorial of {number}")
    print(f"{number}! = {steps}")
    print(f"Factorial of {number} is: {factorial(number)}")
