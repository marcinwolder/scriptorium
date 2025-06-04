lexer grammar ScriptoriumLexer;

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

tokens { INDENT, DEDENT }

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
ELSE_IF: 'aliter si';
IF: 'si' ;
ELSE: 'aliter' ;
INPUT: 'rogare' ;
PRINT: 'scribere' ;

PLUS: 'positivum' ;
MINUS: 'negans' ;

INT: (PLUS|MINUS)? [0-9]+ ;
FLOAT: (PLUS|MINUS)? [0-9]+ ',' [0-9]+ ;
BOOL: ('verum'|'falsum') ;

INT_TYPE: 'numerus' ;
FLOAT_TYPE: 'fractio' ;
BOOL_TYPE: 'veritas' ;
STRING_TYPE: 'sententia' ;

PARENT: 'parentes' ;

AS: 'ut' ;

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

COMMENT: '\t'* '//' .*? NL -> channel(HIDDEN);

NL: ('\r'? '\n') '\t'*;
WS: [ ]+ -> skip;

STRING_START : '"' -> pushMode(IN_STRING) ;

mode IN_STRING;

INTERP_START : '${' -> pushMode(IN_INTERP) ;
STRING_END   : '"'  -> popMode ;
fragment ESC_SEQ : '\\' . ;
STRING_TEXT  : ( ESC_SEQ | ~["\\$] | '$' ~'{' )+ ;

mode IN_INTERP;

INTERP_END : '}' -> popMode ;

WS_INTERP   : [ \t\r\n]+ -> skip ;
INT_INTERP      : INT       -> type(INT) ;
FLOAT_INTERP    : FLOAT     -> type(FLOAT) ;
BOOL_INTERP     : BOOL      -> type(BOOL) ;
PARENT_INTERP   : PARENT    -> type(PARENT) ;
NAME_INTERP     : NAME      -> type(NAME) ;

ADD_INTERP      : ADD       -> type(ADD) ;
SUB_INTERP      : SUB       -> type(SUB);
MUL_INTERP      : MUL       -> type(MUL) ;
DIV_INTERP      : DIV       -> type(DIV) ;
POW_INTERP      : POW       -> type(POW) ;
MOD_INTERP      : MOD       -> type(MOD) ;
FDIV_INTERP     : FDIV      -> type(FDIV) ;

AND_INTERP      : AND       -> type(AND) ;
OR_INTERP       : OR        -> type(OR) ;
NOT_INTERP      : NOT       -> type(NOT) ;

LT_INTERP       : LT        -> type(LT) ;
LE_INTERP       : LE        -> type(LE) ;
GT_INTERP       : GT        -> type(GT) ;
GE_INTERP       : GE        -> type(GE) ;

EQ_INTERP       : EQ        -> type(EQ) ;
NEQ_INTERP      : NEQ       -> type(NEQ) ;

LP_INTERP       : LP        -> type(LP) ;
RP_INTERP       : RP        -> type(RP) ;