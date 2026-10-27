def reverse_list(items):
    reversed_items = []     

    aladi = len(items) -1
    while aladi >= 0:
        reversed_items = reversed_items + [items[aladi]]    
        aladi -= 1

    return reversed_items

target_number = [1, 2, 3, 4]
target_alphabet = ["a", "b", "c", "d"]

print(reverse_list(target_number))
print(reverse_list(target_alphabet))
