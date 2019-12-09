from MathAst import *

class EvaluateExpressionVisitor():
    def visit(self, node):
        if type(node) == InfixExpressionNode:
            if node.value == '+':
                return self.visit(node.left) + self.visit(node.right)
            elif node.value == '-':
                return self.visit(node.left) - self.visit(node.right)
            elif node.value == '*':
                return self.visit(node.left) * self.visit(node.right)
            elif node.value == '/':
                return self.visit(node.left) / self.visit(node.right)
        elif type(node) == NumberNode:
            return node.value
        elif type(node) == NegateNode:
            return node.value
