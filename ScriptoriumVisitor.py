import math
from typing import List

from Scriptorium.ScriptoriumParser import ScriptoriumParser
from Scriptorium.ScriptoriumVisitor import ScriptoriumVisitor
from var import FuncVar, ParamVar, Var

def cast_to_type(value, type_id):
    if type_id == ScriptoriumParser.INT_TYPE:
        return int(float(trans if type(value) == str and (trans:=str(value).replace(',', '.')) else value))
    elif type_id == ScriptoriumParser.FLOAT_TYPE:
        return float(trans if type(value) == str and (trans:=str(value).replace(',', '.')) else value)
    elif type_id == ScriptoriumParser.STRING_TYPE:
        return str(value)
    elif type_id == ScriptoriumParser.BOOL_TYPE:
        return bool(value)
    elif type_id == ScriptoriumParser.NULL:
        return None
    
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
        (var, parent_ctx) = Var.nearest_scope_variable(ctx, self.var_map, return_parent_ctx=True)
        recursion_level = Var.nearest_recursion_level(parent_ctx, self.var_map)
        value = self.visit(ctx.expr())
        try:
            casted_value = cast_to_type(value, var.type_id)
            var.change_or_append_value(recursion_level, casted_value)
        except Exception as e:
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - type transformation error, {e}")

    def visitVarExpr(self, ctx):
        # print("parent lvl:", len(ctx.PARENT()))
        parent_cnt = len(ctx.PARENT())
        parent_level_ctx = ctx
        while parent_cnt >= 0:
            if parent_level_ctx.parentCtx is None:
                raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - variable named \"{ctx.NAME().getText()}\" was not defined {len(ctx.PARENT())} scope(s) ago")
            parent_level_ctx = Var.nearest_scope(parent_level_ctx.parentCtx)
            parent_cnt -= 1
        (var, parent_ctx) = Var.nearest_scope_variable(parent_level_ctx, self.var_map, return_parent_ctx=True, name=ctx.NAME().getText(), scope=len(ctx.PARENT()))
        recursion_level = Var.nearest_recursion_level(parent_ctx, self.var_map)
        if len(var.value) < recursion_level+1:
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - variable named \"{ctx.NAME().getText()}\" is not yet defined")
        return var.value[recursion_level]
    
    # INPUT

    def visitInputExpr(self, ctx):
        return input(self.visit(ctx.printExpr()))
    
    # FUNCTIONS

    def visitFunctionInvocation(self, ctx):
        function_var: FuncVar = Var.nearest_scope_variable(ctx, self.var_map)
        parameters = self.var_map[function_var.function_ctx].values() if function_var.function_ctx in self.var_map.keys() else []
        parameters = [var for var in parameters if type(var) == ParamVar]
        arguments = ctx.expr()
        if len(parameters) != len(arguments):
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - wrong number of arguments - got: {len(arguments)}, expected: {len(parameters)}")
        for param, expr in zip(parameters, ctx.expr()):
            try:
                casted_value = cast_to_type(self.visit(expr), param.type_id)
                recursion_level = Var.nearest_recursion_level(function_var.function_ctx, self.var_map)
                param.change_or_append_value(recursion_level+1, casted_value)
            except Exception as e:
                raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - type transformation error, {e}")
        try:
            function_var.recursion_level += 1
            self.visit(function_var.function_ctx.actionBlock())
            function_var.recursion_level -= 1
        except Exception as e:
            if e.args[0] == 'return':
                function_var.recursion_level -= 1
                return cast_to_type(e.args[1], function_var.return_type)
            raise e

    def visitFunctionDeclaration(self, ctx):
        ...

    def visitReturnStatement(self, ctx):
        result = None
        if (node:=ctx.expr()) is not None:
            result = self.visit(node)
        raise Exception("return", result)

    # IFS
    
    def visitIf(self, ctx):
        if self.visit(ctx.ifBlock().boolExpr()):
            return self.visit(ctx.ifBlock().actionBlock())

        for elseif_ctx in ctx.ifElseBlock():
            if self.visit(elseif_ctx.boolExpr()):
                return self.visit(elseif_ctx.actionBlock())

        if ctx.elseBlock():
            return self.visit(ctx.elseBlock().actionBlock())

    # LOOPS

    def visitBreakStatement(self, ctx):
        raise Exception("break")
    
    def visitContinueStatement(self, ctx):
        raise Exception("continue")

    def visitLoopBlock(self, ctx):
        for action in ctx.actionBlock().children:
            try:
                self.visit(action)
            except Exception as e:
                if e.args[0] == 'continue':
                    return
                else:
                    raise e

    # FOR LOOP

    def visitForLoop(self, ctx):
        start = int(self.visit(ctx.from_))
        end = int(self.visit(ctx.to))

        var: Var = Var.nearest_scope_variable(ctx, self.var_map)

        for i in range(start, end+1):
            var.change_or_append_value(self.recursion_level, i)
            try:
                self.visit(ctx.loopBlock())
            except Exception as e:
                if e.args[0] == 'break':
                    return
                else: 
                    raise e

    # WHILE LOOP

    def visitWhileLoop(self, ctx):
        while(self.visit(ctx.boolExpr())):
            try:
                self.visit(ctx.loopBlock())
            except Exception as e:
                if e.args[0] == 'break':
                    return
                else: 
                    raise e
