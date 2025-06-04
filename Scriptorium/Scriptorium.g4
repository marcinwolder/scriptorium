grammar Scriptorium;

options { tokenVocab = ScriptoriumLexer; }

// PARSER

start: action* EOF;

action: variableDeclaration
      | parentVariableDefinition
      | if
      | forLoop
      | whileLoop
      | functionDeclaration
      | functionInvocation DOT NL
      | print
      | errorStatement
      | returnStatement
      | continueStatement
      | breakStatement
      | COMMENT
      | NL
      ;

templateString
    : STRING_START templatePart* STRING_END
    ;

templatePart
    : STRING_TEXT
    | interpolation
    ;

interpolation
    : INTERP_START varExpr INTERP_END
    ;

expr: boolExpr
    | floatExpr     
    | intExpr       
    | stringExpr       
    | inputExpr
    | functionInvocation
    | varExpr    
    ;

varExpr: PARENT* NAME ;


castedExpr: (INT|FLOAT|templateString|BOOL|functionInvocation|varExpr) AS type=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE)  #CastedValue
          | castedExpr AS type=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE)                                                  #CastedAgain
          ;

stringExpr
    : templateString              #String
    | stringExpr ADD stringExpr   #StringAdd
    | varExpr                     #StringVar
    | castedExpr                  #StringCast
    | functionInvocation          #StringFunc
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
           | castedExpr                                 #NumericCast
           | functionInvocation                         #NumericFunc
           ;
intExpr: numericExpr #Int ;
floatExpr: numericExpr #Float ;

boolExpr: BOOL                                              #Bool
        | NOT boolExpr                                      #BoolNot
        | LP boolExpr RP                                    #BoolBrackets
        | boolExpr AND boolExpr                             #BoolAnd
        | boolExpr OR boolExpr                              #BoolOr
        | boolExpr op=(EQ|NEQ) boolExpr                     #BoolEqual
        | stringExpr op=(LT|LE|GT|GE|EQ|NEQ) stringExpr     #StringLogic
        | numericExpr op=(LT|LE|GT|GE|EQ|NEQ) numericExpr   #NumericLogic
        | varExpr                                           #BoolVar
        | castedExpr                                        #BoolCast
        | functionInvocation                                #BoolFunc
        ;

errorStatement: ERROR printExpr DOT NL;

funcParam: varType=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE) NAME ;
functionDeclaration: varType=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE|NULL) FUNCTION NAME LP funcParam? (PRINT_SEPARATOR funcParam)* RP COLON actionBlock ;
functionInvocation: NAME LP expr? (PRINT_SEPARATOR expr)* RP;

returnStatement: RETURN expr? DOT NL ;

whileLoop: WHILE boolExpr COLON loopBlock ;
forLoop: FOR NAME FROM from=numericExpr TO to=numericExpr COLON loopBlock ;
loopBlock: actionBlock ;

breakStatement: BREAK DOT NL;
continueStatement: CONTINUE DOT NL;

variableDeclaration: varType=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE) variableDefinition
                   | varType=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE) NAME DOT NL;
variableDefinition: NAME IS expr DOT NL;
parentVariableDefinition: PARENT* variableDefinition ;

if: ifBlock ifElseBlock* elseBlock?;

ifBlock: IF boolExpr COLON actionBlock ;
ifElseBlock: ELSE_IF boolExpr COLON actionBlock ;
elseBlock: ELSE COLON actionBlock ;

actionBlock: INDENT action+ DEDENT ;

inputExpr: INPUT printExpr ;

print: PRINT printExpr DOT NL;

printExpr: expr                                 #ExprInPrint
         | printExpr PRINT_SEPARATOR printExpr  #PrintAdd
         ;
