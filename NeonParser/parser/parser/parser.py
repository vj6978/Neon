from NeonLexer.lexer.lexer.lexer import NeonLexer
from NeonLexer.lexer.utility.filecharreader import fileCharReader
from NeonParser.grammar.FirstFollowSetGenerator import Generator

"""
    Recursive Descent Top Down parser
"""
class NeonParser:
    def __init__(self):
        self.lexer = NeonLexer()
        self.generator = Generator()

    def __call__(self, source):
        self.generateFirstAndFollowSet()
        self.parse(self.lexer(fileCharReader(source)))

    def generateFirstAndFollowSet(self):
        firstFollowSet = self.generator.generate()
        print(firstFollowSet)

    def parse(self, token_stream):
        pass