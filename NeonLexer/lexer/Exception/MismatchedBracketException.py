class MismatchedBracketException(Exception):
    def __init__(self, error_str = "Mismatched Closing Bracket In Source File!"):
        super().__init__(error_str)