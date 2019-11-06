# Bracket Balancing

# Test Cases
test1 = "[{{[(}}{})]]"
test2 = "[({})]"
test3 = "[[[(()]]]"
test4 = "[[[["
test5 = "][][][]"
test6 = "]"

def brackets(equation):
    """
    Check to see if brackets are balanced in a string
    
    Input
    equation - String

    Output
    Balanced if brackets are balanced
    Unbalanced if brackets are not balanced
    """
    opening = ["[", "(", "{"]
    closing = ["]", ")", "}"]
    stack = []

    for i in equation:

        # If Brackets are opening
        # Add them to stack
        if i in opening:
            stack.append(str(opening.index(i)))
        
        # If Brackets are closing
        # Check to see if corresponding open bracket exists
        # If yes, continue, 
        # Else return Unbalanced
        if i in closing:
            if len(stack) >= 1:
                if i == closing[0]:
                    if '0' in stack:
                        stack.pop(stack.index('0'))
                    else:
                        return 'Unbalanced'
                if i == closing[1]:
                    if '1' in stack:
                        stack.pop(stack.index('1'))
                    else:
                        return 'Unbalanced'
                if i == closing[2]:
                    if '2' in stack:
                        stack.pop(stack.index('2'))
                    else:
                        return 'Unbalanced'
            else:
                return 'Unbalanced'

    # Return Conditions
    if len(stack) == 0:
        return 'Balanced'
    else:
        return 'Unbalanced'


check = brackets(test6)
print(check)
