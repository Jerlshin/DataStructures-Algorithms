import math
from typing import List
import sys

# def max_pairwise_product_naive(A: List[int]) -> int:
#     n = len(A)
#     if n < 2:
#         raise ValueError("List must contain at least two elements.")
#     max_product = -math.inf
    
#     for i in range(n):
#         for j in range(i+1, n):
#             current_product = A[i] * A[j]
#             if current_product > max_product:
#                 max_product = current_product
    
#     return int(max_product)

def max_pairwise_product_efficient(A: List[int]) -> int:
    """
    Handles negative numbers, as the maximum product can be the result of:
    1. Product of the two largest positive numbers.
    2. Product of the two smallest negative numbers.
    """
    
    n = len(A)
    if n < 2:
        raise ValueError("List must contain at least two elements.")
    
    # Initialize the two largest and two smallest values
    max1 = max2 = -math.inf  # largest two elements (max1 > max2)
    min1 = min2 = math.inf # smallest two elements (min1 < min2)
    
    for number in A:
        # Update the two largest values
        if number > max1:
            max2 = max1
            max1 = number
        elif number > max2:
            max2 = number
        
        # Update the two smallest values
        if number < min1:
            min2 = min1
            min1 = number
        elif number < min2:
            min2 = number
    
    return int(max(max1 * max2, min1 * min2))



# # Test cases:
# list1 = [6, 3, 9, 2, 8]  # Expected: 9 * 8 = 72
# list2 = [1, 5, -2, -4, 0] # Expected: 5 * 1 = 5, or (-2) * (-4) = 8. Max is 8.
# list3 = [-10, -5, -3, -1] # Expected: (-10) * (-5) = 50
# list4 = [10, 10]          # Expected: 10 * 10 = 100

# print(f"List: {list1}")
# print(f"Naive Result: {max_pairwise_product_naive(list1)}")
# print(f"Efficient Result: {max_pairwise_product_efficient(list1)}\n")

# print(f"List: {list2}")
# print(f"Naive Result: {max_pairwise_product_naive(list2)}")
# print(f"Efficient Result: {max_pairwise_product_efficient(list2)}\n")

# print(f"List: {list3}")
# print(f"Naive Result: {max_pairwise_product_naive(list3)}")
# print(f"Efficient Result: {max_pairwise_product_efficient(list3)}\n")

# print(f"List: {list4}")
# print(f"Efficient Result: {max_pairwise_product_efficient(list4)}\n")

if __name__ == "__main__":
    input_n = sys.stdin.readline()
    n = int(input_n)
    
    input_a = sys.stdin.readline()
    a = [int(x) for x in input_a.split()]
    
    print(max_pairwise_product_efficient(a))