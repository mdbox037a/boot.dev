"""
return how many steps it takes to reduce a non-negative integer to 0 using these rules:
- If the number is even, divide it by 2.
- If the number is odd, subtract 1.
Use a recursive solution. The function should be a pure function (no printing or modifying outside state).
"""


def steps_to_zero(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return steps_to_zero(n // 2) + 1
    else:
        return steps_to_zero(n - 1) + 1
