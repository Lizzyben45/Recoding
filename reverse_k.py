def reverse_first(queue, k):
    if not queue or k <= 0:
        return queue
    if k > len(queue):
        k = len(queue)

    reversed_queue = []

    for char in range(k -1, -1, -1):
        reversed_queue.append(queue[char])

    for remaining_index in range(k, len(queue)):
        reversed_queue.append(queue[remaining_index])   

    return reversed_queue 

print(reverse_first([10, 20, 30, 40, 50], k= 3)) 
print(reverse_first([1, 2, 3, 4], k= 2))       