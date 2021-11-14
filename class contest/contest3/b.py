import math

def fib(n):
    a, b = 1, 2
    if n <= 2:
        return n
    for i in range(n-2):
        c = (a + b) % 1000000007
        a, b = b, c
    return c

print(fib(int(input()) ))