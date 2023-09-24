from calc.tokenizer import Token, TokenType, Tokezier

def get_Token(s) -> Token:
    if float == type(s):
        return Token(TokenType.NUMBER, float(s))
    
    elif str == type(s):
        if s == '(':
            return Token(TokenType.LPAREN, '(')
        elif s == ')':
            return Token(TokenType.RPAREN, ')')
        else:
            return Token(TokenType.OPERATOR, s)
    
def test_simple_express():
    assert Token(TokenType.OPERATOR, '+') == Token(TokenType.OPERATOR, '+')

def test_simple_express2():
    result = Tokezier("13+2")

    assert result == [
        get_Token(13.),
        get_Token('+'),
        get_Token(2.),
        Token(TokenType.EOF, '')
    ]
    
def test_simple_express3():
    result = Tokezier("13+ 2 - 5")

    assert result == [
        get_Token(13.),
        get_Token('+'),
        get_Token(2.),
        get_Token('-'),
        get_Token(5.),
        Token(TokenType.EOF, '')
    ]

def test_complex_express():
    result = Tokezier('2 * (1 + 3) / 5')

    assert result == [
        get_Token(2.),
        get_Token('*'),
        get_Token('('),
        get_Token(1.),
        get_Token('+'),
        get_Token(3.),
        get_Token(')'),
        get_Token('/'),
        get_Token(5.),
        Token(TokenType.EOF, '')
    ]
    
def test_float_number():
    result = Tokezier('2.3')

    assert result == [
        get_Token(2.3),
        Token(TokenType.EOF, '')
    ]