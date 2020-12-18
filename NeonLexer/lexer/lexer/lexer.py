import re
from NeonLexer.lexer.stream.stream import Stream
from NeonLexer.lexer.utility.scanner import Scanner
from NeonLexer.lexer.tokens import tokens
from NeonLexer.lexer.Exception.MismatchedBracketException import MismatchedBracketException
from NeonLexer.lexer.Exception.UnrecognizedCharacterException import UnrecognizedCharacterException
from NeonLexer.lexer.tokenRegex.tokenRegex import permitted_number, permitted_identifier

class NeonLexer:
    def __init__(self):
        self.curlyBracketStack = []
        self.simpleBracketStack = []

    def __call__(self, fileCharReader):
        s = Stream(fileCharReader)
        scanner = Scanner(s)
        while s.peekFirstCharacterInStream() != "EOF":
            try:
                c = s.stream.pop(0)
                if c in tokens.ignorelist:
                    continue
                elif c == '{':
                    self.curlyBracketStack.append(c)
                elif c == '}':
                    self.curlyBracketStack.pop()
                elif c == '(':
                    self.simpleBracketStack.append(c)
                elif c == ')':
                    self.simpleBracketStack.pop()
                elif c in tokens.operator:
                    yield "operator", c
                elif c in tokens.special_chars:
                    yield c, ""
                elif c in tokens.quotes:
                    yield scanner.getString(c)
                elif re.match(permitted_number, c):
                    yield scanner.getNumber(c)
                elif re.match(permitted_identifier, c):
                    yield scanner.getIdentifier(c)
                else:
                    raise UnrecognizedCharacterException(str(c))
            except IndexError:
                s.fillStreamProtocol()
        if len(self.curlyBracketStack) != 0 or len(self.simpleBracketStack) != 0:
            raise MismatchedBracketException