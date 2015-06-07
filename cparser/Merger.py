from LiteralParser import LiteralParser

class Merger(object):
    def hasBothNextBlock(self):
        return (self.firstCode.hasNextBlock() and self.secondCode.hasNextBlock())

    def isBlockConflict(self):
        self.firstBlock = self.firstCode.getBlock()
        self.secondBlock = self.secondCode.getBlock()
        return self._isBlockConflict()

    def getBlockOfFirst(self):
        if self._isBlockConflict():
            return self.firstBlock
        return self.firstBlock # ulatwi mi to sporo

    def getBlockOfSecond(self):
        if self._isBlockConflict():
            return self.secondBlock
        return self.secondBlock

    def getBlockOfThird(self):
        if self._isBlockConflict():
            return ''
        return self.firstBlock

    def parseFirst(self, sourceCode):
        self.firstCode = LiteralParser(sourceCode)

    def parserSecond(self, sourceCode):
        self.secondCode = LiteralParser(sourceCode)

    def getRestOfFirstBlock(self):
        return self.firstCode.getRest()

    def getRestOfSecondBlock(self):
        return self.secondCode.getRest()

    def _isBlockConflict(self):
        return (self.firstBlock != self.secondBlock)