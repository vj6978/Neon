import unittest
from NeonLexer.lexer.lexer.lexer import NeonLexer
from NeonLexer.lexer.utility.filecharreader import fileCharReader
from NeonLexer.lexer.Exception.MismatchedBracketException import MismatchedBracketException
from NeonLexer.lexer.Exception.UnrecognizedCharacterException import UnrecognizedCharacterException

class TestLexicalAnalysis(unittest.TestCase):
    def setUp(self):
        self.lexer = NeonLexer()
        self.success_src = "lexer_test_success.txt"
        self.failure_src_curly_bracket = "lexer_test_failure_curly_bracket.txt"
        self.failure_src_unrecognized_char = "lexer_test_unrecognized_character.txt"
        self.expected_output = [('identifier', 'x'), ('=', ''),
                                ('number', '5'), ('operator', '+'),
                                ('number', '10.9'), (';', ''),
                                ('reserved', 'if'), ('identifier', 'x'),
                                ('reserved', 'is'), ('number', '15'),
                                ('reserved', 'print'), ('identifier', 'x'),
                                (';', ''), ('reserved', 'else'),
                                ('reserved', 'print'), ('identifier', 'x'),
                                ('operator', '+'), ('number', '10'), (';', '')]

    def test_lexicalAnalysisSuccess(self):
        self.output = self.lexer(fileCharReader(self.success_src))
        try:
            while value := next(self.output):
                self.expected_output.remove(value)
        except StopIteration:
            self.assertEqual(0, self.expected_output.__len__())

    def test_MismatchedBracketExceptionRaised(self):
        with self.assertRaises(MismatchedBracketException):
            type(*self.lexer(fileCharReader(self.failure_src_curly_bracket)))

    def test_UnrecognizedCharacterExceptionRaised(self):
        with self.assertRaises(UnrecognizedCharacterException):
            type(*self.lexer(fileCharReader(self.failure_src_unrecognized_char)))