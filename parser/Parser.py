import os
import sys
import ply.lex as lex
import ply.yacc as yacc
from ast import *

translationUnit = None
# reserved = {
#     'int' : 'INT_TYPE'
# }

reservedTokends = [r'INT_TYPE']

tokens = [r'SCOLON'
          ,r'INT'
          ,r'ID'
          # , r'WHITE_SPACE'
          ] + reservedTokends
         # + list(reserved.values())

t_SCOLON = r';'

def t_INT_TYPE(t):
     r'[ \t]*int'
     return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[ \t]*[a-zA-Z][a-zA-Z_0-9]*'
    return t

def t_newline(t):
    r'\r*\n+'

def t_error(t):
    print('Illegal character')

#################################################################
def p_translation_unit(p):
    """translation_unit : external_decl"""
    global translationUnit
    translationUnit = Translation_unit(p[1])

def p_external_decl(p):
    """external_decl : decl"""
    p[0]= External_decl(decl=p[1])

def p_decl(p):
    """decl : decl_specs SCOLON"""
    p[0] = Decl(decl_specs=p[1])

def p_decl_specs(p):
    """decl_specs : type_spec decl_specs
                  | type_spec"""
    if len(p) == 2:
        p[0] = Decl_specs(type_spec=p[1])
    else:
        p[0] = Decl_specs(type_spec=p[1], second_type_spec=p[2])

def p_type_spec(p):
    """type_spec : INT_TYPE
                 | typedef_name"""
    p[0] = p[1]
    if isinstance(p[1], Typedef_name) == False:
        p[0] = Type_spec(type=p[1])

def p_typedef_name(p):
    """typedef_name : ID"""
    p[0] = Typedef_name(id=p[1])

def p_error(p):
    print("Lexic token problem")
#################################################################
class Parser(object):
    def __init__(self, fileName):
        self._filename = fileName
    def parseFile(self, srcCode):
        try:
            # print srcCode
            lexer = lex.lex(debug=False)
            parser = yacc.yacc(debug=False)
            parser.parse(srcCode, lexer=lexer)
        except Exception as e:
            print e
            raise e


#################################################################
if __name__ == '__main__':
    try:
        fileName = os.getcwd()[:-6] + os.sep + 'inputs' + os.sep + '1.c'
        print "Usage: python source_file[default= %s]" % fileName
        if len(sys.argv) > 1:
            fileName = sys.argv[1]
        fd = open(fileName, "r")
        programAst = Parser(fileName).parseFile(fd.read())
        fd.close()
        global translationUnit
        print "Success, translated = %s" % translationUnit
    except Exception as e:
        print "Failure"
        print e
    print "Good byte..."