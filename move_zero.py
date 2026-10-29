def move_zeros(numbers):
    result = []
    lizzy = 0
    for number in numbers:
        if number == 0:
            lizzy += 1
        else:
            result.append(number)

    result.extend([0] * lizzy)
    return result
    

print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))  
print(move_zeros([0, 0, 5]))                      



