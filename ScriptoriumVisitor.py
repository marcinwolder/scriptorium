from Scriptorium.ScriptoriumParser import ScriptoriumParser
from Scriptorium.ScriptoriumVisitor import ScriptoriumVisitor
from antlr4.tree.Tree import TerminalNodeImpl

class Visitor(ScriptoriumVisitor):
    int_vars: dict[str, int] = {}

    def visitVariable(self, ctx:ScriptoriumParser.VariableContext):
        if ctx.NUMERUS():
            name:TerminalNodeImpl = ctx.NAME()
            self.int_vars[name.getText()] = int(ctx.INTVALUE().getText())
        if ctx.FRACTIO():
            print('fractio', ctx.NAME())
        return self.visitChildren(ctx)
    
    def visitPrint(self, ctx:ScriptoriumParser.PrintContext):
        if (var_name := ctx.NAME()):
            print(self.int_vars[var_name.getText()])
        return self.visitChildren(ctx)