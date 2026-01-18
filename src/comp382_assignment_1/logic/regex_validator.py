def validate_regex(regex):
    if not regex:
        return True # Or False depending on preference, but usually empty is okay, not sure yet honestly, will check with Yahya
    
    # Simple parentheses balance check
    stack = []
    for char in regex:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0