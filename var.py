from typing import List


class Var:
    @staticmethod
    def nearestScopeVariable(ctx, var_map, recursion_level, insert_mode=False):
        parent_ctx = ctx
        while (parent_ctx := parent_ctx.parentCtx) is not None:
            if parent_ctx in var_map.keys() and \
                ctx.NAME().getText() in var_map[parent_ctx].keys():
                if insert_mode: return var_map[parent_ctx][ctx.NAME().getText()]
                if len(var_map[parent_ctx][ctx.NAME().getText()].value) < recursion_level+1:
                    raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - variable named \"{ctx.NAME().getText()}\" is not yet defined")
                return var_map[parent_ctx][ctx.NAME().getText()].value[recursion_level]
        raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - no variable named \"{ctx.NAME().getText()}\"")

    typeId: int
    value: List[any]

    def __init__(self, typeId: int):
        self.typeId = typeId
        self.value = []

    def __str__(self):
        return f"<typeId={self.typeId}, value={self.value}>"
    
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
