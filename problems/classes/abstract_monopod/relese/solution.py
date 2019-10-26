
class InvisibleMonopod(AbstractMonopod):

    status = "invisible"
    def __init__(self, name):
        self.name = name

    def get_hello_text(self):
        return "Hello, my name is " + self.name + ". I'm Invisible squared monopod."

    def make_magic(self, x):
        return x*x

class CuteMonopod(AbstractMonopod):

    status = "cute"
    def __init__(self, name):
        self.name = name

    def get_hello_text(self):
        return "Hello, my name is " + self.name + ". I'm Cute negative monopod."

    def make_magic(self, x):
        return -x