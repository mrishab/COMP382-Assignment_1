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
        # Check if it's (R)*
        if regex.endswith(')*'):
            inner = regex[1:-2]
            return match(inner + '*', string)
        else:
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


def main():
    print("=" * 50)
    print("REGEX MATCHER (Sipser Definition 1.52)")
    print("=" * 50)
    print("Alphabet: {a, b}")
    print("Symbols: ε ∅ ∪ ◦ * ( )")
    print("\nExamples:")
    print("  a* ∪ b*    - strings of all a's OR all b's")
    print("  (a ◦ b)    - exactly 'ab'")
    print("  (a ∪ b)*   - any string of a's and b's")
    print("=" * 50)
    
    # Get regex from user
    while True:
        regex = input("\nEnter regular expression: ").strip()
        
        # Validate characters
        valid_chars = set('abε∅∪◦*() ')
        if not all(c in valid_chars for c in regex):
            print("Error: Use only a, b, ε, ∅, ∪, ◦, *, (, )")
            continue
        break
    
    print(f"\nTesting: {regex}")
    print("Type 'exit' to quit, 'new' for new regex")
    print("-" * 50)
    
    while True:
        test_string = input("\nTest string: ").strip()
        
        if test_string.lower() == 'exit':
            print("Goodbye!")
            break
            
        if test_string.lower() == 'new':
            print("\n" + "=" * 50)
            main()
            break
        
        if not all(c in 'ab' for c in test_string):
            print("Error: String must contain only 'a' and 'b'")
            continue
        
        # Test the match
        result = match(regex, test_string)
        
        if result:
            print(f"✓ MATCH: '{test_string}' is in L({regex})")
        else:
            print(f"✗ NO MATCH: '{test_string}' is NOT in L({regex})")


if __name__ == "__main__":
    main()