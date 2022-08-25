def digitize(num, base=10):
    final = []
    while num > 0:
        num, digit = divmod(num, base)
        final.insert(0, digit)
    return final

print(digitize(12345))