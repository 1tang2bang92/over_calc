from typing import List, Union
from enum import Enum 

class TokenType(Enum):
    NUMBER = 1
    OPERATOR = 2
    LPAREN = 3
    RPAREN = 4
    EOF = 5
    
    
class Token:
    token_type: TokenType
    value: Union[str, float]
    
    def __init__(self, token_type: TokenType, value: Union[str, float]) -> None:
        self.token_type = token_type
        self.value = value
    
    def __repr__(self) -> str:
        return f'Token({self.token_type.name}, {self.value})'
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Token):
            return False
        
        return self.token_type == __value.token_type and self.value == __value.value

class Tokezier:
    tokens: List[Token] = []

    def __init__(self, input_string: str) -> None:
        self.tokens: List[Token] = []
        current_token: str = ''

        for char in input_string:
            if char.isdigit() or char == '.':
                current_token += char
            else:
                if current_token: 
                    self.tokens.append(Token(TokenType.NUMBER, float(current_token)))
                    current_token = ''
                if char == '+': 
                    self.tokens.append(Token(TokenType.OPERATOR, '+'))
                elif char == '-': 
                    self.tokens.append(Token(TokenType.OPERATOR, '-'))
                elif char == '*': 
                    self.tokens.append(Token(TokenType.OPERATOR, '*'))
                elif char == '/': 
                    self.tokens.append(Token(TokenType.OPERATOR, '/'))
                elif char == '(': 
                    self.tokens.append(Token(TokenType.LPAREN, '('))
                elif char == ')': 
                    self.tokens.append(Token(TokenType.RPAREN, ')'))
        
        if current_token: 
            self.tokens.append(Token(TokenType.NUMBER, float(current_token)))
        
        self.tokens.append(Token(TokenType.EOF, ''))
        
        pass

    def __repr__(self) -> str:
        return f'{self.tokens}'
    
    def __eq__(self, __value: List[Token]) -> bool:
        if not isinstance(__value, list):
            return False
        if len(self.tokens) != len(__value):
            return False
        
        for self_token, value_token in zip(self.tokens, __value):
            if self_token != value_token: 
                return False
        
        return True
