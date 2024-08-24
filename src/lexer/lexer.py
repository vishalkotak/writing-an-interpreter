import logging

from my_token.my_token import Token, TokenType


class Lexer:

    def __init__(self, input_string: str):
        self.input_string = input_string
        self.position = 0
        self.read_position = 0
        self.ch = 0

    def read_char(self) -> None:
        if self.read_position >= len(self.input_string):
            self.ch = 0
        else:
            self.ch = self.input_string[self.read_position]
        self.position = self.read_position
        self.read_position += 1

    def next_token(self) -> Token:
        mapping = {
            "=": TokenType.ASSIGN,
            ";": TokenType.SEMICOLON,
            "(": TokenType.LPAREN,
            ")": TokenType.RPAREN,
            ",": TokenType.COMMA,
            "+": TokenType.PLUS,
            "{": TokenType.LBRACE,
            "}": TokenType.RBRACE,
        }
        self.read_char()
        if self.ch == 0:
            return Token(TokenType.EOF, "")
        if self.ch in mapping:
            return Token(mapping[self.ch], self.ch)


def main():
    input_string = "=+(){},;"
    expected_output = [
        (TokenType.ASSIGN, "="),
        (TokenType.PLUS, "+"),
        (TokenType.LPAREN, "("),
        (TokenType.RPAREN, ")"),
        (TokenType.LBRACE, "{"),
        (TokenType.RBRACE, "}"),
        (TokenType.COMMA, ","),
        (TokenType.SEMICOLON, ";"),
        (TokenType.EOF, ""),
    ]
    lexer = Lexer(input_string)
    for _, value in enumerate(expected_output):
        token = lexer.next_token()
        print(f"{token.type} {value[0]}")
        print(f"{token.literal} {value[1]}")


if __name__ == "__main__":
    main()
