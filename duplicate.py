def has_duplicates(numbers):
    lizzy = set()
    for num in numbers:
        if num in lizzy:
            return True
        lizzy.add(num)
    return False

print(has_duplicates([1, 2, 3, 2]))  
print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([]))
