from gi.repository import Gtk

from .tree import view

class Notebook(Gtk.Notebook):
    pass


class Confirmation(Gtk.MessageDialog):
    def __init__(self):
        Gtk.MessageDialog.__init__(self)
        self.set_markup('<b>Вы уверены?</b>')
        self.add_button('да', 1)
        self.add_button('нет', 0)
        #  'Действительно выйти?'


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

        self.app = kwargs['application']

        self.connect('close-request', self.handle_exit)

    def handle_exit(self, _):
        dialog = Confirmation() # прицепил к классу метод __del__, первый объект умирает на второй
                                # попытке выйти. Т.е. течь не должно, но чуть лишней памяти держит
        dialog.set_transient_for(self)
        dialog.show()
        dialog.connect('response', self.exit)
        return True

    def exit(self, widget, response):
        # print(widget, response)
        if response == 1:
            self.app.quit()
        widget.destroy()

