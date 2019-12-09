class NumberNode():
    def __init__(self, value=None):
        self.value = value

class NegateNode():
    def __init__(self, node):
        self.value = -1 * node.value

class InfixExpressionNode():
    def __init__(self, left=None, right=None, value=None):
        self.value = value
