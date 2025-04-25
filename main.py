import sys
from antlr4 import CommonTokenStream, FileStream
from ErrorListener import ErrorListener
from ScriptoriumVisitor import Visitor
from ScriptoriumVariableListener import VariableListener
from Scriptorium.ScriptoriumLexer import ScriptoriumLexer
from Scriptorium.ScriptoriumParser import ScriptoriumParser

def main():
    var_map = {}

    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    try:
        lexer = ScriptoriumLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(ErrorListener())
        token_stream = CommonTokenStream(lexer)

        parser = ScriptoriumParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ErrorListener())
        parser.addParseListener(VariableListener(var_map))
        tree = parser.start()

        visitor = Visitor(var_map)
        visitor.visit(tree)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
