__author__ = 'Janek'
from gtkcodebuffer import CodeBuffer, SyntaxLoader

def setCodeTextFromFile(codeView, filename=None):
    if filename is not None:
        print "File choosen: ", filename
        lang = SyntaxLoader("c")
        buff = CodeBuffer(lang=lang)
        codeView.set_buffer(buff)
        str = ""
        with open(filename, 'r') as fin:
            str += fin.read()
        buff.set_text(str)
    else:
        codeView.get_buffer().set_text("")

def saveToFile(filename, str):
    if not filename.endswith('.c'):
        filename += ".c"
    with open(filename, 'w') as file_:
        file_.write(str)
    print "saved: " + filename