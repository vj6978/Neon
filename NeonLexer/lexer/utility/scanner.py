import re
from ..tokens.reserved_keywords import keywords
from ..tokenRegex import tokenRegex

class Scanner:
    def __init__(self, stream):
        self.s = stream

    def getString(self, delimiter):
        current = ""
        while symbol := self.s.popFirstFromStream():
            if symbol and symbol != delimiter:
                current = current + symbol
            elif symbol == delimiter:
                break
        return "string", current

    def getIdentifier(self, current):
        pattern_matcher = re.compile(tokenRegex.permitted_identifier)
        while self.s.peekFirstCharacterInStream() and pattern_matcher.match(self.s.peekFirstCharacterInStream()):
            current = current + self.s.popFirstFromStream()
        if current in keywords:
            return "reserved", current
        return "identifier", current

    def getNumber(self, current):
        pattern_matcher = re.compile(tokenRegex.permitted_number)
        while self.s.peekFirstCharacterInStream() and pattern_matcher.match(self.s.peekFirstCharacterInStream()):
            current = current + self.s.popFirstFromStream()
        else:
            if current.count('.') > 1:
                raise Exception("Number Format Exception!")
        return "number", current
