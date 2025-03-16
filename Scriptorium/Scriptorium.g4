grammar Scriptorium;

start: (variable|print)* EOF;

print: 'scribere' (NAME) '.' ;
variable: (NUMERUS|FRACTIO|VERITAS|SENTENTIA) NAME 'esto' (INTVALUE|FLOATVALUE|BOOLVALUE|STRINGVALUE|NULLVALUE) '.';

NUMERUS: 'numerus' ;
FRACTIO: 'fractio' ;
VERITAS: 'veritas' ;
SENTENTIA: 'sententia' ;

NAME: [A-Za-z_]+ ;

INTVALUE: [0-9]+ ;
FLOATVALUE: [0-9]+'.'[0-9]+ ;
BOOLVALUE: ('verum'|'falsum') ;
STRINGVALUE: '"'.*?'"' ;
NULLVALUE: 'nihil' ;

WS: [ \t\n\r]+ -> skip ;