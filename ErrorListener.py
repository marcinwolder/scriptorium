import re
import difflib
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

KEYWORDS = ["et", "culpa", "munus", "reddere", "dum", "repetere",
            "ex", "ad", "exire", "perge", "aliter si", "si",
            "aliter", "rogare", "scribere", "positivum", "negans",
            "numerus", "fractio", "veritas", "sententia", "nihil",
            "esto", "adde", "minue", "multiplica", "divide", "potentia",
            "residuum", "totum", "etiam", "aut", "non", "minor quam",
            "minor aequalis", "maior quam", "maior aequalis", "aequalis",
            "inaequale"]

class ErrorListener(ErrorListener):
    def __init__(self, input_lines=None):
        super().__init__()
        self.input_lines = input_lines

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        suggestion = ""
        line_text = ""
        error = ""
        if self.input_lines and 0 < line <= len(self.input_lines):
            line_text = self.input_lines[line-1]
        if line_text:
            words = line_text.strip().replace("(", " ").replace(")", " ").replace(",", " ").replace("{", " ").replace("}", " ").split()
            for word in words:
                close = difflib.get_close_matches(word, KEYWORDS, n=1)
                error = word
                if close and word not in KEYWORDS:
                    suggestion = f' (Did you mean "{close[0]}" instead of "{word}"?)'
                    break
        if str(msg).count('no viable alternative at input'):
            if match:=re.search(r"['].*[']", msg):
                error_msg = f"CULPA: linea {line}:{column} - syntax error at {error}{suggestion}"
            else:
                error_msg = f"CULPA: linea {line}:{column} - {msg}"
        elif re.search(r"token recognition error at: \'\".*\\n\'", msg):
            error_msg = f"CULPA: linea {line}:{column} - missing (\")"
        elif re.search(r"mismatched input '.*' expecting \{.*\}", msg):
            error_msg = f"CULPA: linea {line}:{column} - incomplete or incorrect sentence"
        else:
            error_msg = f"CULPA: linea {line}:{column} - {msg}"
        raise Exception(error_msg)