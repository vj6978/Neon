from NeonLexer.lexer.lexer import NeonLexer
from NeonLexer.utility.filecharreader import fileCharReader
from NeonParser.parser.rdparser.rdparser import RDParser

"""
    Recursive Descent and LL(1) Top Down parser_dir
"""

class NeonParser:
    def __init__(self):
        self.lexer = NeonLexer()
        self.rdparser = RDParser()

    def __call__(self, source):
        self.parse(self.lexer(fileCharReader(source)))

    def parse(self, token_stream):
        self.rdparser(token_stream)

