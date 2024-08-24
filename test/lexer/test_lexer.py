from __future__ import annotations

from src.lexer.lexer import Lexer
from src.my_token.my_token import TokenType

def test_next_token():
    input = "=+(){},;"
    expected_output = [
        ( TokenType.ASSIGN, "=" ),
        ( TokenType.PLUS, "+" ), 
        ( TokenType.LPAREN, "(" ), 
        ( TokenType.RPAREN, ")" ), 
        ( TokenType.LBRACE, "{" ), 
        ( TokenType.RBRACE, "}" ), 
        ( TokenType.COMMA, "," ), 
        ( TokenType.SEMICOLON, ";" ), 
        ( TokenType.EOF, "" ),
    ]
    lexer = Lexer(input)
    for _, value in enumerate(expected_output):
        token = lexer.next_token()
        assert token.type == value[0]
        assert token.literal == value[1]

