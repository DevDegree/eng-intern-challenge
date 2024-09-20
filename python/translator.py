import sys
from braileParser import BraileParser
from textParser import TextParser

arguments = sys.argv[1:]
argumentsString = " ".join(arguments)

if BraileParser.isBraileString(argumentsString):
    braileParser = BraileParser(argumentsString)
    print(braileParser.braileToText())
else:
    textParser = TextParser(argumentsString)
    print(textParser.textToBraile())


        

    