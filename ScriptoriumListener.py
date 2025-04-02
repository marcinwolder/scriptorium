from Scriptorium.ScriptoriumParser import ScriptoriumParser
from Scriptorium.ScriptoriumListener import ScriptoriumListener
from antlr4.tree.Tree import RuleNode

class Listener(ScriptoriumListener):
    indent = 0
    indent_map = dict()

    def enterIf(self, ctx):
        self.indent += 1
        self.indent_map[self.indent] = ctx
    def exitIf(self, ctx):
        self.indent_map[self.indent]
        self.indent -= 1