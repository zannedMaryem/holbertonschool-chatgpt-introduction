#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if len(sys.argv) < 2:
    print("Usage: ./script.py <number>")
else:
    print(factorial(int(sys.argv[1])))