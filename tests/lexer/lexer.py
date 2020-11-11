import unittest
from NeonLexer.lexer.lexer.lexer import NeonLexer
from NeonLexer.lexer.utility.filecharreader import fileCharReader

class TestLexicalAnalysis(unittest.TestCase):

    def setUp(self):
        self.lexer = NeonLexer()
        self.input = "lexer_test.txt"
        self.expected_output = [('identifier', 'x'), ('=', ''), ('number', '5'), ('operator', '+'), ('number', '10')]

    def test_lexicalAnalysis(self):
        self.output = self.lexer(fileCharReader(self.input))
        try:
            while val := next(self.output):
                self.assertIn(val, self.expected_output)
        except StopIteration:
            pass