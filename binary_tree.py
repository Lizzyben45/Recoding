class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst_iterative(root):
    stack = []
    current = root
    prev = None
         
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
                     
        current = stack.pop()
                 
        if prev is not None and current.value <= prev:
            return False
                     
        prev = current.value
        current = current.right
             
    return True

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.right.left = Node(4)

result = is_valid_bst_iterative(root)
print(result) 
