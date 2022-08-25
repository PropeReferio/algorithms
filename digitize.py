def digitize(num, base=10):
    final = []
    while num > 0:
        num, remainder = divmod(num, base)
        final.insert(0, remainder)
    return final

print(digitize(12345))
