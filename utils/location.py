class Position:

    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

    def copy(self):
        return Position(self.line, self.column)

    def __repr__(self):
        return f"Position(line={self.line}, column={self.column})"

    def __add__(self, other):
        if isinstance(other, Position):
            return Position(self.line + other.line, self.column + other.column)
        else:
            raise TypeError(f"Cannot add Position and {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Position):
            return Position(self.line - other.line, self.column - other.column)
        else:
            raise TypeError(f"Cannot subtract Position and {type(other)}")
