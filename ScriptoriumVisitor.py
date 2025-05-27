import math
import re
from typing import List
import difflib

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
        return self.visit(ctx.printExpr(0))+' '+self.visit(ctx.printExpr(1))        
    
    def visitExprInPrint(self, ctx):
        return str(self.visit(ctx.expr()))

    # CAST

    def visitCastedValue(self, ctx):
        if ctx.functionInvocation():
            value = self.visit(ctx.functionInvocation())
        elif ctx.varExpr():
            value = self.visit(ctx.varExpr())
        else:
            value = ctx.getChild(0).getText()
        return cast_to_type(value, ctx.type_.type)
    
    def visitCastedAgain(self, ctx):
        value = self.visit(ctx.castedExpr())
        return cast_to_type(value, ctx.type_.type)

    # STRING

    def visitString(self, ctx):
        text = ctx.STRING().getText()[1:-1]
        text = text.replace("\\\\", "\\")
        text = text.replace("\\\"", "\"")
        return text

    def visitStringAdd(self, ctx):
        return self.visit(ctx.stringExpr(0))+self.visit(ctx.stringExpr(1))

    def visitStringWithVar(self, ctx):
        text = ctx.STRING_WITH_VAR().getText()[1:-1]
        text = text.replace("\\\\", "\\").replace("\\\"", "\"")
        
        def replace_var(match):
            var_name = match.group(1)
            parent_ctx = Var.nearest_scope(ctx)
            if var_name not in self.var_map.get(parent_ctx, {}):
                similar_vars = [name for name in self.var_map.get(parent_ctx, {}).keys()
                               if self.levenshtein(var_name, name) <= 2]
                suggestion = f". Did you mean to use one of these variables: {', '.join(similar_vars)}?" if similar_vars else ""
                raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - variable \"{var_name}\" was not declared{suggestion}")
            recursion_level = Var.nearest_recursion_level(parent_ctx, self.var_map)
            if len(self.var_map[parent_ctx][var_name].value) < recursion_level + 1:
                raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - variable \"{var_name}\" was not initialized")
            return str(self.var_map[parent_ctx][var_name].value[recursion_level])
        
        result = re.sub(r'\{([a-z_]+[a-zA-Z0-9_]*)\}', replace_var, text)
        return result

    def levenshtein(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein(s2, s1)
        if len(s2) == 0:
            return len(s1)
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        return previous_row[-1]

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

    def visitParentVariableDefinition(self, ctx):
        scope_level = len(ctx.PARENT())
        parent_level_ctx = Var.nth_nearest_scope(ctx, scope_level)
        self.visitVariableDefinition(ctx.variableDefinition(), scope_ctx=parent_level_ctx, scope_level=scope_level)

    def visitVariableDefinition(self, ctx, scope_ctx=None, scope_level=0):
        (var, parent_ctx) = Var.nearest_scope_variable(scope_ctx if scope_ctx is not None else ctx, self.var_map, return_parent_ctx=True, name=ctx.NAME().getText(), scope=scope_level)
        recursion_level = Var.nearest_recursion_level(parent_ctx, self.var_map)
        value = self.visit(ctx.expr())
        try:
            casted_value = cast_to_type(value, var.type_id)
            var.change_or_append_value(recursion_level, casted_value)
        except Exception as e:
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - type transformation error, {e}")

    def visitVarExpr(self, ctx):
        parent_level_ctx = Var.nth_nearest_scope(ctx, len(ctx.PARENT()))

        try:
            (var, parent_ctx) = Var.nearest_scope_variable(parent_level_ctx, self.var_map, return_parent_ctx=True, name=ctx.NAME().getText(), scope=len(ctx.PARENT()))
            recursion_level = Var.nearest_recursion_level(parent_ctx, self.var_map)
        except Exception as e:
            all_names = list(self.var_map.get(parent_level_ctx, {}).keys())
            suggestion = difflib.get_close_matches(ctx.NAME().getText(), all_names, n=1)
            msg = str(e)
            if suggestion:
                msg += f' (Did you mean "{suggestion[0]}"?)'
            raise Exception(msg)
        
        if len(var.value) < recursion_level+1:
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - variable named \"{ctx.NAME().getText()}\" is not yet defined")
        return var.value[recursion_level]
    
    # INPUT

    def visitInputExpr(self, ctx):
        return input(self.visit(ctx.printExpr())+" ")
    
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
        i = start
        while i <= end:
            var.change_or_append_value(self.recursion_level, i)
            try:
                self.visit(ctx.loopBlock())
            except Exception as e:
                if e.args[0] == 'break':
                    return
                else:
                    raise e
            i += 1

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