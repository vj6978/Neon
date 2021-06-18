import re
from NeonLexer.stream.stream import Stream
from NeonLexer.utility.scanner import Scanner
from NeonLexer.tokens import tokens
from NeonLexer.tokenRegex.tokenRegex import permitted_number, permitted_identifier

class NeonLexer:
    def __call__(self, fileCharReader):
        s = Stream(fileCharReader)
        scanner = Scanner(s)
        while s.peekFirstCharacterInStream() != "EOF":
            c = s.stream.pop(0)
            if c in tokens.ignorelist:
                continue
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
                raise Exception("Neon is unable to recognize this character - " + str(c))
            s.fillStreamProtocol()