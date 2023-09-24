from calc.paser import Paser
from calc.tokenizer import Tokezier
from calc.evaluate import Evaluate

def express2eval(str):
    return Evaluate(Paser(Tokezier(str).tokens).parse_express()).Eval()

def test_eval():
    assert express2eval('(1 + 2) * 3') == 9

def test_eval2():
    assert 7 == express2eval('1 + 6')

def test_eval3():
    assert -0.1 == express2eval('((1 + 2) * (3 - 4)) / (5 * 6)')
    

def test_eval4():
    assert 1.6 == express2eval('2 * (1 + 3) / 5')

def test_eval5():
    assert 5 == express2eval('----5')
    
def test_eval6():
    assert -5 == express2eval('-----5')