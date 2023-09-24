from typing import List, Optional

from calc.tokenizer import Token, TokenType

class BaseAst:
    '''
    공통 Ast 노드
    Tree Node의 기본 타입
    
        BaseAST
        /    \
    BaseAST BaseAST
    
    '''
    pass

class BinaryAst(BaseAst):
    '''
    이항 연산자 노드
    '''
    lhs: BaseAst
    rhs: BaseAst
    operator: str
    
    def __init__(self, lhs: BaseAst, operator: str, rhs: BaseAst) -> None:
        self.lhs = lhs
        self.operator = operator
        self.rhs = rhs
    
    def __repr__(self) -> str:
        return f'Binary({self.lhs}, {self.operator}, {self.rhs})'
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, BinaryAst):
            return False
        
        if self.lhs != __value.lhs:
            return False
        
        if self.operator != __value.operator:
            return False
        
        if self.rhs != __value.rhs:
            return False
        
        return True

class UnaryAst(BaseAst):
    '''
    단항 연산자 노드
    '''
    operator: str
    rhs: BaseAst
    
    def __init__(self, operator: str, rhs: BaseAst) -> None:
        self.operator = operator
        self.rhs = rhs
    
    def __repr__(self) -> str:
        return f'Unary({self.operator}, {self.rhs})'
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, UnaryAst):
            return False
        
        if self.operator != __value.operator:
            return False
        
        if self.rhs != __value.rhs:
            return False
        
        return True

class ConstAst(BaseAst):
    '''
    상수 노드
    '''
    value: float
    
    def __init__(self, value: float) -> None:
        self.value = value
    
    def __repr__(self) -> str:
        return f'Const({self.value})'
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, ConstAst):
            return False
        
        return self.value == __value.value

class Paser():
    '''
    token들을 ast로 변환해주는 class
    '''
    __tokens: List[Token] = []
    __current_token = 0

    def __init__(self, tokens: List[Token]) -> None:
        self.__tokens = tokens
    
    def consume_token(self):
        self.__current_token += 1
    
    def get_token(self) -> Optional[Token]:
        if self.__tokens[self.__current_token] == TokenType.EOF :
            return None
        
        return self.__tokens[self.__current_token]
    
    def parse_factor(self) -> BaseAst: #factor 인자
        token = self.get_token()
        
        if token is None:
            return None
                
        if token.token_type == TokenType.NUMBER:
            self.consume_token()
            return ConstAst(token.value)
        elif token.token_type == TokenType.LPAREN:
            self.consume_token()
            ast = self.parse_express()
            token = self.get_token()
                        
            if token.token_type != TokenType.RPAREN:
                # 에러
                pass
            
            self.consume_token()
            return ast
        
        elif token.value == '-':
            self.consume_token()
            ast = self.parse_factor()
            return UnaryAst('-', ast)
        
        # 여기까지 if문 안들어갔으면 오류
        return ConstAst(0)
    
    def parse_term(self) -> BaseAst: #term 항
        lhs = self.parse_factor()
        
        token = self.get_token()
        
        if token is None:
            return lhs
        
        if token.value == '*':
            self.consume_token()
            rhs = self.parse_term()
            return BinaryAst(lhs, '*', rhs)
        elif token.value == '/':
            self.consume_token()
            rhs = self.parse_term()
            return BinaryAst(lhs, '/', rhs)
        else:
            return lhs
        
        
    
    def parse_express(self) -> BaseAst:
        lhs = self.parse_term()
        
        token = self.get_token()
        
        if token is None:
            return lhs
        
        if token.value == '+':
            self.consume_token()
            rhs = self.parse_express()
            return BinaryAst(lhs, '+', rhs)
        elif token.value == '-':
            self.consume_token()
            rhs = self.parse_express()
            return BinaryAst(lhs, '-', rhs)
        else:
            return lhs

    def run(self):
        self.__current_token = 0
        return 