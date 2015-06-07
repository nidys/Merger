__author__ = 'Janek'

import gtk
import sys
from cparser.Merger import Merger
from Utils import setCodeTextFromFile, saveToFile, getTextFromTextView, setCodeText, addTags, addTextToCodeView, \
    setConflicts, setTag, removeTag, getText

class CMergerUI:

    firstConflicts = []
    secondConflicts = []
    mergerConflicts = []
    currentConflict = 0
    codeView_1 = ''

    def addTags(self, index, tag):
        setTag(self.builder.get_object("codeViewOfFirst"), tag, self.firstConflicts[index]['start'],
               self.firstConflicts[index]['end'])
        setTag(self.builder.get_object("codeViewOfSecond"), tag, self.secondConflicts[index]['start'],
               self.secondConflicts[index]['end'])
        setTag(self.builder.get_object("codeViewOfMerged"), tag, self.mergerConflicts[index]['start'],
               self.mergerConflicts[index]['end'])

    def removeTags(self, index, tag):
        removeTag(self.builder.get_object("codeViewOfFirst"), tag, self.firstConflicts[index]['start'],
               self.firstConflicts[index]['end'])
        removeTag(self.builder.get_object("codeViewOfSecond"), tag, self.secondConflicts[index]['start'],
               self.secondConflicts[index]['end'])
        removeTag(self.builder.get_object("codeViewOfMerged"), tag, self.mergerConflicts[index]['start'],
               self.mergerConflicts[index]['end'])

    def on_window1_destroy(self, object, data=None):
        print "quit with cancel"
        gtk.main_quit()

    def on_quit_activate(self, menuitem, data=None):
        print "quit from menu"
        gtk.main_quit()

    def on_codeViewOfFirst_button_release_event(self, textView, e):
        fc = self.builder.get_object("fileChooserOfFirst")
        if fc.get_filename() is None:
            filename = self.chooseFile("open")
            if filename is not None:
                fc.set_filename(filename)
                setCodeTextFromFile(self.builder.get_object("codeViewOfFirst"), filename)
        self.choosenCode("first")

    def on_codeViewOfSecond_button_release_event(self, textView, e):
        fc = self.builder.get_object("fileChooserOfSecond")
        if fc.get_filename() is None:
            filename = self.chooseFile("open")
            if filename is not None:
                fc.set_filename(filename)
                setCodeTextFromFile(self.builder.get_object("codeViewOfSecond"), filename)
        self.choosenCode("second")

    def on_chooseButtonOfFirst_clicked(self, widget):
        self.choosenCode("first")

    def on_chooseButtonOfSecond_clicked(self, widget):
        self.choosenCode("second")

    def choosenCode(self, str):
        if str == 'first':
            start = self.firstConflicts[self.currentConflict]['start']
            end = self.firstConflicts[self.currentConflict]['end']
            print "1: " + getText(self.builder.get_object("codeViewOfFirst"), start, end)
        else:
            start = self.secondConflicts[self.currentConflict]['start']
            end = self.secondConflicts[self.currentConflict]['end']
            print "2: " + getText(self.builder.get_object("codeViewOfSecond"), start, end)

    def on_fileChooserOfFirst_file_set(self, widget):
        setCodeTextFromFile(self.builder.get_object("codeViewOfFirst"), widget.get_filename())

    def on_fileChooserOfSecond_file_set(self, widget):
          setCodeTextFromFile(self.builder.get_object("codeViewOfSecond"), widget.get_filename())

    def on_firstToolButton_clicked(self, widget):
            self.removeTags(self.currentConflict, 'current')
            self.currentConflict = 0
            self.addTags(self.currentConflict, 'current')

    def on_prevToolButton_clicked(self, widget):
        if self.currentConflict - 1 >= 0 :
            self.removeTags(self.currentConflict, 'current')
            self.currentConflict -= 1
            self.addTags(self.currentConflict, 'current')

    def on_nextToolButton_clicked(self, widget):
        if self.currentConflict + 1 < self.firstConflicts.__len__():
            self.removeTags(self.currentConflict, 'current')
            self.currentConflict += 1
            self.addTags(self.currentConflict, 'current')

    def on_lastToolButton_clicked(self, widget):
            self.removeTags(self.currentConflict, 'current')
            self.currentConflict = self.firstConflicts.__len__() - 1
            self.addTags(self.currentConflict, 'current')

    def on_mergeToolButton_clicked(self, widget):
        cv_1 = self.builder.get_object("codeViewOfFirst")
        cv_2 = self.builder.get_object("codeViewOfSecond")
        str_1 = getTextFromTextView(cv_1)
        str_2 = getTextFromTextView(cv_2)
        if str_1 != '' and str_2 != '':
            self.setToolButtonsActive(True)
            setCodeText(cv_1, '')
            setCodeText(cv_2, '')
            merger = Merger()
            mergerView = self.builder.get_object("codeViewOfMerged")
            setCodeText(mergerView, '')
            merger.parseFirst(str_1)
            merger.parserSecond(str_2)

            while merger.hasBothNextBlock():
                if merger.isBlockConflict():
                    self.firstConflicts.append(addTextToCodeView(cv_1, merger.getBlockOfFirst() + '\n'))
                    self.secondConflicts.append(addTextToCodeView(cv_2, merger.getBlockOfSecond() + '\n'))
                    self.mergerConflicts.append(addTextToCodeView(mergerView, '     \n'))
                else:
                    addTextToCodeView(cv_1, merger.getBlockOfFirst() + '\n')
                    addTextToCodeView(cv_2, merger.getBlockOfSecond() + '\n')
                    addTextToCodeView(mergerView, merger.getBlockOfThird() + '\n')
            rest = merger.getRestOfFirstBlock()
            addTextToCodeView(mergerView, rest)
            addTextToCodeView(cv_1, rest)
            rest = merger.getRestOfSecondBlock()
            addTextToCodeView(mergerView, rest)
            addTextToCodeView(cv_2, rest)

            setConflicts(mergerView, self.mergerConflicts)
            setConflicts(cv_1, self.firstConflicts)
            setConflicts(cv_2, self.secondConflicts)
        print "mergeToolButton"

    def setToolButtonsActive(self, active):
        self.builder.get_object("firstToolButton").set_sensitive(active)
        self.builder.get_object("prevToolButton").set_sensitive(active)
        self.builder.get_object("nextToolButton").set_sensitive(active)
        self.builder.get_object("lastToolButton").set_sensitive(active)

    def on_newMenuItem_activate(self, widget):
        self.on_newToolButton_clicked(widget)

    def on_newToolButton_clicked(self, widget):
        self.setToolButtonsActive(False)
        self.builder.get_object("fileChooserOfFirst").unselect_all()
        self.builder.get_object("fileChooserOfSecond").unselect_all()
        setCodeTextFromFile(self.builder.get_object("codeViewOfFirst"))
        setCodeTextFromFile(self.builder.get_object("codeViewOfSecond"))

    def on_saveAsMenuItem_activate(self, arg):
        filename = self.chooseFile("save")
        if filename is not None:
            self.file = filename
            print self.file
            saveToFile(filename, "test")

    def on_saveMenuItem_activate(self, arg):
        if not hasattr(self, 'file'):
            self.on_saveAsMenuItem_activate(arg)
        else:
            saveToFile(self.file, "test2")

    def on_saveToolButton_clicked(self, widget):
        self.on_saveMenuItem_activate(widget)

    def chooseFile(self, action="open"):
        filter = gtk.FileFilter()
        filter.set_name("only c files")
        filter.add_pattern("*.c")
        if action == "save":
            fcd = gtk.FileChooserDialog("Save...",
                 None,
                 gtk.FILE_CHOOSER_ACTION_SAVE,
                 (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE_AS, gtk.RESPONSE_OK))
        else:
            fcd = gtk.FileChooserDialog("Open...",
                 None,
                 gtk.FILE_CHOOSER_ACTION_OPEN,
                 (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        fcd.add_filter(filter)
        self.response = fcd.run()
        filename = fcd.get_filename()
        fcd.destroy()
        if self.response == gtk.RESPONSE_OK:
            return filename
        return

    def __init__(self):
        self.gladefile = "gui.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")

        filter = gtk.FileFilter()
        filter.set_name("only c files")
        filter.add_pattern("*.c")
        self.builder.get_object("fileChooserOfFirst").add_filter(filter)
        self.builder.get_object("fileChooserOfSecond").add_filter(filter)
        addTags(self.builder.get_object("codeViewOfFirst"))
        addTags(self.builder.get_object("codeViewOfSecond"))
        addTags(self.builder.get_object("codeViewOfMerged"))

        self.window.show()

if __name__ == "__main__":
    main = CMergerUI()
    gtk.main()