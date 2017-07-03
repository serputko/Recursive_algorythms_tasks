def power_of_2(number):
    if number % 2 == 0:
        return 'YES'
    else:
        return 'NO'
    return power_of_2(number/2)

print(power_of_2(8))
