호서대 gate동아리에서 계산기를 만들기위한 예제코드

동작방식:
lexer -> paser -> evaluate
    token      AST

lexer에서 평문을 받아 token와 시킨다
paser에서는 token들을 받아 AST(Abstract Syntex Tree)를 생성한다.
evaluate에서는 AST의 비선형구조를 따라 재귀적으로 식을 평가한다.

test는 pytest를 활용해 실행가능

의존된 라이브러리:
pytest == 7.4.2