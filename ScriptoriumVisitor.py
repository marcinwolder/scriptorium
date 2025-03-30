import math

from Scriptorium.ScriptoriumParser import ScriptoriumParser
from Scriptorium.ScriptoriumVisitor import ScriptoriumVisitor

class Visitor(ScriptoriumVisitor):
    def visitPrint(self, ctx):
        print(self.visit(ctx.printExpr()))

    def visitPrintAdd(self, ctx):
        return self.visit(ctx.printExpr(0))+', '+self.visit(ctx.printExpr(1))        
    
    def visitExprInPrint(self, ctx):
        return str(self.visit(ctx.expr()))

    def visitString(self, ctx):
        text = ctx.STRING().getText()[1:-1]
        text = text.replace("\\\\", "\\")
        text = text.replace("\\\"", "\"")
        return text

    def visitStringAdd(self, ctx):
        return self.visit(ctx.stringExpr(0))+self.visit(ctx.stringExpr(1))

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitIntPow(self, ctx):
        primary = self.visit(ctx.intExpr(0))
        secondary = self.visit(ctx.intExpr(1))
        return int(math.pow(primary, secondary))
            
    def visitIntMulFDiv(self, ctx):
        primary = self.visit(ctx.intExpr(0))
        secondary = self.visit(ctx.intExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.MUL:
                return primary*secondary
            case ScriptoriumParser.FDIV:
                return primary // secondary

    def visitIntAddSub(self, ctx):
        primary = self.visit(ctx.intExpr(0))
        secondary = self.visit(ctx.intExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.ADD:
                return primary+secondary
            case ScriptoriumParser.SUB:
                return primary-secondary

    def visitIntMod(self, ctx):
        primary = self.visit(ctx.intExpr(0))
        secondary = self.visit(ctx.intExpr(1))
        return primary % secondary
    
    def visitFloatIntDiv(self, ctx):
        primary = self.visit(ctx.intExpr(0))
        secondary = self.visit(ctx.intExpr(1))
        return float(primary/secondary)
    
    def visitFloat(self, ctx):
        return float(ctx.FLOAT().getText().replace(",", "."))

    def visitFloatPow(self, ctx):
        primary = self.visit(ctx.floatExpr(0))
        secondary = self.visit(ctx.floatExpr(1))
        return math.pow(primary, secondary)
            
    def visitFloatMulDiv(self, ctx):
        primary = self.visit(ctx.floatExpr(0))
        secondary = self.visit(ctx.floatExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.MUL:
                return primary*secondary
            case ScriptoriumParser.DIV:
                return primary / secondary
            case ScriptoriumParser.FDIV:
                return primary // secondary

    def visitFloatAddSub(self, ctx):
        primary = self.visit(ctx.floatExpr(0))
        secondary = self.visit(ctx.floatExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.ADD:
                return primary+secondary
            case ScriptoriumParser.SUB:
                return primary-secondary

    def visitFloatMod(self, ctx):
        primary = self.visit(ctx.floatExpr(0))
        secondary = self.visit(ctx.floatExpr(1))
        return primary % secondary
    
    def visitBool(self, ctx):
        match ctx.BOOL().getText():
            case 'verum':
                return True
            case 'falsum':
                return False
            
    def visitStringLogic(self, ctx):
        primary:str = self.visit(ctx.stringExpr(0))
        secondary:str = self.visit(ctx.stringExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.EQ:
                return primary == secondary
            case ScriptoriumParser.NEQ:
                return primary != secondary
            case ScriptoriumParser.LT:
                return primary < secondary
            case ScriptoriumParser.GT:
                return primary > secondary
            case ScriptoriumParser.LE:
                return primary <= secondary
            case ScriptoriumParser.GE:
                return primary >= secondary
            
    def visitIntLogic(self, ctx):
        primary:int = self.visit(ctx.intExpr(0))
        secondary:int = self.visit(ctx.intExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.EQ:
                return primary == secondary
            case ScriptoriumParser.NEQ:
                return primary != secondary
            case ScriptoriumParser.LT:
                return primary < secondary
            case ScriptoriumParser.GT:
                return primary > secondary
            case ScriptoriumParser.LE:
                return primary <= secondary
            case ScriptoriumParser.GE:
                return primary >= secondary

    def visitFloatLogic(self, ctx):
        primary:float = self.visit(ctx.floatExpr(0))
        secondary:float = self.visit(ctx.floatExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.EQ:
                return primary == secondary
            case ScriptoriumParser.NEQ:
                return primary != secondary
            case ScriptoriumParser.LT:
                return primary < secondary
            case ScriptoriumParser.GT:
                return primary > secondary
            case ScriptoriumParser.LE:
                return primary <= secondary
            case ScriptoriumParser.GE:
                return primary >= secondary

    def visitBoolLogic(self, ctx):
        primary:bool = self.visit(ctx.boolExpr(0))
        secondary:bool = self.visit(ctx.boolExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.AND:
                return primary and secondary
            case ScriptoriumParser.OR:
                return primary or secondary
            case ScriptoriumParser.EQ:
                return primary == secondary
            case ScriptoriumParser.NEQ:
                return primary != secondary

    def visitBoolNot(self, ctx):
        primary:bool = self.visit(ctx.boolExpr())
        return not primary