class Lexer:

    def __init__(self, input: str):
        self.input = str
        self.position = 0
        self.read_position = 0
        self.ch = 0

    def read_char(self):
        if self.read_position >= len(input):
            self.ch = 0
        else:
            self.ch = input[self.read_position]
        self.position = self.read_position
        self.read_position += 1
