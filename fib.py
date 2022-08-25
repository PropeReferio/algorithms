# Return the nth fibonacci number
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
cache = {0: 0, 1: 1}


def fib(n):
    if n in cache:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)
    return cache[n]


print(fib(100))
