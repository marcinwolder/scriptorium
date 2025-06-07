# Generated from d:/Repositories/TKK/Scriptorium/Scriptorium.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ScriptoriumParser import ScriptoriumParser
else:
    from ScriptoriumParser import ScriptoriumParser

# This class defines a complete listener for a parse tree produced by ScriptoriumParser.
class ScriptoriumListener(ParseTreeListener):

    # Enter a parse tree produced by ScriptoriumParser#start.
    def enterStart(self, ctx:ScriptoriumParser.StartContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#start.
    def exitStart(self, ctx:ScriptoriumParser.StartContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#action.
    def enterAction(self, ctx:ScriptoriumParser.ActionContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#action.
    def exitAction(self, ctx:ScriptoriumParser.ActionContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#templateString.
    def enterTemplateString(self, ctx:ScriptoriumParser.TemplateStringContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#templateString.
    def exitTemplateString(self, ctx:ScriptoriumParser.TemplateStringContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#templatePart.
    def enterTemplatePart(self, ctx:ScriptoriumParser.TemplatePartContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#templatePart.
    def exitTemplatePart(self, ctx:ScriptoriumParser.TemplatePartContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#interpolation.
    def enterInterpolation(self, ctx:ScriptoriumParser.InterpolationContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#interpolation.
    def exitInterpolation(self, ctx:ScriptoriumParser.InterpolationContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#expr.
    def enterExpr(self, ctx:ScriptoriumParser.ExprContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#expr.
    def exitExpr(self, ctx:ScriptoriumParser.ExprContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#varExpr.
    def enterVarExpr(self, ctx:ScriptoriumParser.VarExprContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#varExpr.
    def exitVarExpr(self, ctx:ScriptoriumParser.VarExprContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#CastedAgain.
    def enterCastedAgain(self, ctx:ScriptoriumParser.CastedAgainContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#CastedAgain.
    def exitCastedAgain(self, ctx:ScriptoriumParser.CastedAgainContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#CastedValue.
    def enterCastedValue(self, ctx:ScriptoriumParser.CastedValueContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#CastedValue.
    def exitCastedValue(self, ctx:ScriptoriumParser.CastedValueContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#StringCast.
    def enterStringCast(self, ctx:ScriptoriumParser.StringCastContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#StringCast.
    def exitStringCast(self, ctx:ScriptoriumParser.StringCastContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#StringAdd.
    def enterStringAdd(self, ctx:ScriptoriumParser.StringAddContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#StringAdd.
    def exitStringAdd(self, ctx:ScriptoriumParser.StringAddContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#String.
    def enterString(self, ctx:ScriptoriumParser.StringContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#String.
    def exitString(self, ctx:ScriptoriumParser.StringContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#StringFunc.
    def enterStringFunc(self, ctx:ScriptoriumParser.StringFuncContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#StringFunc.
    def exitStringFunc(self, ctx:ScriptoriumParser.StringFuncContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#StringVar.
    def enterStringVar(self, ctx:ScriptoriumParser.StringVarContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#StringVar.
    def exitStringVar(self, ctx:ScriptoriumParser.StringVarContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericFunc.
    def enterNumericFunc(self, ctx:ScriptoriumParser.NumericFuncContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericFunc.
    def exitNumericFunc(self, ctx:ScriptoriumParser.NumericFuncContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericPow.
    def enterNumericPow(self, ctx:ScriptoriumParser.NumericPowContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericPow.
    def exitNumericPow(self, ctx:ScriptoriumParser.NumericPowContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericVar.
    def enterNumericVar(self, ctx:ScriptoriumParser.NumericVarContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericVar.
    def exitNumericVar(self, ctx:ScriptoriumParser.NumericVarContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericAddSub.
    def enterNumericAddSub(self, ctx:ScriptoriumParser.NumericAddSubContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericAddSub.
    def exitNumericAddSub(self, ctx:ScriptoriumParser.NumericAddSubContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericFloat.
    def enterNumericFloat(self, ctx:ScriptoriumParser.NumericFloatContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericFloat.
    def exitNumericFloat(self, ctx:ScriptoriumParser.NumericFloatContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericCast.
    def enterNumericCast(self, ctx:ScriptoriumParser.NumericCastContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericCast.
    def exitNumericCast(self, ctx:ScriptoriumParser.NumericCastContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericPlusMinus.
    def enterNumericPlusMinus(self, ctx:ScriptoriumParser.NumericPlusMinusContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericPlusMinus.
    def exitNumericPlusMinus(self, ctx:ScriptoriumParser.NumericPlusMinusContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericMulDiv.
    def enterNumericMulDiv(self, ctx:ScriptoriumParser.NumericMulDivContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericMulDiv.
    def exitNumericMulDiv(self, ctx:ScriptoriumParser.NumericMulDivContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericInt.
    def enterNumericInt(self, ctx:ScriptoriumParser.NumericIntContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericInt.
    def exitNumericInt(self, ctx:ScriptoriumParser.NumericIntContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericBrackets.
    def enterNumericBrackets(self, ctx:ScriptoriumParser.NumericBracketsContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericBrackets.
    def exitNumericBrackets(self, ctx:ScriptoriumParser.NumericBracketsContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericMod.
    def enterNumericMod(self, ctx:ScriptoriumParser.NumericModContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericMod.
    def exitNumericMod(self, ctx:ScriptoriumParser.NumericModContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#Int.
    def enterInt(self, ctx:ScriptoriumParser.IntContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#Int.
    def exitInt(self, ctx:ScriptoriumParser.IntContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#Float.
    def enterFloat(self, ctx:ScriptoriumParser.FloatContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#Float.
    def exitFloat(self, ctx:ScriptoriumParser.FloatContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#BoolFunc.
    def enterBoolFunc(self, ctx:ScriptoriumParser.BoolFuncContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#BoolFunc.
    def exitBoolFunc(self, ctx:ScriptoriumParser.BoolFuncContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#NumericLogic.
    def enterNumericLogic(self, ctx:ScriptoriumParser.NumericLogicContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#NumericLogic.
    def exitNumericLogic(self, ctx:ScriptoriumParser.NumericLogicContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#BoolCast.
    def enterBoolCast(self, ctx:ScriptoriumParser.BoolCastContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#BoolCast.
    def exitBoolCast(self, ctx:ScriptoriumParser.BoolCastContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#Bool.
    def enterBool(self, ctx:ScriptoriumParser.BoolContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#Bool.
    def exitBool(self, ctx:ScriptoriumParser.BoolContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#StringLogic.
    def enterStringLogic(self, ctx:ScriptoriumParser.StringLogicContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#StringLogic.
    def exitStringLogic(self, ctx:ScriptoriumParser.StringLogicContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#BoolBrackets.
    def enterBoolBrackets(self, ctx:ScriptoriumParser.BoolBracketsContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#BoolBrackets.
    def exitBoolBrackets(self, ctx:ScriptoriumParser.BoolBracketsContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#BoolNot.
    def enterBoolNot(self, ctx:ScriptoriumParser.BoolNotContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#BoolNot.
    def exitBoolNot(self, ctx:ScriptoriumParser.BoolNotContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#BoolOr.
    def enterBoolOr(self, ctx:ScriptoriumParser.BoolOrContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#BoolOr.
    def exitBoolOr(self, ctx:ScriptoriumParser.BoolOrContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#BoolEqual.
    def enterBoolEqual(self, ctx:ScriptoriumParser.BoolEqualContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#BoolEqual.
    def exitBoolEqual(self, ctx:ScriptoriumParser.BoolEqualContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#BoolVar.
    def enterBoolVar(self, ctx:ScriptoriumParser.BoolVarContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#BoolVar.
    def exitBoolVar(self, ctx:ScriptoriumParser.BoolVarContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#BoolAnd.
    def enterBoolAnd(self, ctx:ScriptoriumParser.BoolAndContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#BoolAnd.
    def exitBoolAnd(self, ctx:ScriptoriumParser.BoolAndContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#errorStatement.
    def enterErrorStatement(self, ctx:ScriptoriumParser.ErrorStatementContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#errorStatement.
    def exitErrorStatement(self, ctx:ScriptoriumParser.ErrorStatementContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#funcParam.
    def enterFuncParam(self, ctx:ScriptoriumParser.FuncParamContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#funcParam.
    def exitFuncParam(self, ctx:ScriptoriumParser.FuncParamContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:ScriptoriumParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:ScriptoriumParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#functionInvocation.
    def enterFunctionInvocation(self, ctx:ScriptoriumParser.FunctionInvocationContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#functionInvocation.
    def exitFunctionInvocation(self, ctx:ScriptoriumParser.FunctionInvocationContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#returnStatement.
    def enterReturnStatement(self, ctx:ScriptoriumParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#returnStatement.
    def exitReturnStatement(self, ctx:ScriptoriumParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#whileLoop.
    def enterWhileLoop(self, ctx:ScriptoriumParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#whileLoop.
    def exitWhileLoop(self, ctx:ScriptoriumParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#forLoop.
    def enterForLoop(self, ctx:ScriptoriumParser.ForLoopContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#forLoop.
    def exitForLoop(self, ctx:ScriptoriumParser.ForLoopContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#loopBlock.
    def enterLoopBlock(self, ctx:ScriptoriumParser.LoopBlockContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#loopBlock.
    def exitLoopBlock(self, ctx:ScriptoriumParser.LoopBlockContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#breakStatement.
    def enterBreakStatement(self, ctx:ScriptoriumParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#breakStatement.
    def exitBreakStatement(self, ctx:ScriptoriumParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#continueStatement.
    def enterContinueStatement(self, ctx:ScriptoriumParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#continueStatement.
    def exitContinueStatement(self, ctx:ScriptoriumParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:ScriptoriumParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:ScriptoriumParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#variableDefinition.
    def enterVariableDefinition(self, ctx:ScriptoriumParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#variableDefinition.
    def exitVariableDefinition(self, ctx:ScriptoriumParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#parentVariableDefinition.
    def enterParentVariableDefinition(self, ctx:ScriptoriumParser.ParentVariableDefinitionContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#parentVariableDefinition.
    def exitParentVariableDefinition(self, ctx:ScriptoriumParser.ParentVariableDefinitionContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#if.
    def enterIf(self, ctx:ScriptoriumParser.IfContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#if.
    def exitIf(self, ctx:ScriptoriumParser.IfContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#ifBlock.
    def enterIfBlock(self, ctx:ScriptoriumParser.IfBlockContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#ifBlock.
    def exitIfBlock(self, ctx:ScriptoriumParser.IfBlockContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#ifElseBlock.
    def enterIfElseBlock(self, ctx:ScriptoriumParser.IfElseBlockContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#ifElseBlock.
    def exitIfElseBlock(self, ctx:ScriptoriumParser.IfElseBlockContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#elseBlock.
    def enterElseBlock(self, ctx:ScriptoriumParser.ElseBlockContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#elseBlock.
    def exitElseBlock(self, ctx:ScriptoriumParser.ElseBlockContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#actionBlock.
    def enterActionBlock(self, ctx:ScriptoriumParser.ActionBlockContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#actionBlock.
    def exitActionBlock(self, ctx:ScriptoriumParser.ActionBlockContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#inputExpr.
    def enterInputExpr(self, ctx:ScriptoriumParser.InputExprContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#inputExpr.
    def exitInputExpr(self, ctx:ScriptoriumParser.InputExprContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#print.
    def enterPrint(self, ctx:ScriptoriumParser.PrintContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#print.
    def exitPrint(self, ctx:ScriptoriumParser.PrintContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#PrintAdd.
    def enterPrintAdd(self, ctx:ScriptoriumParser.PrintAddContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#PrintAdd.
    def exitPrintAdd(self, ctx:ScriptoriumParser.PrintAddContext):
        pass


    # Enter a parse tree produced by ScriptoriumParser#ExprInPrint.
    def enterExprInPrint(self, ctx:ScriptoriumParser.ExprInPrintContext):
        pass

    # Exit a parse tree produced by ScriptoriumParser#ExprInPrint.
    def exitExprInPrint(self, ctx:ScriptoriumParser.ExprInPrintContext):
        pass



del ScriptoriumParser