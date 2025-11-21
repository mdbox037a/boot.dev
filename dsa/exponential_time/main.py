def fib(n):
    grandparent = 0
    parent = 1
    current = 1

    if n == 0:
        return 0

    i = n - 1
    while i > 0:
        current = parent + grandparent
        grandparent, parent = parent, current
        i -= 1
    return current
