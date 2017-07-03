def print_number_inverse(n):
    if n < 10:
        return str(n)
    return str(n % 10) + print_number_inverse(int(n/10))

print(print_number_inverse(65432))
