from gi.repository import Gtk

from .tree import view

class Notebook(Gtk.Notebook):
    pass


class Window(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        Gtk.ApplicationWindow.__init__(self, *args, **kwargs)

        notebook = Notebook()

        intro = Gtk.ScrolledWindow()
        box = Gtk.Box()
        label = Gtk.Label()
        label.set_text("Test")
        box.append(label)
        intro.set_child(box)
        tab_label = Gtk.Label()
        tab_label.set_text("Вход")
        notebook.append_page(intro, tab_label)

        tab_label = Gtk.Label()
        tab_label.set_text("Список")
        notebook.append_page(view, tab_label)
        view.show()


        self.set_child(notebook)
        self.show()

        app = kwargs['application']


