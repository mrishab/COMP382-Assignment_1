from enum import Enum

class Symbols(str, Enum):
    UNION = '∪'
    CONCATENATION = '◦'
    STAR = '*'
    EPSILON = 'ε'
    EMPTY_SET = '∅'
    LEFT_PARENTHESIS = '('
    RIGHT_PARENTHESIS = ')'
    A = 'a'
    B = 'b'
    EMPTY_STRING = ''
    SPACE = ' '
    SUBSCRIPT_ONE = '₁'
    SUBSCRIPT_TWO = '₂'
    SIGMA = 'Σ'

    def __str__(self):
        return self.value
