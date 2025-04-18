grammar Scriptorium;

// PARSER

start: (action|NL)* EOF;

action: variableDeclaration
      | if
      | forLoop
      | whileLoop
      | function
      | print
      | errorStatement
      ;

expr: varExpr  
    | boolExpr
    | intExpr       
    | floatExpr     
    | stringExpr       
    | nullExpr          
    ;

varExpr: NAME ;

stringExpr
    : STRING                      #String
    | stringExpr ADD stringExpr   #StringAdd
    | varExpr                     #StringVar
    ;

intExpr: INT                                    #Int
       | intExpr POW intExpr                    #IntPow
       | intExpr op=(MUL | DIV) intExpr         #IntMulDiv
       | intExpr op=(ADD | SUB) intExpr         #IntAddSub
       | intExpr MOD intExpr                    #IntMod
       | varExpr                                #IntVar
       ;

floatExpr: FLOAT                                      #Float
         | floatExpr POW floatExpr                    #FloatPow
         | floatExpr op=(MUL | DIV | FDIV) floatExpr  #FloatMulDiv
         | floatExpr op=(ADD | SUB) floatExpr         #FloatAddSub
         | floatExpr MOD floatExpr                    #FloatMod
         | varExpr                                    #FloatVar
         ;

boolExpr: BOOL                                              #Bool
        | NOT boolExpr                                      #BoolNot
        | stringExpr op=(LT|LE|GT|GE|EQ|NEQ) stringExpr     #StringLogic
        | intExpr op=(LT|LE|GT|GE|EQ|NEQ) intExpr           #IntLogic
        | floatExpr op=(LT|LE|GT|GE|EQ|NEQ) floatExpr       #FloatLogic
        | boolExpr op=(AND|OR|EQ|NEQ) boolExpr              #BoolLogic
        | varExpr                                           #BoolVar
        ;

nullExpr: NULL #Null ;

errorStatement: ERROR printExpr DOT ;

funcParam: type=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE) NAME ;
function: type=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE|NULL) FUNCTION NAME LP funcParam (COMMA funcParam)* RP COLON (action|returnStatement)+ NL;

returnStatement: RETURN expr DOT;

whileLoop: WHILE boolExpr COLON (action|continueStatement|breakStatement)+ NL ;

forLoop: FOR NAME FROM from=INT TO to=INT COLON (action|continueStatement|breakStatement)+ NL ;

breakStatement: BREAK DOT;
continueStatement: CONTINUE DOT;

variableDeclaration: type=INT_TYPE NAME IS (intExpr|nullExpr|inputExpr) DOT
                   | type=FLOAT_TYPE NAME IS (floatExpr|nullExpr|inputExpr) DOT
                   | type=STRING_TYPE NAME IS (stringExpr|nullExpr|inputExpr) DOT
                   | type=BOOL_TYPE NAME IS (boolExpr|nullExpr|inputExpr) DOT
                   ;

if: ifBlock ifElseBlock* elseBlock?;

ifBlock: IF boolExpr COLON (action)+ NL ;
ifElseBlock: ELSE IF boolExpr COLON (action)+ NL ;
elseBlock: ELSE COLON (action)+ NL ;

inputExpr: INPUT printExpr ;

print: PRINT printExpr DOT ;

printExpr: expr                                 #ExprInPrint
         | printExpr PRINT_SEPARATOR printExpr  #PrintAdd
         ;

// LEXER

PRINT_SEPARATOR: 'et' ;
ERROR: 'culpa' ;
FUNCTION: 'munus' ;
RETURN: 'reddere' ;
WHILE: 'dum' ;
FOR: 'repetere' ;
FROM: 'ex' ;
TO: 'ad' ;
BREAK: 'exire' ;
CONTINUE: 'perge' ;
IF: 'si' ;
ELSE: 'aliter' ;
INPUT: 'rogare' ;
PRINT: 'scribere' ;

INT: '-'? [0-9]+ ;
FLOAT: '-'? [0-9]+ ',' [0-9]+ ;
fragment ESC: '\\' ["\\] ;
STRING: '"' (ESC | ~["\\\n])* '"' ;
BOOL: ('verum'|'falsum') ;

INT_TYPE: 'numerus' ;
FLOAT_TYPE: 'fractio' ;
BOOL_TYPE: 'veritas' ;
STRING_TYPE: 'sententia' ;

NULL: 'nihil' ;

IS: 'esto' ; // =

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

DOT: '.' ;
COMMA: ',' ;
COLON: ':' ;
LP: '(' ;
RP: ')' ;

NAME: [a-z_]+[a-zA-Z0-9_]* ;

WS: [ \t]+ -> channel(HIDDEN) ;
NL: '\r'? '\n';
