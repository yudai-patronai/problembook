
if 'AbstractMonopod' not in dir():
    print("ERROR: No AbstractMonopod class")
    exit()

try:
    a = AbstractMonopod()
    print('ERROR: I can create abstract class')
    exit()
except Exception as e:
    pass

if 'get_hello_text' not in dir(AbstractMonopod):
    print("ERROR: Monopod hasn't `get_hello_text` method.")
    exit()

if 'make_magic' not in dir(AbstractMonopod):
    print("ERROR: Monopod hasn't `make_magic` method.")
    exit()

if '__init__' not in dir(AbstractMonopod):
    print("ERROR: Monopod hasn't initialization method method.")
    exit()
    
print("CORRECT -", sys.a, end="")
