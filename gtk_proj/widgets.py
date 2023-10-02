from gi.repository import Gtk

from matplotlib.backends.backend_gtk4agg import \
    FigureCanvasGTK4Agg as FigureCanvas
from matplotlib.figure import Figure

class Window(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        Gtk.ApplicationWindow().__init__(self, *args, **kwargs)

        fig = Figure(figsize=(5, 4), dpi=100)
        # ax = fig.add_subplot()

        sw = Gtk.ScrolledWindow(margin_top=10, margin_bottom=10,
                            margin_start=10, margin_end=10)

        # self.set_child(sw)

        # canvas = FigureCanvas(fig)
        # canvas.set_size_request(800, 600)
        # sw.set_child(canvas)
        #
        # canvas.show_all()