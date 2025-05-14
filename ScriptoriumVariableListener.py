from Scriptorium.ScriptoriumListener import ScriptoriumListener
from Scriptorium.ScriptoriumLexer import ScriptoriumLexer

from var import FuncVar, Var

class VariableListener(ScriptoriumListener):
    var_map = {} # {parentCtx -> {var_name -> Var(type, value[])}}

    def __init__(self, var_map):
        self.var_map = var_map
        super().__init__()

    def exitVariableDeclaration(self, ctx):
        scope_ctx = Var.nearest_scope(ctx)
        varNameNode = ctx.NAME() if ctx.NAME() else ctx.variableDefinition().NAME()

        self.var_map.setdefault(scope_ctx, {})
        if varNameNode.getText() in self.var_map[scope_ctx].keys():
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - multiple variable \"{varNameNode.getText()}\" declaration")
        
        self.var_map[scope_ctx][varNameNode.getText()] = Var(type_id=ctx.varType.type)

    def exitFuncParam(self, ctx):
        scope_ctx = Var.nearest_scope(ctx)
        varNameNode = ctx.NAME()
        
        self.var_map.setdefault(scope_ctx, {})
        if varNameNode.getText() in self.var_map[scope_ctx].keys():
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - multiple variable \"{varNameNode.getText()}\" declaration")
        
        self.var_map[scope_ctx][varNameNode.getText()] = Var(type_id=ctx.varType.type)

    def exitFunctionDeclaration(self, ctx):
        scope_ctx = Var.nearest_scope(ctx.parentCtx)
        varNameNode = ctx.NAME()
        
        self.var_map.setdefault(scope_ctx, {})
        if varNameNode.getText() in self.var_map[scope_ctx].keys():
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - multiple variable \"{varNameNode.getText()}\" declaration")
        
        self.var_map[scope_ctx][varNameNode.getText()] = FuncVar(type_id=ScriptoriumLexer.FUNCTION, return_type=ctx.varType.type, function_ctx=ctx)
