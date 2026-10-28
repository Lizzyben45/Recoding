def second_largest(numbers):
    if len(numbers) < 2:
        return None

    largest = second_largest = numbers[0]

    has_second = False

    for number in numbers:
        if number > largest:
            second_largest = largest
            largest = number
            has_second = True
        elif number < largest:

            if not has_second or number > second_largest:
                second_largest = number
                has_second = True

    return second_largest if has_second else None
print(second_largest([10, 5, 8, 10, 3]))                
print(second_largest([4, 4, 4]))                
print(second_largest([-5, -2, -8, -3]))                
             