from typing import List, Tuple
from Scriptorium.ScriptoriumParser import ScriptoriumParser


class Var:
    @staticmethod
    def nearest_recursion_level(ctx, var_map):
        recursion_level = 0
        parent_ctx = ctx
        while parent_ctx is not None:
            if type(parent_ctx) == ScriptoriumParser.FunctionDeclarationContext:
                outer_ctx = Var.nearest_scope(parent_ctx.parentCtx)
                func_var: FuncVar = var_map[outer_ctx][parent_ctx.NAME().getText()]
                recursion_level = func_var.recursion_level
                break
            parent_ctx = parent_ctx.parentCtx
        return recursion_level
    
    def change_or_append_value(self, recursion_level, value):
        try: self.value[recursion_level] = value
        except: 
            while recursion_level+1 > len(self.value):
                self.value.append(None)
            self.value[recursion_level] = value

    @staticmethod
    def nearest_scope_variable(ctx, var_map, return_parent_ctx=False):
        parent_ctx = ctx
        while parent_ctx is not None:
            if parent_ctx in var_map.keys() and \
                ctx.NAME().getText() in var_map[parent_ctx].keys():
                if return_parent_ctx: return (var_map[parent_ctx][ctx.NAME().getText()], parent_ctx)
                return var_map[parent_ctx][ctx.NAME().getText()]
            parent_ctx = parent_ctx.parentCtx
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
    declaration_position: Tuple[int, int]

    def __init__(self, type_id: int, declaration_position: Tuple[int, int]):
        self.type_id = type_id
        self.value = []
        self.declaration_position = declaration_position

    def __str__(self):
        return f"<Var: typeId={self.type_id}, value={self.value}>"
    
    def __repr__(self):
        return self.__str__()
    
class FuncVar(Var):
    def __init__(self, type_id: int, return_type: int, function_ctx, declaration_position: Tuple[int, int]):
        super().__init__(type_id, declaration_position)
        self.return_type = return_type
        self.function_ctx = function_ctx
        self.recursion_level = -1
    
    def __str__(self):
        return f"<FuncVar: typeId={self.type_id}, value={self.value}, returnType={self.return_type}>"
    
class ParamVar(Var):
    def __str__(self):
        return f"<ParamVar: typeId={self.type_id}, value={self.value}>"
