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

    # NUMERIC

    def visitNumericInt(self, ctx):
        return float(ctx.INT().getText())
    def visitNumericFloat(self, ctx):
        return float(ctx.FLOAT().getText().replace(",", "."))

    def visitNumericPlusMinus(self, ctx):
        match ctx.op.type:
            case ScriptoriumParser.PLUS:
                return self.visit(ctx.numericExpr())
            case ScriptoriumParser.MINUS:
                return -self.visit(ctx.numericExpr())

    def visitNumericBrackets(self, ctx):
        return self.visit(ctx.numericExpr())

    def visitNumericPow(self, ctx):
        primary = self.visit(ctx.numericExpr(0))
        secondary = self.visit(ctx.numericExpr(1))
        return math.pow(primary, secondary)
            
    def visitNumericMulDiv(self, ctx):
        primary = self.visit(ctx.numericExpr(0))
        secondary = self.visit(ctx.numericExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.MUL:
                return primary * secondary
            case ScriptoriumParser.DIV:
                return primary / secondary
            case ScriptoriumParser.FDIV:
                return primary // secondary

    def visitNumericAddSub(self, ctx):
        primary = self.visit(ctx.numericExpr(0))
        secondary = self.visit(ctx.numericExpr(1))
        match ctx.op.type:
            case ScriptoriumParser.ADD:
                return primary+secondary
            case ScriptoriumParser.SUB:
                return primary-secondary

    def visitNumericMod(self, ctx):
        primary = self.visit(ctx.numericExpr(0))
        secondary = self.visit(ctx.numericExpr(1))
        return primary % secondary
    
    # INT

    def visitInt(self, ctx):
        return int(self.visit(ctx.numericExpr()))
    
    # FLOAT
    
    def visitFloat(self, ctx):
        return float(str(self.visit(ctx.numericExpr())).replace(",", "."))   

    # NULL
    
    def visitNull(self, ctx):
        return None

    # BOOL

    def visitBool(self, ctx):
        match ctx.BOOL().getText():
            case 'verum':
                return True
            case 'falsum':
                return False
            
    def visitBoolBrackets(self, ctx):
        return self.visit(ctx.boolExpr())

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

    def visitNumericLogic(self, ctx):
        primary:float = self.visit(ctx.numericExpr(0))
        secondary:float = self.visit(ctx.numericExpr(1))
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

    # VAR

    def visitVariableDeclaration(self, ctx):
        value = None
        if ctx.NAME().getText() in self.var_map:
            error_msg = f"CULPA: linea {ctx.start.line}:{ctx.start.column} - variable cannot be declared multiple times"
            raise Exception(error_msg)
        value = self.visit(ctx.expr())
        if value is None:
            self.var_map[ctx.NAME().getText()] = None
            return
        try:
            match ctx.varType.type:
                case ScriptoriumParser.INT_TYPE:
                    value = value or self.visit(ctx.expr())
                    self.var_map[ctx.NAME().getText()] = int(value)
                case ScriptoriumParser.FLOAT_TYPE:
                    value = value or self.visit(ctx.expr())
                    self.var_map[ctx.NAME().getText()] = float(trans if type(value) == str and (trans:=str(value).replace(',', '.')) else value)
                case ScriptoriumParser.STRING_TYPE:
                    value = value or self.visit(ctx.expr())
                    self.var_map[ctx.NAME().getText()] = str(value)
                case ScriptoriumParser.BOOL_TYPE:
                    value = value or self.visit(ctx.expr())
                    self.var_map[ctx.NAME().getText()] = bool(value)
        except:
            error_msg = f"CULPA: linea {ctx.start.line}:{ctx.start.column} - type transformation error"
            raise Exception(error_msg)
    
    def visitVarExpr(self, ctx):
        var = None;
        try:
            var = self.var_map[ctx.NAME().getText()]
        except:
            error_msg = f"CULPA: linea {ctx.start.line}:{ctx.start.column} - no variable named \"{ctx.NAME().getText()}\""
            raise Exception(error_msg)
        return var
    
    # INPUT

    def visitInputExpr(self, ctx):
        return input(self.visit(ctx.printExpr()))