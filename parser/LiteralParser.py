import os
import sys
import re

class LiteralParser(object):
    def getWhisteSpaceSeparated(self, value):
        match = re.search(r'[ \t\n]*', value)
        if match:
            wSpacesLength = len(match.group())
            return value[:wSpacesLength],value[wSpacesLength:]
        return '', value

    def parse(self, sourceCode):
        pass



# if __name__ == '__main__':
#     try:
#         fileName = os.getcwd()[:-6] + os.sep + 'inputs' + os.sep + '1.c'
#         print "Usage: python source_file[default= %s]" % fileName
#         if len(sys.argv) > 1:
#             fileName = sys.argv[1]
#         fd = open(fileName, "r")
#         programAst = Parser(fileName).parseFile(fd.read())
#         fd.close()
#         print "Success, translated = %s" % programAst
#     except Exception as e:
#         print "Failure:" +str(e)
#     print "Good byte..."