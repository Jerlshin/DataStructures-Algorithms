def gcd_binary(a: int, b: int) -> int:
    """
    Calculates the Greatest Common Divisor (GCD) using Stein's Binary GCD Algorithm.
    Time Complexity: O((log a)^2) or O((log b)^2).
    """
    if a == 0:
        return b
    if b == 0:
        return a

    # Find the largest power of 2 dividing both a and b (k = gcd(a, b) factor)
    k = 0
    while (a & 1) == 0 and (b & 1) == 0:
        a >>= 1
        b >>= 1
        k += 1

    # Reduce a until it is odd
    while (a & 1) == 0:
        a >>= 1

    # Main loop (at least one number is guaranteed to be odd)
    while b != 0:
        # Reduce b until it is odd
        while (b & 1) == 0:
            b >>= 1
        
        # Now both a and b are odd. Replace the larger with (larger - smaller) / 2
        if a > b:
            a = (a - b) >> 1
        else:
            b = (b - a) >> 1

    # Multiply back the common factors of 2 removed in the first step
    return a << k

if __name__ == '__main__':
    # Example usage reading input from a single line
    try:
        a, b = map(int, input("Enter two integers (a b): ").split())
        print(gcd_binary(a, b))
    except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")