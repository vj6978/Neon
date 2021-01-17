class Generator:
    # TODO: Need to extract grammar to Grammar file
    def __init__(self):
        self.grammar = {
            "PROGRAM": "STATEMENTS",
            "STATEMENTS": "ASSIGNMENT_STATEMENT",
            "ASSIGNMENT_STATEMENT": "[DATATYPE] ID = NUM | NUM",
            "DATATYPE": "int",
            "ID": "[a_zA_Z0 - 9]",
            "NUM": "[0 - 9]"
        }

    # LL Grammar Sanity Check
    def llGrammarSanityCheck(self):
        self.checkLeftRecursion()
        self.checkLeftFactoring()

    def checkLeftRecursion(self, lhs=None, rhs=None):
        if not lhs and not rhs:
            for key, value in self.grammar.items():
                if value.__contains__("|"):
                    grammar_rule_rhs = value.split("|")
                    for rule in grammar_rule_rhs:
                        self.checkLeftRecursion(key.strip(), rule.strip())
                else:
                    if key.strip() == value.split(" ")[0].strip():
                        raise Exception("Grammar failed sanity check! Left recursion found!")
        else:
            if lhs == rhs:
                raise Exception("Grammar failed sanity check! Left recursion found!")

    def checkLeftFactoring(self):
        pass

    def generate(self):
        self.llGrammarSanityCheck()
