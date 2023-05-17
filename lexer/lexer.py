from typing import List

from token import Token, SINGLE_CHAR_TOKENS, DOUBLE_CHAR_TOKENS, KEYWORD_TOKENS, TokenType


class Lexer:
    """
    Returns a list of tokens from the input string
    """

    def __init__(self, code: str):
        self.code = code
        self.tokens: List[List[Token]] = []  # List of tokens for each line

    def tokenize(self):
        """
        Tokenize the input code
        """
        self.tokens = []
        lines = self.code.split('\n')
        for line in lines:
            for i, char in line:
                if char in SINGLE_CHAR_TOKENS:
                    self.tokens.append(Token(SINGLE_CHAR_TOKENS[char]))
                elif i > 0 and line[i - 1] + char in DOUBLE_CHAR_TOKENS:
                    self.tokens.append(Token(DOUBLE_CHAR_TOKENS[line[i - 1] + char]))
                elif char == ' ':
                    continue
                elif char == '#':
                    break
                elif char.isalpha():
                    self.tokens.append(self._parse_identifier(line, i))
                elif char.isdigit():
                    self.tokens.append(self._parse_number(line, i))
                elif char == '"':
                    self.tokens.append(self._parse_string(line, i))
                else:
                    raise ValueError(f"Unexpected character '{char}' at line {line}")

    @staticmethod
    def _parse_identifier(line: str, i: int) -> Token:
        """
        Parse an identifier
        """
        start = i
        while i < len(line) and line[i].isalnum():
            i += 1
        return Token(KEYWORD_TOKENS.get(line[start:i], TokenType.IDENTIFIER), line[start:i])

    @staticmethod
    def _parse_number(line: str, i: int) -> Token:
        """
        Parse a number
        """
        start = i
        while i < len(line) and line[i].isdigit():
            i += 1
        if i < len(line) and line[i] == '.':
            i += 1
            while i < len(line) and line[i].isdigit():
                i += 1
            return Token(TokenType.FLOAT_NUMBER, line[start:i])
        return Token(TokenType.INT_NUMBER, line[start:i])

    @staticmethod
    def _parse_string(line: str, i: int) -> Token:
        """
        Parse a string
        """
        start = i
        i += 1
        while i < len(line) and line[i] != '"':
            i += 1
        return Token(TokenType.STRING, line[start:i])
