grammar Scriptorium;

start: print* EOF ;

print: 'scribere' printExpr '.' ;

printExpr: expr
         | printExpr 'et' expr
         ;

expr: intExpr 
    | stringExpr
    ;

stringExpr: STRING
          | stringExpr ADD STRING
          ;

STRING: '"' (ESC | ~["\\])* '"' ;
ESC: '\\' ['"\\bfnrt] ;


intExpr: INT
       | intExpr intOpp INT
       ;

intOpp: ADD
      | SUB
      | MUL 
      | DIV
      | POW
      | MOD
      | FDIV
      ;

INT: [0-9]+ ;

ADD: 'adde';
SUB: 'minue';
MUL: 'multiplica';
DIV: 'divide';
POW: 'potentia';
MOD: 'residuum';
FDIV: 'totum';

WS: [ \n\t\r] -> skip ;