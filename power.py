def my_pow(x: float, n: int) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n < 0:
        return my_pow(1/x, abs(n))
    half_pow = n // 2
    if n % 2 == 1:
        return my_pow(x, half_pow) * my_pow(x, half_pow) * x
    else:
        return my_pow(x, half_pow) * my_pow(x, half_pow)


print(my_pow(2, -2))