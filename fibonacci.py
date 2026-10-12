"""Fibonacci series (default: first 10 terms)."""


def fibonacci(n: int) -> list:
    """Return the first n terms of the Fibonacci series."""
    if n < 0:
        raise ValueError("Number of terms cannot be negative.")
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    terms = 10
    print(f"Fibonacci series of {terms} terms")
    print(" ".join(str(x) for x in fibonacci(terms)))
    print(f"Sum of the series is: {sum(fibonacci(terms))}")
