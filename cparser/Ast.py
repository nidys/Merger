import re


class Unit(object):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return str(self.line)

    def __eq__(self, other):
        if isinstance(other, Unit):
            return self.line.lstrip() == other.line.lstrip()
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


class EmbeddedSimpleVariableDeclaration(Unit):
    def __init__(self, ws1, type, ws2, name, ws3, myOperator, ws4, value, ws5, end):
        self.ws1 = ws1
        self.type = type
        self.ws2 = ws2
        self.name = name
        self.ws3 = ws3
        self.myOperator = myOperator
        self.ws4 = ws4
        self.value = value
        self.ws5 = ws5
        self.end = end

    def __str__(self):
        return self.ws1 + self.type + self.ws2 + self.name + \
               self.ws3 + self.myOperator + self.ws4 + \
               self.value + self.ws5 + self.end


    def __eq__(self, other):
        if isinstance(other, EmbeddedSimpleVariableDeclaration):
            return self.type == other.type and \
                   self.name == other.name and \
                   self.myOperator == self.myOperator and \
                   self.value == self.value
        return False


    def getLen(self):
        return len(self.ws1 + self.type + self.ws2 + self.name + \
                   self.ws3 + self.myOperator + self.ws4 + \
                   self.value + self.ws5 + self.end)

    @staticmethod
    def getThis(line):
        m = re.match(r'(\s+)(int|double|float|long|char)(\s+)(\S+)(;)', line)
        if m:
            return EmbeddedSimpleVariableDeclaration(m.group(1), m.group(2), \
                                                     m.group(3), m.group(4), '', '', '', '', '', m.group(5))
        m = re.match(r'(\s+)(int|double|float|long|char)(\s+)(\S+)(\s+)(=)(\s+)(\S+)(;)', line)
        if m:
            return EmbeddedSimpleVariableDeclaration(m.group(1), m.group(2), \
                                                     m.group(3), m.group(4), m.group(5), m.group(6), \
                                                     m.group(7), m.group(8), '', m.group(9))
        return None

############### TODO delete this
if __name__ == '__main__':
    # u = Unit('u')
    # d1 = MacroInclude('a', 'b', 'c')
    # d2 = MacroInclude('a', 'b', 'c')
    # print d1 == d2
    # print d1 == u
    # print MacroDefine.getThis('#define ab')

    t = 'double   da;'
    m = re.match(r'(int|double|float|long|char)(\s+)(\S+)(;)', t)
    if m: print '#' + m.group() + '#'
    print 'koniec'
