class RDParser:

    def identifier_token(self):
        pass

    def start(self):
        token = self.get_next_token()
        if token[0] == "identifier":
            self.identifier_token(self.get_next_token())
        else:
            print("Unexpected token %s!", token)

    def get_next_token(self):
        return next(self.token_stream)

    def __call__(self, token_stream):
        self.token_stream = token_stream
        self.start()
