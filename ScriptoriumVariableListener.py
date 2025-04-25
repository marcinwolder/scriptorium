from Scriptorium.ScriptoriumListener import ScriptoriumListener

from var import Var

class VariableListener(ScriptoriumListener):
    var_map = {} # {parentCtx -> {var_name -> Var(type, value[])}}

    def __init__(self, var_map):
        self.var_map = var_map
        super().__init__()

    def exitVariableDeclaration(self, ctx):
        self.var_map.setdefault(ctx.parentCtx.parentCtx, {})

        varNameNode = ctx.NAME() if ctx.NAME() else ctx.variableDefinition().NAME()

        if varNameNode.getText() in self.var_map[ctx.parentCtx.parentCtx].keys():
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - multiple variable \"{varNameNode.getText()}\" declaration")
        else:
            self.var_map[ctx.parentCtx.parentCtx][varNameNode.getText()] = Var(typeId=ctx.varType.type)

    def exitFuncParam(self, ctx):
        self.var_map.setdefault(ctx.parentCtx, {})

        varNameNode = ctx.NAME()

        if varNameNode.getText() in self.var_map[ctx.parentCtx].keys():
            raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - multiple variable \"{varNameNode.getText()}\" declaration")
        else:
            self.var_map[ctx.parentCtx][varNameNode.getText()] = Var(typeId=ctx.varType.type)
