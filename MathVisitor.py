# Generated from Math.g4 by ANTLR 4.7.2
from antlr4 import *
from MathAst import *
if __name__ is not None and "." in __name__:
    from .MathParser import MathParser
else:
    from MathParser import MathParser

# This class defines a complete generic visitor for a parse tree produced by MathParser.

class MathVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MathParser#compileUnit.
    def visitCompileUnit(self, ctx:MathParser.CompileUnitContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by MathParser#infixExpr.
    def visitInfixExpr(self, ctx:MathParser.InfixExprContext):
        node = InfixExpressionNode()
        if ctx.OP_ADD():
            node.value = '+'
        elif ctx.OP_DIV():
            node.value = '/'
        elif ctx.OP_MUL():
            node.value = '*'
        elif ctx.OP_SUB():
            node.value = '-'
        node.left = self.visit(ctx.left)
        node.right = self.visit(ctx.right)
        return node


    # Visit a parse tree produced by MathParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MathParser.UnaryExprContext):
        if ctx.OP_ADD():
            return self.visit(ctx.expr())
        elif ctx.OP_SUB():
            return NegateNode(self.visit(ctx.expr()))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#funcExpr.
    def visitFuncExpr(self, ctx:MathParser.FuncExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MathParser#numberExpr.
    def visitNumberExpr(self, ctx:MathParser.NumberExprContext):
        return NumberNode(value=int(str(ctx.NUM())))


    # Visit a parse tree produced by MathParser#parensExpr.
    def visitParensExpr(self, ctx:MathParser.ParensExprContext):
        return self.visit(ctx.expr())



del MathParser