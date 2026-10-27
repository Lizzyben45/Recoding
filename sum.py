def list_sum(numbers):     
    if numbers == []:     
        return 0      
    
    lizzy = 0     
    for number in numbers:         
        lizzy += number     
        
    return lizzy    

print(list_sum([2, 4, 6, 8]))
