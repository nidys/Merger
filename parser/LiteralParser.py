class LiteralParser(object):
    def __init__(self, sourceCode):
        # print(sourceCode)
        self.lines = sourceCode.split('\n')
        self.lineNo = 0;

    def getBlock(self):
        if self.hasNextBlock():
            line = self.lines[self.lineNo]
            self.lineNo += 1
            return line
        return ''

    def getRest(self):
        result = ''
        if self.hasNextBlock():
            result = self.getBlock()
        while self.hasNextBlock():
            result += '\n' + self.getBlock()
        return result

    def hasNextBlock(self):
        return self.lineNo < len(self.lines)