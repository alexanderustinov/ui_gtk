import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

from .widgets import Window

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        Gtk.Application.__init__(self, *args, **kwargs)
        win = Window(application=self)
        win.set_default_size(400, 300)
        win.set_title("Embedding in GTK4")
        win.show()
        self.win = win


app = Application(application_id='org.matplotlib.examples.EmbeddingInGTK4')
app.run(None)