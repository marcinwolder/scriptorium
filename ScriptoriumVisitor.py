import math
from Scriptorium.ScriptoriumParser import ScriptoriumParser
from Scriptorium.ScriptoriumVisitor import ScriptoriumVisitor

class Visitor(ScriptoriumVisitor):

    def visitIntExpr(self, ctx:ScriptoriumParser.IntExprContext):
        ints = [int(num.getText()) for num in list(ctx.INT())]
        if ctx.intExpr() is None and len(ints) == 1:
            return ints[0]
        if ctx.intExpr() is not None:
            ints.insert(0, self.visit(ctx.intExpr()))
        match ctx.getChild(1).getChild(0).getSymbol().type:
            case ScriptoriumParser.ADD:
                return ints[0]+ints[1]
            case ScriptoriumParser.SUB:
                return ints[0]-ints[1]
            case ScriptoriumParser.MUL:
                return ints[0]*ints[1]
            case ScriptoriumParser.DIV:
                return ints[0]/ints[1]
            case ScriptoriumParser.POW:
                return int(math.pow(ints[0], ints[1]))
            case ScriptoriumParser.MOD:
                return ints[0] % ints[1]
            case ScriptoriumParser.FDIV:
                return ints[0] // ints[1]
    
    def visitPrint(self, ctx:ScriptoriumParser.PrintContext):
        print(self.visit(ctx.printExpr()))

    def visitPrintExpr(self, ctx:ScriptoriumParser.PrintExprContext):
        if ctx.printExpr() is None:
            return str(self.visit(ctx.expr()))
        if ctx.printExpr is not None:
            return str(self.visit(ctx.printExpr())) + ", " \
                + str(self.visit(ctx.expr()))