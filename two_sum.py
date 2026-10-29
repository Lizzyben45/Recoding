def two_sum(numbers, target):
    seen = {}
    
    for index, num in enumerate(numbers):
        complement = target - num
        
        if complement in seen:
            return [seen[complement], index]
        
        seen[num] = index
        
    return None

print(two_sum([2, 7, 11, 15], target = 9)) 
print(two_sum([2, 7, 11, 15], target = 26))
print(two_sum([5, 1, 3], target = 3 ))    

