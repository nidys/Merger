from Ast import *
from RegexpUtils import *

class LiteralParser(object):
    def __init__(self, sourceCode):
        # print(sourceCode)
        self.parse(sourceCode)
        self.lineNo = 0;

    def getBlock(self):
        if self.hasNextBlock():
            unitLine = self.lines[self.lineNo]
            self.lineNo += 1
            return unitLine
        return ''

    def getRest(self):
        result = ''
        if self.hasNextBlock():
            result = str(self.getBlock())
        while self.hasNextBlock():
            result += '\n' + str(self.getBlock())
        return result

    def hasNextBlock(self):
        return self.lineNo < len(self.lines)

    def parse(self, code):
        firtChar = indexOfFirstChar(code)
        whiteSpaces = code[:firtChar]
        code = code[firtChar:]

        lines = whiteSpaces.split('\n')
        self.lines = []
        for i in range(len(lines)):
            self.lines.append(Unit(lines[i]))
        #######################################

        while len(code) > 0:
            (result, tmpCode) = addMacroInclude(self.lines, code)
            if(result == True):
                code = tmpCode
                continue
            (result, tmpCode) = addMacroDefine(self.lines, code)
            if(result == True):
                code = tmpCode
                continue

            code = skipToAfterNextLine(self.lines, code)
