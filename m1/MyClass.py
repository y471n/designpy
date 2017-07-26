from m1.MyABC import MyABC


class MyClass(MyABC):
    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        self._myprop *= 2

    @property
    def some_property(self):
        return self._myprop
