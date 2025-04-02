import sys
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from ErrorListener import ErrorListener
from ScriptoriumVisitor import Visitor
from ScriptoriumListener import Listener
from Scriptorium.ScriptoriumLexer import ScriptoriumLexer
from Scriptorium.ScriptoriumParser import ScriptoriumParser

def main():
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    try:
        lexer = ScriptoriumLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(ErrorListener())
        token_stream = CommonTokenStream(lexer)

        parser = ScriptoriumParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ErrorListener())
        tree = parser.start()

        listener = Listener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        visitor = Visitor(listener)
        visitor.visit(tree)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
