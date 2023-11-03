import sys
from javalex import MyLexer
from javaparse import MyParser



data  = sys.stdin.read()
myLexer = MyLexer()
lexer = myLexer.build()
parser = MyParser(myLexer)
parser.build(lexer)
parser.test(data)