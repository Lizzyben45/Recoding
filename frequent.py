def most_frequent(numbers):
    if not numbers:
        return None

    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1

    return max(frequencies, key=frequencies.get)


print(most_frequent([2, 5, 2, 8, 2, 5]))
print(most_frequent([4, 7, 7, 4]))
print(most_frequent([]))