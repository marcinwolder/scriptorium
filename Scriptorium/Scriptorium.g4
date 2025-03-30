grammar Scriptorium;

start: (action | '\n')*;

INT: '-'? [0-9]+ ;
FLOAT: '-'? [0-9]+ ',' [0-9]+ ;
STRING: '"' (ESC | ~["\\])* '"' ;
fragment
ESC: '\\' ["\\] ;
BOOL: ('verum'|'falsum') ;

ADD: 'adde'; // "+"
SUB: 'minue'; // "-"
MUL: 'multiplica'; // "*"
DIV: 'divide'; // "/"
POW: 'potentia'; // "^"
MOD: 'residuum'; // "%"
FDIV: 'totum'; // "//"

AND: 'etiam' ; // "&&"
OR: 'aut' ; // "||"
NOT: 'non' ; // "!"

LT: 'minor quam' ; // “<”
LE: 'minor aequalis' ; // “<=”
GT: 'maior quam' ; // “>”
GE: 'maior aequalis' ; // “>=”

EQ: 'aequalis' ; // "=="
NEQ: 'inaequale' ; // "!="

WS: [ \r\t]+ -> skip ;
INDENT: [>]+ ;

action: if
      | print '.'
      ;

print: 'scribere' printExpr ;

printExpr: expr                         #ExprInPrint
         | printExpr 'et' printExpr     #PrintAdd
         ;


if: 'si' boolExpr ':' '\n' indentAction+ ;

indentAction: INDENT action+ '\n'; 

expr: floatExpr
    | intExpr
    | stringExpr
    | boolExpr
    ;

stringExpr
    : STRING                      #String
    | stringExpr ADD stringExpr   #StringAdd
    ;



intExpr: INT                                    #Int
       | intExpr POW intExpr                    #IntPow
       | intExpr op=(MUL | FDIV) intExpr        #IntMulFDiv
       | intExpr op=(ADD | SUB) intExpr         #IntAddSub
       | intExpr MOD intExpr                    #IntMod
       ;


floatExpr: FLOAT                                      #Float
         | floatExpr POW floatExpr                    #FloatPow
         | floatExpr op=(MUL | DIV | FDIV) floatExpr  #FloatMulDiv
         | floatExpr op=(ADD | SUB) floatExpr         #FloatAddSub
         | floatExpr MOD floatExpr                    #FloatMod
         | intExpr DIV intExpr                        #FloatIntDiv
         ;

boolExpr: BOOL                                              #Bool
        | NOT boolExpr                                      #BoolNot
        | stringExpr op=(LT|LE|GT|GE|EQ|NEQ) stringExpr     #StringLogic
        | intExpr op=(LT|LE|GT|GE|EQ|NEQ) intExpr           #IntLogic
        | floatExpr op=(LT|LE|GT|GE|EQ|NEQ) floatExpr       #FloatLogic
        | boolExpr op=(AND|OR|EQ|NEQ) boolExpr              #BoolLogic
        ;

