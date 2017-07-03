def print_all_digits(number):
    if number < 10:
        return number
    return number % 10 + print_all_digits(int(number / 10))

print(print_all_digits(124))