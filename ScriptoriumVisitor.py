import math
from Scriptorium.ScriptoriumParser import ScriptoriumParser
from Scriptorium.ScriptoriumVisitor import ScriptoriumVisitor

class Visitor(ScriptoriumVisitor):

    def visitStringExpr(self, ctx:ScriptoriumParser.StringExprContext):
        secondary = ctx.STRING().getText()[1:-1]
        primary = None
        if ctx.stringExpr() is None:
            return secondary
        else:
            primary = self.visit(ctx.stringExpr())
        return primary+secondary

    def visitIntExpr(self, ctx:ScriptoriumParser.IntExprContext):
        secondary = int(ctx.INT().getText())
        primary = None
        if ctx.intExpr() is None:
            return secondary
        else:
            primary = self.visit(ctx.intExpr())
        match ctx.getChild(1).getChild(0).getSymbol().type:
            case ScriptoriumParser.ADD:
                return primary+secondary
            case ScriptoriumParser.SUB:
                return primary-secondary
            case ScriptoriumParser.MUL:
                return primary*secondary
            case ScriptoriumParser.DIV:
                return primary/secondary
            case ScriptoriumParser.POW:
                return int(math.pow(primary, secondary))
            case ScriptoriumParser.MOD:
                return primary % secondary
            case ScriptoriumParser.FDIV:
                return primary // secondary
    
    def visitPrint(self, ctx:ScriptoriumParser.PrintContext):
        print(self.visit(ctx.printExpr()))

    def visitPrintExpr(self, ctx:ScriptoriumParser.PrintExprContext):
        if ctx.printExpr() is None:
            return str(self.visit(ctx.expr()))
        if ctx.printExpr is not None:
            return str(self.visit(ctx.printExpr())) + ", " \
                + str(self.visit(ctx.expr()))