def valid_parentheses(text):
    matching_brackets = {')': '(', ']': '[', '}': '{' }
    stack = []

    for number in text:

        if number in matching_brackets.values():
            stack.append(number)
        elif number in matching_brackets:

            if not stack or stack[-1] != matching_brackets[number]:
                return False
            stack.pop()

    return len(stack) == 0
print(valid_parentheses("{[()]}")) 
print(valid_parentheses("([)]"))
print(valid_parentheses("((()))" ))
print(valid_parentheses("{[}"))

                                               