
if 'AbstractDragon' not in dir():
    print("ERROR: No AbstractDragon class")
    exit()

try:
    a = AbstractDragon()
    print('ERROR: I can create abstract class')
    exit()
except Exception as e:
    pass

if 'get_intro_text' not in dir(AbstractDragon):
    print("ERROR: Dragon hasn't `get_intro_text` method.")
    exit()

if 'make_action' not in dir(AbstractDragon):
    print("ERROR: Dragon hasn't `make_action` method.")
    exit()

if '__init__' not in dir(AbstractDragon):
    print("ERROR: Dragon hasn't initialization method method.")
    exit()
    
print("CORRECT", end="")
