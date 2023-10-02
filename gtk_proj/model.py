from random import random


class Plot():
    def __init__(self):
        self._x = []
        self._y = []

    def handle_event(self):
        if len(self._x)>0:
            self._x.append(self._x+1)
        else:
            self._x.append(0)

        self._y.append(random())