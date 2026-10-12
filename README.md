# Fibonacci Series

A simple Python project that prints the Fibonacci series (default: first **10** terms).

## What is the Fibonacci series?
Each number is the sum of the two numbers before it, starting from 0 and 1.

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
```

## Project Structure
```
fibonacci_project/
├── fibonacci.py            # Python source code
├── README.md               # Project documentation
└── output_screenshot.png   # Screenshot of program output
```

## Requirements
- Python 3.6+

## How to Run
```bash
python fibonacci.py
```

## Output
```
Fibonacci series of 10 terms
0 1 1 2 3 5 8 13 21 34
Sum of the series is: 88
```

![Output Screenshot](output_screenshot.png)

## How It Works
The `fibonacci(n)` function starts with `a = 0` and `b = 1`, appends `a` to the list, then updates the pair to `(b, a + b)` on each loop. It raises a `ValueError` for negative input.

To print a different number of terms, change `terms = 10` in `fibonacci.py`.
