from typing import List
from Scriptorium.ScriptoriumParser import ScriptoriumParser


class Var:
    @staticmethod
    def change_or_append_value(var, recursion_level, value):
        try: var.value[recursion_level] = value
        except: var.value.append(value)

    @staticmethod
    def nearest_scope_variable(ctx, var_map, recursion_level, insert_mode=False):
        parent_ctx = ctx
        while (parent_ctx := parent_ctx.parentCtx) is not None:
            if parent_ctx in var_map.keys() and \
                ctx.NAME().getText() in var_map[parent_ctx].keys():
                if insert_mode: return var_map[parent_ctx][ctx.NAME().getText()]
                if type(var_map[parent_ctx][ctx.NAME().getText()]) == FuncVar:
                    return var_map[parent_ctx][ctx.NAME().getText()]
                if len(var_map[parent_ctx][ctx.NAME().getText()].value) < recursion_level+1:
                    raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - variable named \"{ctx.NAME().getText()}\" is not yet defined")
                return var_map[parent_ctx][ctx.NAME().getText()].value[recursion_level]
        raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - no variable named \"{ctx.NAME().getText()}\"")

    @staticmethod
    def nearest_scope(ctx):
        parent_ctx = ctx
        while parent_ctx.parentCtx is not None:
            if type(parent_ctx) in [
                ScriptoriumParser.IfBlockContext, 
                ScriptoriumParser.IfElseBlockContext, 
                ScriptoriumParser.ElseBlockContext, 
                ScriptoriumParser.ForLoopContext, 
                ScriptoriumParser.WhileLoopContext, 
                ScriptoriumParser.FunctionDeclarationContext,
                ScriptoriumParser.StartContext
            ]:
                break
            parent_ctx = parent_ctx.parentCtx
        return parent_ctx

    type_id: int
    value: List[any]

    def __init__(self, type_id: int):
        self.type_id = type_id
        self.value = []

    def __str__(self):
        return f"<typeId={self.type_id}, value={self.value}>"
    
    def __repr__(self):
        return self.__str__()
    
class FuncVar(Var):
    def __init__(self, type_id: int, return_type: int, function_ctx):
        super().__init__(type_id)
        self.return_type = return_type
        self.function_ctx = function_ctx
    
    def __str__(self):
        return f"<typeId={self.type_id}, value={self.value}, returnType={self.return_type}>"