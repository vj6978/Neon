from NeonLexer.lexer.lexer import NeonLexer
from NeonLexer.utility.filecharreader import fileCharReader

"""
    Recursive Descent and LL(1) Top Down parser_dir
"""


class NeonParser:
    def __init__(self):
        self.lexer = NeonLexer()

    def __call__(self, source):
        self.parse(self.lexer(fileCharReader(source)))

    def parse(self, token_stream):
        for token in token_stream:
            print(token)
