from NeonLexer.lexer.lexer.lexer import NeonLexer
from NeonLexer.lexer.utility.filecharreader import fileCharReader

"""
    Recursive Descent LL(1) Top Down parser
"""


class NeonParser:
    def __init__(self):
        self.lexer = NeonLexer()

    def __call__(self, source):
        return self.lexer(fileCharReader(source))

    def parse(self, token_stream):
        pass
