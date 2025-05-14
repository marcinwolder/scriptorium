import math
from typing import List

from Scriptorium.ScriptoriumParser import ScriptoriumParser
from Scriptorium.ScriptoriumVisitor import ScriptoriumVisitor
from var import Var

class Visitor(ScriptoriumVisitor):
    var_map = {}
    recursion_level = 0

    def __init__(self, var_map):
        self.var_map = var_map
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
        if ctx.op.type == ScriptoriumParser.PLUS:
            return self.visit(ctx.numericExpr())
        elif ctx.op.type == ScriptoriumParser.MINUS:
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
        if ctx.op.type == ScriptoriumParser.MUL:
            return primary * secondary
        elif ctx.op.type == ScriptoriumParser.DIV:
            return primary / secondary
        elif ctx.op.type == ScriptoriumParser.FDIV:
            return primary // secondary

    def visitNumericAddSub(self, ctx):
        primary = self.visit(ctx.numericExpr(0))
        secondary = self.visit(ctx.numericExpr(1))
        if ctx.op.type == ScriptoriumParser.ADD:
            return primary+secondary
        elif ctx.op.type == ScriptoriumParser.SUB:
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
        if ctx.BOOL().getText() == 'verum':
            return True
        elif ctx.BOOL().getText() == 'falsum':
            return False
            
    def visitBoolBrackets(self, ctx):
        return self.visit(ctx.boolExpr())

    def visitStringLogic(self, ctx):
        primary:str = self.visit(ctx.stringExpr(0))
        secondary:str = self.visit(ctx.stringExpr(1))
        if ctx.op.type == ScriptoriumParser.EQ:
            return primary == secondary
        elif ctx.op.type == ScriptoriumParser.NEQ:
            return primary != secondary
        elif ctx.op.type == ScriptoriumParser.LT:
            return primary < secondary
        elif ctx.op.type == ScriptoriumParser.GT:
            return primary > secondary
        elif ctx.op.type == ScriptoriumParser.LE:
            return primary <= secondary
        elif ctx.op.type == ScriptoriumParser.GE:
            return primary >= secondary

    def visitNumericLogic(self, ctx):
        primary:float = self.visit(ctx.numericExpr(0))
        secondary:float = self.visit(ctx.numericExpr(1))
        if ctx.op.type == ScriptoriumParser.EQ:
            return primary == secondary
        elif ctx.op.type == ScriptoriumParser.NEQ:
            return primary != secondary
        elif ctx.op.type == ScriptoriumParser.LT:
            return primary < secondary
        elif ctx.op.type == ScriptoriumParser.GT:
            return primary > secondary
        elif ctx.op.type == ScriptoriumParser.LE:
            return primary <= secondary
        elif ctx.op.type == ScriptoriumParser.GE:
            return primary >= secondary

    def visitBoolAnd(self, ctx):
        primary:bool = self.visit(ctx.boolExpr(0))
        secondary:bool = self.visit(ctx.boolExpr(1))
        return primary and secondary

    def visitBoolOr(self, ctx):
        primary:bool = self.visit(ctx.boolExpr(0))
        secondary:bool = self.visit(ctx.boolExpr(1))
        return primary or secondary

    def visitBoolEqual(self, ctx):
        primary:bool = self.visit(ctx.boolExpr(0))
        secondary:bool = self.visit(ctx.boolExpr(1))
        if ctx.op.type == ScriptoriumParser.EQ:
            return primary == secondary
        elif ctx.op.type == ScriptoriumParser.NEQ:
            return primary != secondary

    def visitBoolNot(self, ctx):
        primary:bool = self.visit(ctx.boolExpr())
        return not primary

    # VAR
    
    def visitVariableDefinition(self, ctx):
        def changeOrAppend(list: List[any], index: int, value: any):
            try: var.value[self.recursion_level] = value
            except: var.value.append(value)

        parentCtx = ctx.parentCtx.parentCtx
        parentCtx = parentCtx if type(parentCtx) != ScriptoriumParser.ActionContext else parentCtx.parentCtx

        var: Var = Var.nearestScopeVariable(ctx, self.var_map, self.recursion_level, True)

        value = self.visit(ctx.expr())
        try:
            if var.typeId == ScriptoriumParser.INT_TYPE:
                value = trans if type(value) == str and (trans:=str(value).replace(',', '.')) else value
                changeOrAppend(var.value, self.recursion_level, int(float(value)))
            elif var.typeId == ScriptoriumParser.FLOAT_TYPE:
                value = trans if type(value) == str and (trans:=str(value).replace(',', '.')) else value
                changeOrAppend(var.value, self.recursion_level, float(value))
            elif var.typeId == ScriptoriumParser.STRING_TYPE:
                changeOrAppend(var.value, self.recursion_level, str(value))
            elif var.typeId == ScriptoriumParser.BOOL_TYPE:
                changeOrAppend(var.value, self.recursion_level, bool(value))
        except:
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - type transformation error")

    def visitVarExpr(self, ctx):
        return Var.nearestScopeVariable(ctx, self.var_map, self.recursion_level)
    
    # INPUT

    def visitInputExpr(self, ctx):
        return input(self.visit(ctx.printExpr()))
    
    # FUNCTIONS

    # FIXME: FIXXXXX!!!!!!!

    # IFS
    
    def visitIf(self, ctx):
        if self.visit(ctx.ifBlock().boolExpr()):
            return self.visit(ctx.ifBlock().actionBlock())

        for elseif_ctx in ctx.ifElseBlock():
            if self.visit(elseif_ctx.boolExpr()):
                return self.visit(elseif_ctx.actionBlock())

        if ctx.elseBlock():
            return self.visit(ctx.elseBlock().actionBlock())

    # FOR LOOP

    def visitForLoop(self, ctx):
        var_name = ctx.NAME().getText()
        start = int(ctx.from_.text)
        end = int(ctx.to.text)

        parentCtx = ctx.parentCtx
        self.var_map.setdefault(parentCtx, {})

        if var_name not in self.var_map[parentCtx]:
            self.var_map[parentCtx][var_name] = Var(typeId=ScriptoriumParser.INT_TYPE)

        var: Var = Var.nearestScopeVariable(ctx, self.var_map, self.recursion_level, True)

        for i in range(start, end+1):
            var.value = [i]
            for action in ctx.actionBlock().children:
                try:
                    self.visit(action)
                except Exception as e:
                    if e.args[0]=='break':
                        return
                    elif e.args[0]=='continue':
                        break
                    else:
                        raise e

    # WHILE LOOP

    def visitWhileLoop(self, ctx):
        while(self.visit(ctx.boolExpr())):
            for action in ctx.actionBlock().children:
                try:
                    self.visit(action)
                except Exception as e:
                    if e.args[0]=='break':
                        return
                    elif e.args[0]=='continue':
                        break
                    else:
                        raise e

    # BREAK

    def visitBreakStatement(self, ctx):
        raise Exception("break")
    
    # CONTINUE

    def visitContinueStatement(self, ctx):
        raise Exception("continue")