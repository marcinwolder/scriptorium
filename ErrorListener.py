import re
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

class ErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        if str(msg).count('no viable alternative at input'):
            if match:=re.search(r"['].*[']", msg):
                error_msg = f"CULPA: linea {line}:{column} - syntax error at {match.group()}"
            else:
                error_msg = f"CULPA: linea {line}:{column} - {msg}"
        elif re.search(r"token recognition error at: \'\".*\\n\'", msg):
            error_msg = f"CULPA: linea {line}:{column} - missing (\")"
        elif re.search(r"mismatched input '.*' expecting \{.*\}", msg):
            error_msg = f"CULPA: linea {line}:{column} - incomplete or incorrect sentence"
        else:
            error_msg = f"CULPA: linea {line}:{column} - {msg}"
        raise Exception(error_msg)