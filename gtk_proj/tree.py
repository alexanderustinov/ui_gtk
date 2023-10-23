from enum import Enum

from gi.repository import Gtk

store = Gtk.TreeStore(int, str, str, float)
store.append(None, [0, "Первый", "Первый элемент списка", 0.0])
store.append(None, [1, "Второй", "Второй элемент списка", 0.0])


for el in store:
    print(el[0])
    # store.append(el, [3, "Вложен", "Вложенный элемент", 0.0])
    store.append(el.iter, [3, "Вложен", "Вложенный элемент", 0.0])

view = Gtk.TreeView(model=store)

renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Айди", renderer, text=0)
view.append_column(column)

renderer = Gtk.CellRendererText()
column = Gtk.TreeViewColumn("Текст", renderer, text=1)
view.append_column(column)




# renderer_text = Gtk.CellRendererText()
# column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
# treeview.append_column(column_text)
