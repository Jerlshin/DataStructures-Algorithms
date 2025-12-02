import math

def calc_fib(n):
    if n <= 1:
        return n
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    fib_n = (phi**n - psi**n) / math.sqrt(5)
    return round(fib_n)

n = int(input())
print(calc_fib(n))