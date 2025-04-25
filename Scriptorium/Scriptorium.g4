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
    | floatExpr     
    | intExpr       
    | stringExpr       
    | nullExpr      
    | inputExpr    
    ;

varExpr: NAME ;

stringExpr
    : STRING                      #String
    | stringExpr ADD stringExpr   #StringAdd
    | varExpr                     #StringVar
    ;

numericExpr: INT                                        #NumericInt
           | FLOAT                                      #NumericFloat
           | LP numericExpr RP                          #NumericBrackets
           | op=(PLUS|MINUS) numericExpr                #NumericPlusMinus
           | numericExpr POW numericExpr                #NumericPow
           | numericExpr op=(MUL|DIV|FDIV) numericExpr  #NumericMulDiv
           | numericExpr op=(ADD|SUB) numericExpr       #NumericAddSub
           | numericExpr MOD numericExpr                #NumericMod
           | varExpr                                    #NumericVar
           ;
intExpr: numericExpr #Int ;
floatExpr: numericExpr #Float ;

boolExpr: BOOL                                              #Bool
        | NOT boolExpr                                      #BoolNot
        | LP boolExpr RP                                    #BoolBrackets
        | stringExpr op=(LT|LE|GT|GE|EQ|NEQ) stringExpr     #StringLogic
        | numericExpr op=(LT|LE|GT|GE|EQ|NEQ) numericExpr   #NumericLogic
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

variableDeclaration: varType=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE) NAME IS expr DOT ;

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

PLUS: 'positivum' ;
MINUS: 'negans' ;

INT: (PLUS|MINUS)? [0-9]+ ;
FLOAT: (PLUS|MINUS)? [0-9]+ ',' [0-9]+ ;
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
