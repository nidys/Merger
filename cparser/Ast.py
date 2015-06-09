import re


class Unit(object):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return str(self.line)

    def __eq__(self, other):
        if isinstance(other, Unit):
            return self.line == other.line
        return False

    def getThis(self, line):
        return line

    def getLen(self):
        return len(self.line)


class MacroInclude(Unit):
    defineName = r'#include'

    def __init__(self, firstpart, whiteSpace, secondPart):
        self.beginingWhiteSpace = None
        self.firstpart = firstpart
        self.whiteSpace = whiteSpace
        self.secondPart = secondPart

    def __str__(self):
        tmp = ''
        if self.beginingWhiteSpace != None:
            tmp = self.beginingWhiteSpace
        return tmp + self.firstpart + self.whiteSpace + self.secondPart

    def __eq__(self, other):
        if isinstance(other, MacroInclude):
            return self.firstpart == other.firstpart and self.secondPart == other.secondPart
        return False

    def getLen(self):
        tmpLen = 0
        if self.beginingWhiteSpace != None:
            tmpLen = len(self.beginingWhiteSpace)
        return tmpLen + len(self.firstpart + self.whiteSpace + self.secondPart)

    @staticmethod
    def getThis(line):
        m = re.match(r'(\s+)(' + MacroInclude.defineName + ')(\s*)(\S+)', line)
        if m:
            tmp = MacroInclude(m.group(2), m.group(3), m.group(4))
            tmp.beginingWhiteSpace = m.group(1)
            return tmp
        m = re.match(r'(' + MacroInclude.defineName + ')(\s*)(\S+)', line)
        if m:
            return MacroInclude(m.group(1), m.group(2), m.group(3))
        return None

class MacroDefine(Unit):
    defineName = r'#define'

    def __init__(self, firstpart, whiteSpace, secondPart):
        self.beginingWhiteSpace = None
        self.firstpart = firstpart
        self.whiteSpace = whiteSpace
        self.secondPart = secondPart

    def __str__(self):
        tmp = ''
        if self.beginingWhiteSpace != None:
            tmp = self.beginingWhiteSpace
        return tmp + self.firstpart + self.whiteSpace + self.secondPart

    def __eq__(self, other):
        if isinstance(other, MacroDefine):
            return self.firstpart == other.firstpart and self.secondPart == other.secondPart
        return False

    def getLen(self):
        tmpLen = 0
        if self.beginingWhiteSpace != None:
            tmpLen = len(self.beginingWhiteSpace)
        return tmpLen + len(self.firstpart + self.whiteSpace + self.secondPart)

    @staticmethod
    def getThis(line):
        m = re.match(r'(\s+)(' + MacroDefine.defineName + ')(\s*)(\S+)', line)
        if m:
            tmp = MacroDefine(m.group(2), m.group(3), m.group(4))
            tmp.beginingWhiteSpace = m.group(1)
            return tmp
        m = re.match(r'(' + MacroDefine.defineName + ')(\s*)(\S+)', line)
        if m:
            return MacroDefine(m.group(1), m.group(2), m.group(3))
        return None

############### TODO delete this
if __name__ == '__main__':
    u = Unit('u')
    d1 = MacroInclude('a', 'b', 'c')
    d2 = MacroInclude('a', 'b', 'c')
    print d1 == d2
    print d1 == u
    print MacroDefine.getThis('#define ab')

    t = '\n\n\t\t  \n\n\n'
    m = re.match(r'^\s+$', t)
    if m: print '#' +m.group() + '#'
    t = '\n\n   \t\n\ng\n\n\n'
    m = re.match(r'^\s+$', t)
    if m: print '#' +m.group() + '#'
    print 'koniec'
