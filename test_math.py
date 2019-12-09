import sys
from antlr4 import *
from MathLexer import MathLexer
from MathParser import MathParser
from MathVisitor import MathVisitor
from EvaluateExpressionVisitor import EvaluateExpressionVisitor
def main(argv):
    while True:
        text = InputStream(input(">"))
        lexer = MathLexer(text)
        stream = CommonTokenStream(lexer)
        parser = MathParser(stream)
        tree = parser.compileUnit()
        ast = MathVisitor().visitCompileUnit(tree)
        value = EvaluateExpressionVisitor().visit(ast)
        print('=', value)

if __name__ == '__main__':
    main(sys.argv)