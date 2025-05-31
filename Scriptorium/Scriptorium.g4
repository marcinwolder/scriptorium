grammar Scriptorium;

options { tokenVocab = ScriptoriumLexer; }
tokens { INDENT, DEDENT }

@lexer::header{
from antlr_denter.DenterHelper import DenterHelper
from Scriptorium.ScriptoriumParser import ScriptoriumParser
}
@lexer::members {
class ScriptoriumDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: ScriptoriumLexer = lexer

    def pull_token(self):
        buf = super(ScriptoriumLexer, self.lexer).nextToken()
        # print(buf)
        return buf

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.ScriptoriumDenter(self, self.NL, ScriptoriumParser.INDENT, ScriptoriumParser.DEDENT, False)
    buf = self.denter.next_token()
    # print(buf)
    return buf

}


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
    | nullExpr      
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

nullExpr: NULL #Null ;

errorStatement: ERROR printExpr DOT NL;

funcParam: varType=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE) NAME ;
functionDeclaration: varType=(INT_TYPE|FLOAT_TYPE|STRING_TYPE|BOOL_TYPE|NULL) FUNCTION NAME LP funcParam? (COMMA funcParam)* RP COLON actionBlock ;
functionInvocation: NAME LP expr? (PRINT_SEPARATOR expr)* RP ;

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
