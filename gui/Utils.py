__author__ = 'Janek'
from gtkcodebuffer import CodeBuffer, SyntaxLoader
import gtk

def setCodeTextFromFile(codeView, filename=None):
    if filename is not None:
        print "File choosen: ", filename
        fd = open(filename, 'r')
        str = fd.read()
        fd.close()
        setCodeText(codeView, str)
    else:
        codeView.get_buffer().set_text("")

def saveToFile(filename, str):
    if not filename.endswith('.c'):
        filename += ".c"
    with open(filename, 'w') as file_:
        file_.write(str)
    print "saved: " + filename

def getTextFromTextView(codeView):
    buff = codeView.get_buffer()
    return buff.get_text(buff.get_start_iter(), buff.get_end_iter(), True)

def setCodeText(codeView, str):
    lang = SyntaxLoader("c")
    buff = CodeBuffer(lang=lang)
    codeView.set_buffer(buff)
    buff.set_text(str)
    addTags(codeView)

def addTextToCodeView(codeView, str):
    buff = codeView.get_buffer()
    start = buff.get_end_iter().get_offset()
    buff.insert(buff.get_end_iter(), str)
    end = buff.get_end_iter().get_offset()
    return {'start': start, 'end': end}

def addTags(codeView):
    buff = codeView.get_buffer()
    tag = gtk.TextTag(name="conflict")
    tag.set_property("background-gdk", gtk.gdk.Color(red=65535, green=32000, blue=32000))
    buff.get_tag_table().add(tag)

    tag = gtk.TextTag(name="current")
    tag.set_property("background-gdk", gtk.gdk.Color(red=32000, green=65535, blue=32000))
    buff.get_tag_table().add(tag)

def setConflicts(codeView, list):
    buff = codeView.get_buffer()
    for el in list:
        buff.apply_tag_by_name("conflict", buff.get_iter_at_offset(el['start']), buff.get_iter_at_offset(el['end']))

def setTag(codeView, tag, start, end):
    buff = codeView.get_buffer()
    buff.apply_tag_by_name(tag, buff.get_iter_at_offset(start), buff.get_iter_at_offset(end))

def removeTag(codeView, tag, start, end):
    buff = codeView.get_buffer()
    buff.remove_tag_by_name(tag, buff.get_iter_at_offset(start), buff.get_iter_at_offset(end))

def getText(codeView, start, end):
    buff = codeView.get_buffer()
    return buff.get_text(buff.get_iter_at_offset(start), buff.get_iter_at_offset(end))