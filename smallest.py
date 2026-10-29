def find_smallest(numbers):
    if not numbers:
        return None
        
    smallest = numbers[0]
    
    for number in numbers:
        if number < smallest:
            smallest = number
            
    return smallest

find_number = [8, 3, 12, 1, 7]
smallest = find_smallest(find_number)
print(smallest)


