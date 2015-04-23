__author__ = 'Janek'

import gtk
from Utils import setCodeTextFromFile, saveToFile

class CMergerUI:

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
        print "Choosen: " + str

    def on_fileChooserOfFirst_file_set(self, widget):
        setCodeTextFromFile(self.builder.get_object("codeViewOfFirst"), widget.get_filename())

    def on_fileChooserOfSecond_file_set(self, widget):
          setCodeTextFromFile(self.builder.get_object("codeViewOfSecond"), widget.get_filename())
    # KONFLKIKTY !!!!!!!!!
    # tag = gtk.TextTag(name="conflict")
    # tag.set_property("background-gdk", gtk.gdk.Color(red=65535, green=32000, blue=32000))
    # buff.get_tag_table().add(tag)
    # offset = buff.get_end_iter().get_offset()
    # buff.insert(buff.get_end_iter(), "\n\ndupdudapadasodadas")
    # buff.apply_tag_by_name("conflict", buff.get_iter_at_offset(offset), buff.get_end_iter())

    def on_firstToolButton_clicked(self, widget):
        print "firstToolButton"

    def on_prevToolButton_clicked(self, widget):
        print "prevToolButton"

    def on_nextToolButton_clicked(self, widget):
        print "nextToolButton"

    def on_lastToolButton_clicked(self, widget):
        print "lastToolButton"

    def on_mergeToolButton_clicked(self, widget):
        self.setToolButtonsActive(True)
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

        self.window.show()

if __name__ == "__main__":
    main = CMergerUI()
    gtk.main()