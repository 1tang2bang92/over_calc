from .paser import Paser
from .tokenizer import Tokezier
from .evaluate import Evaluate

class Calc():
    __express: str = ''

    def __init__(self, express: str) -> None:
        self.__express = express
        pass
    
    def run(self):
        return Evaluate(Paser(Tokezier(self.__express).tokens).parse_express()).Eval()