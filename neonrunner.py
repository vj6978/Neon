import sys
from NeonLexer.lang.utility.filecharreader import fileCharReader
from NeonLexer.lang.lexer.lexer import NeonLexer

lexer = NeonLexer()
print(*lexer(fileCharReader(sys.argv[1])), sep="\n")