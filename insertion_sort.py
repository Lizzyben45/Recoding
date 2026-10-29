def insertion_sort(numbers):
    shift_count = 0
    
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            shift_count += 1  
            j -= 1
            
        numbers[j + 1] = key
        
    return numbers, shift_count

print(insertion_sort([5, 3, 4]))  
print(insertion_sort([7, 5, 4, 6, 8]))  
