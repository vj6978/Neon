class UnrecognizedCharacterException(Exception):
    def __init__(self, error_str):
        super().__init__("Neon is unable to recognize this character - " + error_str)