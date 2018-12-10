
if 'GreenDragon' not in dir():
    print("ERROR: I can't find GreenDragon in solution.")
    exit()

if 'BlueDragon' not in dir():
    print("ERROR: I can't find BlueDragon in solution.")
    exit()

if GreenDragon not in AbstractDragon.__subclasses__():
    print("ERROR: GreenDragon class is not child of AbstractDragon class.")
    exit()

if BlueDragon not in AbstractDragon.__subclasses__():
    print("ERROR: BlueDragon class is not child of AbstractDragon class.")
    exit()

try:
    b = BlueDragon('sam')
    g = GreenDragon('mik')
except Exception as e:
    print('ERROR: I can not create class :', e)
    exit()

try:
    assert b.make_action(2) == -2
    assert b.make_action(3) == -3
except:
    print("ERROR: in make_action Blue dragon", e)
    exit()

try:
    assert g.make_action(2) == 4
    assert g.make_action(3) == 9
except:
    print("ERROR: in make_action Green dragon", e)
    exit()

try:
    assert g.name == "mik"
    assert b.name == "sam"
except:
    print("Wrong name information in variable.")
    exit();

try:
    assert GreenDragon.color == "Green"
    assert BlueDragon.color == "Blue"
except:
    print("Wrong color information in class.")
    exit();

try:
    assert g.get_intro_text() == "Hello, my name is mik. I'm Green squared dragon."
    assert b.get_intro_text() == "Hello, my name is sam. I'm Blue negative dragon."
except:
    print("Wrong intro text.")
    exit();


print("CORRECT", end="")
