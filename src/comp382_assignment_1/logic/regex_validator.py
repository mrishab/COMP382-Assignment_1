from comp382_assignment_1.common.symbols import Symbols

def validate_regex(regex):
    if not regex:
        return True
    
    # Simple parentheses balance check
    stack = []
    
    # Track if we're inside a star or other operator context
    for i, char in enumerate(regex):
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    
    if len(stack) != 0:
        return False
    
    # Check for implicit concatenation without operators
    # We need to ensure that where concatenation happens, it uses the ◦ operator
    
    valid_symbols = {Symbols.A, Symbols.B, Symbols.EPSILON, Symbols.EMPTY_SET}
    
    regex_no_spaces = regex.replace(Symbols.SPACE, Symbols.EMPTY_STRING)
    
    for i in range(len(regex_no_spaces) - 1):
        current = regex_no_spaces[i]
        next_char = regex_no_spaces[i + 1]
        
        # Cases where concatenation should be explicit:
        # 1. Two basic symbols next to each other: A followed by A, B, A, etc.
        if current in valid_symbols and next_char in valid_symbols:
            return False
        
        # 2. Symbol followed by '('
        if current in valid_symbols and next_char == Symbols.LEFT_PARENTHESIS:
            return False
        
        # 3. ')' followed by a symbol
        if current == Symbols.RIGHT_PARENTHESIS and next_char in valid_symbols:
            return False
        
        # 4. ')' followed by '('
        if current == Symbols.RIGHT_PARENTHESIS and next_char == Symbols.LEFT_PARENTHESIS:
            return False
        
        # 5. Star followed by anything that needs concatenation
        if current == Symbols.STAR:
            if next_char in valid_symbols or next_char == Symbols.LEFT_PARENTHESIS:
                return False
    
    return True