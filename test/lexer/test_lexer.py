from __future__ import annotations

from src.lexer.lexer import Lexer
from src.my_token.my_token import TokenType

import logging


def test_next_token():
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
        assert token.literal == value[1]
        assert token.type.value == value[0].value
