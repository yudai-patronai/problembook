import math
import abc

class AbstractMonopod(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_hello_text(self):
        pass

    @abc.abstractmethod
    def make_magic(self):
        pass

class GreenDragon(AbstractMonopod):

    color = "Green"
    def __init__(self, name):
        self.name = name

    def get_hello_text(self):
        return "Hello, my name is " + self.name + ". I'm " + self.color + " squared dragon."

    def make_magic(self, x):
        return x*x

class BlueDragon(AbstractMonopod):

    color = "Blue"
    def __init__(self, name):
        self.name = name

    def get_hello_text(self):
        return "Hello, my name is " + self.name + ". I'm "+ self.color + " negative dragon."

    def make_magic(self, x):
        return -x