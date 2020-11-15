class Stream:
    def __init__(self, iterator):
        self.iterator = iterator
        self.stream = []
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
                self.stream.append(character)
                if character == ';':
                    break
        except StopIteration:
            self.stream.append("EOF")