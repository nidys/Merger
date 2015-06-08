from Ast import *

def indexOfFirstChar(str):
    return len(str) - len(str.lstrip())

def skipToAfterNextLine(lines, code):
    newLineIdx = code.index('\n')
    lines.append(Unit(code[:newLineIdx]))
    return code[newLineIdx+1:]

def addDefineInclude(lines, code):
    tmp = DefineInclude.getThis(code)
    if tmp != None:
        lines.append(tmp)
        return (True, code[tmp.getLen()+1:])
    return (False, code)