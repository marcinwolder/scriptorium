# Generated from d:/Repositories/TKK/Scriptorium/Scriptorium.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ScriptoriumParser import ScriptoriumParser
else:
    from ScriptoriumParser import ScriptoriumParser

# This class defines a complete generic visitor for a parse tree produced by ScriptoriumParser.

class ScriptoriumVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ScriptoriumParser#start.
    def visitStart(self, ctx:ScriptoriumParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#action.
    def visitAction(self, ctx:ScriptoriumParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#templateString.
    def visitTemplateString(self, ctx:ScriptoriumParser.TemplateStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#templatePart.
    def visitTemplatePart(self, ctx:ScriptoriumParser.TemplatePartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#interpolation.
    def visitInterpolation(self, ctx:ScriptoriumParser.InterpolationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#expr.
    def visitExpr(self, ctx:ScriptoriumParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#varExpr.
    def visitVarExpr(self, ctx:ScriptoriumParser.VarExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#CastedAgain.
    def visitCastedAgain(self, ctx:ScriptoriumParser.CastedAgainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#CastedValue.
    def visitCastedValue(self, ctx:ScriptoriumParser.CastedValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#StringCast.
    def visitStringCast(self, ctx:ScriptoriumParser.StringCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#StringAdd.
    def visitStringAdd(self, ctx:ScriptoriumParser.StringAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#String.
    def visitString(self, ctx:ScriptoriumParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#StringFunc.
    def visitStringFunc(self, ctx:ScriptoriumParser.StringFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#StringVar.
    def visitStringVar(self, ctx:ScriptoriumParser.StringVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericFunc.
    def visitNumericFunc(self, ctx:ScriptoriumParser.NumericFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericPow.
    def visitNumericPow(self, ctx:ScriptoriumParser.NumericPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericVar.
    def visitNumericVar(self, ctx:ScriptoriumParser.NumericVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericAddSub.
    def visitNumericAddSub(self, ctx:ScriptoriumParser.NumericAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericFloat.
    def visitNumericFloat(self, ctx:ScriptoriumParser.NumericFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericCast.
    def visitNumericCast(self, ctx:ScriptoriumParser.NumericCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericPlusMinus.
    def visitNumericPlusMinus(self, ctx:ScriptoriumParser.NumericPlusMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericMulDiv.
    def visitNumericMulDiv(self, ctx:ScriptoriumParser.NumericMulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericInt.
    def visitNumericInt(self, ctx:ScriptoriumParser.NumericIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericBrackets.
    def visitNumericBrackets(self, ctx:ScriptoriumParser.NumericBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericMod.
    def visitNumericMod(self, ctx:ScriptoriumParser.NumericModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#Int.
    def visitInt(self, ctx:ScriptoriumParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#Float.
    def visitFloat(self, ctx:ScriptoriumParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#BoolFunc.
    def visitBoolFunc(self, ctx:ScriptoriumParser.BoolFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#NumericLogic.
    def visitNumericLogic(self, ctx:ScriptoriumParser.NumericLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#BoolCast.
    def visitBoolCast(self, ctx:ScriptoriumParser.BoolCastContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#Bool.
    def visitBool(self, ctx:ScriptoriumParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#StringLogic.
    def visitStringLogic(self, ctx:ScriptoriumParser.StringLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#BoolBrackets.
    def visitBoolBrackets(self, ctx:ScriptoriumParser.BoolBracketsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#BoolNot.
    def visitBoolNot(self, ctx:ScriptoriumParser.BoolNotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#BoolOr.
    def visitBoolOr(self, ctx:ScriptoriumParser.BoolOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#BoolEqual.
    def visitBoolEqual(self, ctx:ScriptoriumParser.BoolEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#BoolVar.
    def visitBoolVar(self, ctx:ScriptoriumParser.BoolVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#BoolAnd.
    def visitBoolAnd(self, ctx:ScriptoriumParser.BoolAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#errorStatement.
    def visitErrorStatement(self, ctx:ScriptoriumParser.ErrorStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#funcParam.
    def visitFuncParam(self, ctx:ScriptoriumParser.FuncParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:ScriptoriumParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#functionInvocation.
    def visitFunctionInvocation(self, ctx:ScriptoriumParser.FunctionInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#returnStatement.
    def visitReturnStatement(self, ctx:ScriptoriumParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#whileLoop.
    def visitWhileLoop(self, ctx:ScriptoriumParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#forLoop.
    def visitForLoop(self, ctx:ScriptoriumParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#loopBlock.
    def visitLoopBlock(self, ctx:ScriptoriumParser.LoopBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#breakStatement.
    def visitBreakStatement(self, ctx:ScriptoriumParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#continueStatement.
    def visitContinueStatement(self, ctx:ScriptoriumParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:ScriptoriumParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#variableDefinition.
    def visitVariableDefinition(self, ctx:ScriptoriumParser.VariableDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#parentVariableDefinition.
    def visitParentVariableDefinition(self, ctx:ScriptoriumParser.ParentVariableDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#if.
    def visitIf(self, ctx:ScriptoriumParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#ifBlock.
    def visitIfBlock(self, ctx:ScriptoriumParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#ifElseBlock.
    def visitIfElseBlock(self, ctx:ScriptoriumParser.IfElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#elseBlock.
    def visitElseBlock(self, ctx:ScriptoriumParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#actionBlock.
    def visitActionBlock(self, ctx:ScriptoriumParser.ActionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#inputExpr.
    def visitInputExpr(self, ctx:ScriptoriumParser.InputExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#print.
    def visitPrint(self, ctx:ScriptoriumParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#PrintAdd.
    def visitPrintAdd(self, ctx:ScriptoriumParser.PrintAddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScriptoriumParser#ExprInPrint.
    def visitExprInPrint(self, ctx:ScriptoriumParser.ExprInPrintContext):
        return self.visitChildren(ctx)



del ScriptoriumParser