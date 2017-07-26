import abc


class MyABC(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def do_something(self):
         pass

    @property
    def some_property(self):
        return 1

