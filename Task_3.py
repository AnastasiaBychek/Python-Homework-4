numbers = [2, 2, 3, 4, 5, 5, 6]
d = list(set(numbers))
print(d)


def unique_numbers(numbers):
    unique = []
    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique

print(unique_numbers(numbers))