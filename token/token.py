from enum import Enum

class TokenType(Enum):
    ILLEGAL = "ILLEGAL" # Signifies a token/character we don't know.
    EOF = "EOF" # End of file.

    # Identifiers
    IDENT = "IDENT"
    INT = "INT"

    # Operators
    ASSIGN = "="
    PLUS = "+"

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"
    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # Keywords
    FUNCTION = "FUNCTION"
    LET = "LET"


class Token:
    type: str # could have been an int/byte for better performance.
    literal: str

