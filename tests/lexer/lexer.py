import unittest
from NeonLexer.lexer.lexer.lexer import NeonLexer
from NeonLexer.lexer.utility.filecharreader import fileCharReader

class TestLexicalAnalysis(unittest.TestCase):

    def setUp(self):
        self.lexer = NeonLexer()
        self.input = "lexer_test.txt"
        self.expected_output = [('identifier', 'x'), ('=', ''), ('number', '5'), ('operator', '+'), ('number', '10.9'),
        (';', ''), ('reserved', 'if'), ('identifier', 'x'), ('reserved', 'matches'), ('number', '15'), ('{', ''), ('reserved', 'print'),
        ('identifier', 'x'), (';', ''), ('}', ''), ('reserved', 'else'), ('{', ''), ('reserved', 'print'), ('identifier', 'x'),
        ('operator', '+'), ('number', '10'), (';', ''), ('}', '')]

    def test_lexicalAnalysis(self):
        self.output = self.lexer(fileCharReader(self.input))
        try:
            while value := next(self.output):
                self.expected_output.remove(value)
        except StopIteration:
            self.assertEqual(self.expected_output.__len__(), 0)