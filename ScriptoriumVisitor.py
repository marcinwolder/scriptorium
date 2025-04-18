import math

from Scriptorium.ScriptoriumParser import ScriptoriumParser
from Scriptorium.ScriptoriumVisitor import ScriptoriumVisitor

class Visitor(ScriptoriumVisitor):
    var_map = dict()
    listener = None
    def __init__(self, listener):
        self.listener = listener
        super().__init__()

    # PRINT

    def visitPrint(self, ctx):
        print(self.visit(ctx.printExpr()))

    def visitPrintAdd(self, ctx):
        return self.visit(ctx.printExpr(0))+', '+self.visit(ctx.printExpr(1))        
    
    def visitExprInPrint(self, ctx):
        return str(self.visit(ctx.expr()))

    # STRING

    def visitString(self, ctx):
        text = ctx.STRING().getText()[1:-1]
        text = text.replace("\\\\", "\\")
        text = text.replace("\\\"", "\"")
        return text

    def visitStringAdd(self, ctx):
        return self.visit(ctx.stringExpr(0))+self.visit(ctx.stringExpr(1))

    # INT

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitIntPow(self, ctx):
        primary = self.visit(ctx.intExpr(0))
        secondary = self.visit(ctx.intExpr(1))
        return int(math.pow(primary, secondary))
            
    def visitIntMulDiv(self, ctx):
        primary = self.visit(ctx.intExpr(0))
        secondary = self.visit(ctx.intExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.MUL:
                return primary * secondary
            case ScriptoriumParser.DIV:
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
    
    # FLOAT
    
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
                return primary * secondary
            case ScriptoriumParser.DIV:
                return primary / secondary
            case ScriptoriumParser.FDIV:
                return primary // secondary

    def visitFloatAddSub(self, ctx):
        primary = self.visit(ctx.floatExpr(0))
        secondary = self.visit(ctx.floatExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.ADD:
                return primary + secondary
            case ScriptoriumParser.SUB:
                return primary - secondary

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
            
    def visitNull(self, ctx):
        return None
            
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

    def visitVarExpr(self, ctx):
        var = None;
        try:
            var = self.var_map[ctx.NAME().getText()]
        except:
            error_msg = f"CULPA: linea {ctx.start.line}:{ctx.start.column} - no variable named \"{ctx.NAME().getText()}\""
            raise Exception(error_msg)
        return var
    
    def visitInputExpr(self, ctx):
        return input(self.visit(ctx.printExpr()))

    def visitVariableDeclaration(self, ctx):
        value = None
        if ctx.NAME().getText() in self.var_map:
            error_msg = f"CULPA: linea {ctx.start.line}:{ctx.start.column} - variable cannot be declared multiple times"
            raise Exception(error_msg)
        if ctx.nullExpr() is not None:
            self.var_map[ctx.NAME().getText()] = None
            return
        if ctx.inputExpr() is not None:
            value = self.visit(ctx.inputExpr())
        try:
            match ctx.type_.type:
                case ScriptoriumParser.INT_TYPE:
                    value = value or self.visit(ctx.intExpr())
                    self.var_map[ctx.NAME().getText()] = int(value)
                case ScriptoriumParser.FLOAT_TYPE:
                    value = value or self.visit(ctx.floatExpr())
                    self.var_map[ctx.NAME().getText()] = float(trans if type(value) == str and (trans:=str(value).replace(',', '.')) else value)
                case ScriptoriumParser.STRING_TYPE:
                    value = value or self.visit(ctx.stringExpr())
                    self.var_map[ctx.NAME().getText()] = str(value)
                case ScriptoriumParser.BOOL_TYPE:
                    value = value or self.visit(ctx.boolExpr())
                    self.var_map[ctx.NAME().getText()] = bool(value)
        except:
            error_msg = f"CULPA: linea {ctx.start.line}:{ctx.start.column} - type transformation error"
            raise Exception(error_msg)