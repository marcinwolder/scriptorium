import os
import sys
from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from graphviz import Source
from ScriptoriumVisitor import Visitor
from ScriptoriumListener import Listener
from Scriptorium.ScriptoriumLexer import ScriptoriumLexer
from Scriptorium.ScriptoriumParser import ScriptoriumParser
from antlr4.tree.Trees import Trees

def main():
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    
    lexer = ScriptoriumLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = ScriptoriumParser(token_stream)
    tree = parser.start()

    visitor = Visitor()
    visitor.visit(tree)

    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    main()
