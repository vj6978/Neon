class Stream:
    def __init__(self, iterator):
        self.iterator = iterator
        self.stream = []
        self.curlyBracketStack = []
        self.simpleBracketStack = []
        self.fillStreamProtocol()

    def popFirstFromStream(self):
        if len(self.stream) == 0:
            self.fillStreamProtocol()
        return self.stream.pop(0)

    def peekFirstCharacterInStream(self):
        if self.stream.__len__() > 0:
            return self.stream[0]

    def fillStreamProtocol(self):
        try:
            while character := next(self.iterator):
                if character == ';':
                    break
                elif character == '{':
                    self.curlyBracketStack.append(character)
                elif character == '}':
                    self.curlyBracketStack.pop()
                elif character == '(':
                    self.simpleBracketStack.append(character)
                elif character == ')':
                    self.simpleBracketStack.pop()
                self.stream.append(character)
        except StopIteration:
            self.stream.append("EOF")
            if len(self.curlyBracketStack) !=0 or len(self.simpleBracketStack) != 0:
                raise Exception("Mismatched Bracket!")