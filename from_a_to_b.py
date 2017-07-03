def from_a_to_b(a, b):
    if a <= b:
        if a == b:
            return str(b)
        return str(a) + ' ' + from_a_to_b(a+1, b)
    if a > b:
        if a == b:
            return str(b)
        return str(a) + ' ' + from_a_to_b(a - 1, b)

print(from_a_to_b(10, 3))
