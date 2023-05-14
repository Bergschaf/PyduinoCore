class TokenType:
    # Single-character tokens.
    LEFT_PAREN = 1
    RIGHT_PAREN = 2
    LEFT_BRACE = 3
    RIGHT_BRACE = 4
    LEFT_BRACKET = 5
    RIGHT_BRACKET = 6
    COMMA = 7
    DOT = 8
    MINUS = 9
    PLUS = 10
    SLASH = 11
    STAR = 12

    # One or two character tokens.
    BANG = 13
    BANG_EQUAL = 14
    EQUAL = 15
    EQUAL_EQUAL = 16
    GREATER = 17
    GREATER_EQUAL = 18
    LESS = 19
    LESS_EQUAL = 29

    # Literals.
    IDENTIFIER = 21
    STRING = 22
    INT_NUMBER = 23
    FLOAT_NUMBER = 24

    # Keywords.
    AND = 25
    DEF = 26
    ELIF = 27
    ELSE = 28
    FALSE = 29
    FOR = 30
    IF = 31
    OR = 32
    RETURN = 33
    TRUE = 34
    WHILE = 35

    INDENT = 36

    EOF = 37
