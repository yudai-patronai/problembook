import abc

abc.a = input()

class AbstractOnefootman(metaclass = abc.ABCMeta):
	_origin = 1
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_hello_text(self):
        pass

    @abc.abstractmethod
    def make_magic(self):
        pass