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
        # print(0)
        with open(sys.argv[1], encoding='utf-8') as f:
            input_lines = f.readlines()
        lexer = ScriptoriumLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(ErrorListener(input_lines))
        token_stream = CommonTokenStream(lexer)

        # print(1)

        parser = ScriptoriumParser(token_stream)
        parser.removeErrorListeners()
        parser.addErrorListener(ErrorListener(input_lines))
        parser.addParseListener(VariableListener(var_map))
        tree = parser.start()

        if sys.argv[2] == "tree":
            from dot_tree import tree_to_dot
            tree_to_dot(tree, parser, outfile="tree.dot", to_png=True)
            print(var_map)

        # print(2)
        # print("===")

        visitor = Visitor(var_map)
        visitor.visit(tree)

        # print(3)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
