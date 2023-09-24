from calc.tokenizer import Tokezier
from calc.paser import Paser, BinaryAst, ConstAst, UnaryAst

def test_parse():
    assert Paser(
        Tokezier("1 + 2 + 3").tokens
        ).parse_express() == BinaryAst(ConstAst(1), '+', BinaryAst(ConstAst(2), '+', ConstAst(3)))

def test_parse2():
    assert Paser(
        Tokezier("1 * 2 + 3").tokens
        ).parse_express() == BinaryAst(BinaryAst(ConstAst(1), '*', ConstAst(2)), '+', ConstAst(3))
    
def test_parse3():
    assert Paser(
        Tokezier("1 * ( 2 + 3 )").tokens
        ).parse_express() == BinaryAst(ConstAst(1), '*', BinaryAst(ConstAst(2), '+', ConstAst(3)))
    
def test_parse4():
    assert Paser(
        Tokezier("1 * ( -2 + 3 )").tokens
        ).parse_express() == BinaryAst(ConstAst(1), '*', BinaryAst(UnaryAst('-', ConstAst(2)), '+', ConstAst(3)))
    
def test_parse4():
    assert Paser(
        Tokezier("((1 + 2) * (3 - 4)) / (5 * 6)").tokens
        ).parse_express() == BinaryAst(BinaryAst(BinaryAst(ConstAst(1.0), '+', ConstAst(2.0)), '*', BinaryAst(ConstAst(3.0), '-', ConstAst(4.0))), '/', BinaryAst(ConstAst(5.0), '*', ConstAst(6.0)))