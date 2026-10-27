def find_number(numbers, target):
    i = 0
    while i < len(numbers):
        if numbers[i] == target:
            return i
        i += 1
    return "-1"
print(find_number([10, 25, 30, 45], target = 10))
