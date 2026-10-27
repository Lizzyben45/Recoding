def find_largest(numbers):
    if not numbers:
        return None
        
    largest = numbers[0]
    
    for number in numbers:
        if number > largest:
            largest = number
            
    return largest

find_number = [3, 41, 56, 21, 76, 9]
largest = find_largest(find_number)
print(largest)