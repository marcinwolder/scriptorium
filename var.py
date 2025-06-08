from typing import List, Tuple
from Scriptorium.ScriptoriumParser import ScriptoriumParser


class Var:
    @staticmethod
    def nearest_recursion_level(ctx, var_map):
        """
        Determines the recursion level of the nearest function declaration context.

        This function moves up through the parent contexts of the given `ctx` to locate the nearest
        function declaration context. Once found, it retrieves the recursion level of the
        corresponding function variable from the `var_map`.

        Args:
            ctx: The current context object, typically an instance of a parser context.
            var_map: A dictionary mapping scope contexts to variable mappings. Each variable
                 mapping contains function variables with their associated recursion levels.var_map (dict): A mapping of contexts to their defined variables. 
                      Each key is a context, and each value is a dictionary of variable names to their Var objects.

        Returns:
            int: The recursion level of the nearest function declaration context. If no function
             declaration context is found, returns 0.
        """
        recursion_level = 0
        parent_ctx = ctx
        while parent_ctx is not None:
            if type(parent_ctx) == ScriptoriumParser.FunctionDeclarationContext:
                outer_ctx = Var.nearest_scope(parent_ctx.parentCtx)
                func_var: Func = var_map[outer_ctx][parent_ctx.NAME().getText()]
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
    def nearest_scope_variable(ctx, var_map, return_parent_ctx=False, name="", scope=0):
        """
        Searches for the nearest variable definition in the current or parent scopes.

        Args:
            ctx: The current context object, typically representing a scope or block.
            var_map (dict): A mapping of contexts to their defined variables. 
                            Each key is a context, and each value is a dictionary of variable names to their Var objects.
            return_parent_ctx (bool, optional): If True, returns a tuple containing the variable value and its parent context.
                                                Defaults to False.
            name (str, optional): The name of the variable to search for. If empty, the variable name is extracted from `ctx`.
                                  Defaults to an empty string.
            scope (int, optional): The number of scopes to go back for the search. Used for error reporting purposes.
                                   Defaults to 0.

        Returns:
            The Var object of the nearest variable matching the name in the current or parent scopes.
            If `return_parent_ctx` is True, returns a tuple (variable_object, parent_context).

        Raises:
            Exception: If the variable is not found in the current or parent scopes, an exception is raised with details
                       about the line and column of the context and the scope depth.
        """
        var_name = name if name != "" else ctx.NAME().getText()
        parent_ctx = ctx
        while parent_ctx is not None:
            if parent_ctx in var_map.keys() and \
                var_name in var_map[parent_ctx].keys():
                if return_parent_ctx: return (var_map[parent_ctx][var_name], parent_ctx)
                return var_map[parent_ctx][var_name]
            parent_ctx = parent_ctx.parentCtx
        raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - no variable named \"{var_name}\" was defined"+(f" {scope} scope(s) ago" if scope != 0 else " in current scope"))
    
    @staticmethod
    def nth_nearest_scope(ctx, n):
        """
        Retrieves the nth nearest scope from the given context.

        This function navigates up the scope hierarchy starting from the provided
        context (`ctx`) to find the nth nearest scope. If the requested scope level
        exceeds the available parent scopes, an exception is raised.

        Args:
            ctx: The current context object.
            n (int): The number of scopes to move up from the current context.

        Returns:
            The context object representing the nth nearest scope.

        Raises:
            Exception: If the requested scope level exceeds the available parent
                       scopes, an exception is raised.
        """
        parent_ctx = ctx
        scope_level = n
        while n >= 0:
            if parent_ctx.parentCtx is None:
                raise Exception(f"CULPA: linea {ctx.start.line}:{ctx.start.column} - cannot move {scope_level} scope(s) ago - no such scope defined")
            parent_ctx = Var.nearest_scope(parent_ctx.parentCtx)
            n -= 1
        return parent_ctx

    @staticmethod
    def nearest_scope(ctx):
        """
        Determines the nearest enclosing scope for a given context.
        This function traverses the parent contexts of the given `ctx` object
        until it finds a context that matches one of the predefined scope types.
        If no matching scope is found, it returns the topmost parent context.
        Args:
            ctx: The current context object.
        Returns:
            The nearest enclosing scope context object that matches one of the
            predefined scope types.
        """
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
    
class Func(Var):
    def __init__(self, type_id: int, return_type: int, function_ctx, declaration_position: Tuple[int, int]):
        super().__init__(type_id, declaration_position)
        self.return_type = return_type
        self.function_ctx = function_ctx
        self.recursion_level = -1
    
    def __str__(self):
        return f"<Func: typeId={self.type_id}, functionCtx={self.function_ctx.__repr__()}, returnType={self.return_type}>"
    
class ParamVar(Var):
    def __str__(self):
        return f"<ParamVar: typeId={self.type_id}, value={self.value}>"
