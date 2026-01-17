def match(regex, string):
    
    regex = regex.replace(' ', '')
    
    # BASE CASES
    if regex == 'ε':
        return string == ''
    if regex == '∅':
        return False
    if regex == 'a':
        return string == 'a'
    if regex == 'b':
        return string == 'b'
    
    # Check for parentheses
    if regex.startswith('(') and regex.endswith(')'):
        return match(regex[1:-1], string)
    
   # UNION OPERATOR ∪
    depth = 0
    # Find the rightmost union at top level
    last_union_pos = -1
    for i, char in enumerate(regex):
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif char == '∪' and depth == 0:
            last_union_pos = i
    
    if last_union_pos != -1:
        left = regex[:last_union_pos]
        right = regex[last_union_pos+1:]
        return match(left, string) or match(right, string)
    
    # CONCATENATION OPERATOR ◦
    depth = 0
    last_concat_pos = -1
    for i, char in enumerate(regex):
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif char == '◦' and depth == 0:
            last_concat_pos = i
    
    if last_concat_pos != -1:
        left = regex[:last_concat_pos]
        right = regex[last_concat_pos+1:]
        # Try all splits
        for split_point in range(len(string) + 1):
            if match(left, string[:split_point]) and match(right, string[split_point:]):
                return True
        return False
    
    # STAR OPERATOR *
    if regex.endswith('*'):
        inner = regex[:-1]
        
        if string == '':
            return True
        
        for i in range(1, len(string) + 1):
            if match(inner, string[:i]) and match(regex, string[i:]):
                return True
        
        return False
    
    # If the regex wasn't recognized
    return False