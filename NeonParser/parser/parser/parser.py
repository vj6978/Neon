from NeonLexer.lexer.lexer.lexer import NeonLexer as lexer
from NeonLexer.lexer.utility.filecharreader import fileCharReader
"""
    Recursive Descent LL(1) Top Down parser
"""

class NeonParser:
    def __call__(self, source):
        self.parse(lexer(fileCharReader(source)))

    def parse(self, token_stream):
        while val := next(token_stream):
            print("Value {}".format(val))
