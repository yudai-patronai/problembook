
if 'AbstractMonopod' not in dir():
    print("ERROR: No AbstractDragon class")
    exit()

try:
    a = AbstractMonopod()
    print('ERROR: I can create abstract class')
    exit()
except Exception as e:
    pass

if 'get_hello_text' not in dir(AbstractMonopod):
    print("ERROR: Dragon hasn't `get_intro_text` method.")
    exit()

if 'make_magic' not in dir(AbstractMonopod):
    print("ERROR: Dragon hasn't `make_action` method.")
    exit()

if '__init__' not in dir(AbstractMonopod):
    print("ERROR: Dragon hasn't initialization method method.")
    exit()
    
print("CORRECT -", sys.a, end="")
