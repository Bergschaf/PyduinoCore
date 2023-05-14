from typing import Optional
from tokenType import TokenType


class Token:
    """
    Token class, is instantiated in the lexer
    """

    def __init__(self, type: int, value: Optional[str] = None):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}{' ,' + self.value if self.value else ''})"


SINGLE_CHAR_TOKENS = {
    '(': TokenType.LEFT_PAREN,
    ')': TokenType.RIGHT_PAREN,
    '{': TokenType.LEFT_BRACE,
    '}': TokenType.RIGHT_BRACE,
    '[': TokenType.LEFT_BRACKET,
    ']': TokenType.RIGHT_BRACKET,
    ',': TokenType.COMMA,
    '.': TokenType.DOT,
    '-': TokenType.MINUS,
    '+': TokenType.PLUS,
    '/': TokenType.SLASH,
    '*': TokenType.STAR,
    '!': TokenType.BANG,
    '=': TokenType.EQUAL,
    '>': TokenType.GREATER,
    '<': TokenType.LESS
}

DOUBLE_CHAR_TOKENS = {
    '!=': TokenType.BANG_EQUAL,
    '==': TokenType.EQUAL_EQUAL,
    '>=': TokenType.GREATER_EQUAL,
    '<=': TokenType.LESS_EQUAL
}

KEYWORDS = {
    'and': TokenType.AND,
    'def': TokenType.DEF,
    'else': TokenType.ELSE,
    'False': TokenType.FALSE,
    'for': TokenType.FOR,
    'if': TokenType.IF,
    'or': TokenType.OR,
    'return': TokenType.RETURN,
    'True': TokenType.TRUE,
    'while': TokenType.WHILE
}