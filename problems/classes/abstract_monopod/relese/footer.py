class AbstractMonopod(metaclass = abc.ABCMeta):
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


if 'InvisibleMonopod' not in dir():
    print("ERROR: I can't find InvisibleMonopod in solution.")
    exit()

if 'CuteMonopod' not in dir():
    print("ERROR: I can't find CuteMonopod in solution.")
    exit()

if issubclass(InvisibleMonopod, AbstractMonopod):
    print("ERROR: InvisibleMonopod class is not child of AbstractDragon class.")
    exit()

if issubclass(CuteMonopod, AbstractMonopod):
    print("ERROR: CuteMonopod class is not child of AbstractDragon class.")
    exit()

try:
    b = CuteMonopod('sam')
    g = InvisibleMonopod('mik')
except Exception as e:
    print('ERROR: Failed create object :', e)
    exit()

try:
    assert b.make_magic(2) == -2
    assert b.make_magic(3) == -3
except:
    print("ERROR: in make_magic of cute monopod", e)
    exit()

try:
    assert g.make_magic(2) == 4
    assert g.make_magic(3) == 9
except:
    print("ERROR: in make_magic of invisible monopod", e)
    exit()

try:
    assert g.name == "mik"
    assert b.name == "sam"
except:
    print("Wrong name information in variable.")
    exit();

try:
    assert InvisibleMonopod.status == "invisible"
    assert CuteMonopod.status == "cute"
except:
    print("Wrong status information in class.")
    exit();

try:
    assert g.get_hello_text() == "Hello, my name is mik. I'm Invisible squared monopod."
    assert b.get_hello_text() == "Hello, my name is sam. I'm Cute negative monopod."
except:
    print("Wrong intro text.0")0
    exit();  
             

print("CORRECT", end="")
    