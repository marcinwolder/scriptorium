from Scriptorium.ScriptoriumParser import ScriptoriumParser
from Scriptorium.ScriptoriumListener import ScriptoriumListener
from antlr4.tree.Tree import RuleNode

class Listener(ScriptoriumListener):
    indent_count = 0
    indent_map = dict()

    def enterIf(self, ctx):
        self.indent_count += 1
        self.indent_map[self.indent_count] = ctx
        return super().enterIf(ctx)
    def exitIf(self, ctx):
        self.indent_map[self.indent_count]
        self.indent_count -= 1
        return super().exitIf(ctx)

    def enterIndentAction(self, ctx):
        indent = len(ctx.INDENT().getText())
        while self.indent_count > indent:
            self.indent_map[self.indent_count].exitRule(self)
        
        return super().enterIndentAction(ctx)