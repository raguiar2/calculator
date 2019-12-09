# Generated from Math.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete listener for a parse tree produced by MathParser.
class MathListener(ParseTreeListener):

    # Enter a parse tree produced by MathParser#compileUnit.
    def enterCompileUnit(self, ctx:MathParser.CompileUnitContext):
        pass

    # Exit a parse tree produced by MathParser#compileUnit.
    def exitCompileUnit(self, ctx:MathParser.CompileUnitContext):
        pass


    # Enter a parse tree produced by MathParser#infixExpr.
    def enterInfixExpr(self, ctx:MathParser.InfixExprContext):
        pass

    # Exit a parse tree produced by MathParser#infixExpr.
    def exitInfixExpr(self, ctx:MathParser.InfixExprContext):
        pass


    # Enter a parse tree produced by MathParser#unaryExpr.
    def enterUnaryExpr(self, ctx:MathParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by MathParser#unaryExpr.
    def exitUnaryExpr(self, ctx:MathParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by MathParser#funcExpr.
    def enterFuncExpr(self, ctx:MathParser.FuncExprContext):
        pass

    # Exit a parse tree produced by MathParser#funcExpr.
    def exitFuncExpr(self, ctx:MathParser.FuncExprContext):
        pass


    # Enter a parse tree produced by MathParser#numberExpr.
    def enterNumberExpr(self, ctx:MathParser.NumberExprContext):
        pass

    # Exit a parse tree produced by MathParser#numberExpr.
    def exitNumberExpr(self, ctx:MathParser.NumberExprContext):
        pass


    # Enter a parse tree produced by MathParser#parensExpr.
    def enterParensExpr(self, ctx:MathParser.ParensExprContext):
        pass

    # Exit a parse tree produced by MathParser#parensExpr.
    def exitParensExpr(self, ctx:MathParser.ParensExprContext):
        pass


