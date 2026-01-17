from comp382_assignment_1.common.symbols import Symbols

def match(regex, string):

    regex = regex.replace(Symbols.SPACE, Symbols.EMPTY_STRING)

    # BASE CASES
    if regex == Symbols.EPSILON:
        return string == Symbols.EMPTY_STRING
    if regex == Symbols.EMPTY_SET:
        return False
    if regex == Symbols.A:
        return string == Symbols.A
    if regex == Symbols.B:
        return string == Symbols.B

    # Check for parentheses
    if regex.startswith(Symbols.LEFT_PARENTHESIS) and regex.endswith(Symbols.RIGHT_PARENTHESIS):
        # Check if it's (R)*
        if regex.endswith(Symbols.RIGHT_PARENTHESIS + Symbols.STAR):
            inner = regex[1:-2]
            return match(inner + Symbols.STAR, string)
        else:
            return match(regex[1:-1], string)

   # UNION OPERATOR ∪
    depth = 0
    # Find the rightmost union at top level
    last_union_pos = -1
    for i, char in enumerate(regex):
        if char == Symbols.LEFT_PARENTHESIS:
            depth += 1
        elif char == Symbols.RIGHT_PARENTHESIS:
            depth -= 1
        elif char == Symbols.UNION and depth == 0:
            last_union_pos = i

    if last_union_pos != -1:
        left = regex[:last_union_pos]
        right = regex[last_union_pos+1:]
        return match(left, string) or match(right, string)

    # CONCATENATION OPERATOR ◦
    depth = 0
    last_concat_pos = -1
    for i, char in enumerate(regex):
        if char == Symbols.LEFT_PARENTHESIS:
            depth += 1
        elif char == Symbols.RIGHT_PARENTHESIS:
            depth -= 1
        elif char == Symbols.CONCATENATION and depth == 0:
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
    if regex.endswith(Symbols.STAR):
        inner = regex[:-1]

        if string == Symbols.EMPTY_STRING:
            return True

        for i in range(1, len(string) + 1):
            if match(inner, string[:i]) and match(regex, string[i:]):
                return True

        return False

    # If the regex wasn't recognized
    return False
