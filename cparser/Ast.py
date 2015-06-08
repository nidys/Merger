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

class DefineInclude(Unit):
    def __init__(self, firstpart, whiteSpace, secondPart):
        self.firstpart = firstpart
        self.whiteSpace = whiteSpace
        self.secondPart = secondPart

    def __str__(self):
        return self.firstpart + self.whiteSpace + self.secondPart

    def __eq__(self, other):
        if isinstance(other, DefineInclude):
            return self.firstpart == other.firstpart and self.secondPart == other.secondPart
        return False

    def getLen(self):
        return len(self.firstpart + self.whiteSpace + self.secondPart)

    @staticmethod
    def getThis(line):
        m = re.match(r'(#include)(\s*)(\S+)',line)
        if m:
            return DefineInclude(m.group(1), m.group(2), m.group(3))
        return None


if __name__ == '__main__':
    u = Unit('u')
    d1 = DefineInclude('a', 'b', 'c')
    d2 = DefineInclude('a', 'b', 'c')
    print d1 == d2
    print d1 == u