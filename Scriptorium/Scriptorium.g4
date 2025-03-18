grammar Scriptorium;

start: print* EOF ;

print: 'scribere' printExpr '.' ;

printExpr: expr
         | printExpr 'et' expr
         ;

expr: intExpr ;

intExpr: INT intOpp INT
       | intExpr intOpp INT
       | INT
       ;

intOpp: ADD
      | SUB
      | MUL 
      | DIV
      | POW
      | MOD
      | FDIV
      ;

ADD: 'adde';
SUB: 'minue';
MUL: 'multiplica';
DIV: 'divide';
POW: 'potentia';
MOD: 'residuum';
FDIV: 'totum';

INT: [0-9]+ ;

WS: [ \n\t\r] -> skip ;