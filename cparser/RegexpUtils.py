from Ast import *


def indexOfFirstChar(str):
    return len(str) - len(str.lstrip())

def getSplitedByNextLine(code):
    newLineIdx = code.index('\n')
    fragment = code[:newLineIdx]
    return (fragment, code[newLineIdx + 1:])


def filterWhiteSpaces(code):
    whiteSpaces = ''
    fragment = None
    while True:
        (fragment, code) = getSplitedByNextLine(code)
        if containsOnlyWhiteSpaces(fragment) and len(code) > 0:
            whiteSpaces += ('\n' if fragment == '' else fragment)
        else:
            break
    return (whiteSpaces + fragment, code)


def skipNextLines(lines, code):
    (fragment, code) = filterWhiteSpaces(code)
    lines.append(Unit(fragment))
    return code


def containsOnlyWhiteSpaces(fragment):
    m = re.match(r'^\s+$', fragment)
    if m or fragment == '':
        return True
    return False


def addMacroInclude(lines, code):
    tmp = MacroInclude.getThis(code)
    if tmp != None:
        lines.append(tmp)
        return (True, code[tmp.getLen() + 1:])
    return (False, code)


def addMacroDefine(lines, code):
    tmp = MacroDefine.getThis(code)
    if tmp != None:
        lines.append(tmp)
        return (True, code[tmp.getLen() + 1:])
    return (False, code)

def addSimpleDefinition(lines, code):
    tmp = EmbeddedSimpleVariableDeclaration.getThis(code)
    if tmp != None:
        lines.append(tmp)
        return (True, code[tmp.getLen() + 1:])
    return (False, code)

def addFunctionFirstBuckle(lines, code):
    tmp = FunctionFirstBracerDetector.getThis(code)
    if tmp != None:
        lines.append(tmp)
        return (True, code[tmp.getLen() + 1:])
    return (False, code)
