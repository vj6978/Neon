from abc import ABC

"""
    To store integer literal like 1.0
"""
class LiteralExpr:
    def __init__(self, value):
        self.value = value

"""
    To store variable name literal like abc
"""
class VariableExpr:
    def __init__(self, varName):
        self.variableName = varName

"""
    To store binary operations like x+y
"""
class BinaryOp:
    def __init__(self, op, left, right):
        self.value = (op, left, right)

"""
    To store print operations like x+7
"""
class PrintOp:
    def __init__(self, value):
        self.value = value