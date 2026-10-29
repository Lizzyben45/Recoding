def closest_number(numbers, target):
    closest = numbers[0]
    
    for number in numbers:
        current_distance = abs(number - target)
        closest_distance = abs(closest - target)
        
        if current_distance < closest_distance:
            closest = number
        elif current_distance == closest_distance:
            if number < closest:
                closest = number
                
    return closest

print(closest_number([4, 8, 15, 20], target = 13))
print(closest_number([8, 12], target = 10))
