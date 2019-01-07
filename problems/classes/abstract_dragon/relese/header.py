import math
import abc

class AbstractDragon(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_intro_text(self):
        pass

    @abc.abstractmethod
    def make_action(self):
        pass