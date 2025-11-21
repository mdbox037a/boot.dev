def fib(n):
    if n == 0:
        return n

    grandparent = 0
    parent = 1
    current = 1

    for i in range(0, n - 1):
        current = parent + grandparent
        grandparent, parent = parent, current
    return current
