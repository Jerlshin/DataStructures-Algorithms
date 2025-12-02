import sys
from typing import Optional

def gcd_binary(a: int, b: int) -> int:
    """
    Calculates the Greatest Common Divisor (GCD) using Stein's Binary GCD Algorithm.
    (Converted from the provided Java implementation logic).

    The function is non-recursive and uses bitwise operations for efficiency.
    """
    # Ensure inputs are non-negative for GCD calculation
    a = abs(a)
    b = abs(b)

    # Base cases
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a

    # 1. Extract common factors of 2 (k counts the number of times both were even)
    k = 0
    # While both a and b are even (a & 1 == 0 and b & 1 == 0)
    while (a & 1) == 0 and (b & 1) == 0:
        a >>= 1  # a = a / 2
        b >>= 1  # b = b / 2
        k += 1

    # 2. Reduce a until it is odd
    while (a & 1) == 0:
        a >>= 1

    # 3. Main loop: Use subtraction and division by 2
    while b != 0:
        # Reduce b until it is odd
        while (b & 1) == 0:
            b >>= 1
        
        # Now both a and b are odd. Replace the larger with |a - b| / 2
        if a > b:
            # a = (a - b) / 2
            a = (a - b) >> 1
        else:
            # b = (b - a) / 2
            b = (b - a) >> 1

    # 4. Final GCD is a * 2^k
    return a << k

def lcm(a: int, b: int) -> int:
    """
    Calculates the Least Common Multiple (LCM) of two integers a and b
    using the relationship: LCM(a, b) = (|a * b|) / GCD(a, b).

    Uses the gcd_binary function to find the GCD.
    """
    if a == 0 or b == 0:
        return 0

    # Calculate GCD
    g = gcd_binary(a, b)

    # The formula ensures the result is always positive and avoids float operations
    # It also prioritizes division before multiplication to prevent intermediate overflow
    # if a and b are very large.
    return abs(a * (b // g))

# --- Main Execution Block ---

if __name__ == '__main__':
    # Read two integers from standard input, similar to Java Scanner behavior
    try:
        # Prompt user to enter two space-separated integers
        a, b = map(int, input().split())

        # Calculate and print the LCM
        print(lcm(a, b))

    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
    except EOFError:
        pass