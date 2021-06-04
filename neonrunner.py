from NeonParser.parser.parser.parser import NeonParser


class NeonRunner:
    def __init__(self, source):
        self.parser = NeonParser()
        self.source = source

    def __call__(self):
        return self.parser(self.source)
