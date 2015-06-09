from Ast import *

def indexOfFirstChar(str):
    return len(str) - len(str.lstrip())
#
def skipToAfterNextLine(lines, code):
    newLineIdx = code.index('\n')
    lines.append(Unit(code[:newLineIdx]))
    return code[newLineIdx+1:]

# def skipToAfterNextLine(lines, code):
#     newLineIdx = code.index('\n')
#     fragment = code[:newLineIdx]
#     #print '#' + fragment + '#'
#     lines.append(Unit(fragment))
#     return (fragment, code[newLineIdx+1:])
#
# def skipNextLines(lines, code):
#     (fragment, code) = skipToAfterNextLine(lines, code)
#     while containsOnlyWhiteSpaces(fragment) == True:
#         (fragment, code) = skipToAfterNextLine(lines, code)
#     return code
#
# def containsOnlyWhiteSpaces(fragment):
#     m = re.match(r'^\s+$', fragment)
#     if m:
#         return True
#     return False

def addMacroInclude(lines, code):
    tmp = MacroInclude.getThis(code)
    if tmp != None:
        lines.append(tmp)
        return (True, code[tmp.getLen()+1:])
    return (False, code)

def addMacroDefine(lines, code):
    tmp = MacroDefine.getThis(code)
    if tmp != None:
        lines.append(tmp)
        return (True, code[tmp.getLen()+1:])
    return (False, code)


