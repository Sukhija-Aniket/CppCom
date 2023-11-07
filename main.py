import sys
from cpplex import MyLexer
from cppparse import MyParser

data  = sys.stdin.read()
myLexer = MyLexer()
lexer = myLexer.build()
parser = MyParser(myLexer)
parser.build(lexer)
parser.test(data)