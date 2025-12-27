import math


def prime_factors(n):
    factors_list = []
    while (n % 2) == 0:
        n //= 2
        factors_list.append(2)

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        while (n % i) == 0:
            n //= i
            factors_list.append(i)
    if n > 2:
        factors_list.append(n)
    return sorted(factors_list)
