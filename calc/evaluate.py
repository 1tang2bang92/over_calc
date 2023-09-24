from calc.paser import BinaryAst, ConstAst, UnaryAst, BaseAst

def calc(a: float, b: str, c: float) -> float:
        if b == '+':
            return a + c
        elif b == '-':
            return a - c
        elif b == '*':
            return a * c
        elif b == '/':
            return a / c

def real_eval(ast: BaseAst) -> float:
        if isinstance(ast, BinaryAst):
            return calc(real_eval(ast.lhs), ast.operator, real_eval(ast.rhs))
        elif isinstance(ast, UnaryAst):
            return calc(0, ast.operator, real_eval(ast.rhs))
        elif isinstance(ast, ConstAst):
            return ast.value
        else:
            None

class Evaluate:
    __Ast:BaseAst = BaseAst()

    def __init__(self, Ast: BaseAst) -> None:
        self.__Ast = Ast
        pass
        
    def Eval(self):
        return real_eval(self.__Ast)
        
    