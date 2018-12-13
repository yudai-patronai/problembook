import math
import abc

class AbstractOnefootman(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_hello_text(self):
        pass

    @abc.abstractmethod
    def make_magic(self):
        pass

class GreenDragon(AbstractDragon):

    color = "Green"
    def __init__(self, name):
        self.name = name

    def get_intro_text(self):
        return "Hello, my name is " + self.name + ". I'm " + self.color + " squared dragon."

    def make_action(self, x):
        return x*x

class BlueDragon(AbstractDragon):

    color = "Blue"
    def __init__(self, name):
        self.name = name

    def get_intro_text(self):
        return "Hello, my name is " + self.name + ". I'm "+ self.color + " negative dragon."

    def make_action(self, x):
        return -x