from lib.testgen import TestSet
from lib.random import randint
from lib.random import sample

allnames = ['Ella-Mai', 'Wyatt', 'Dilan', 'Alexandros',
         'Davey', 'Kamal', 'Connah', 'Amit', 'Kiki',
         'Klara', 'Konnor', 'Elina', 'Myrtle', 'Derek',
         'Koby', 'Albert', 'Silas', 'Lola-Rose', 'Janae',
         'Nataniel', 'Elin', 'Jaxson', 'John-Paul', 'Asa',
         'Savannah', 'Vlad', 'Shanae', 'Ronan', 'Jim',
         'Aamir', 'Zubair', 'Yu', 'Ikrah', 'Kealan',
         'Taylor', 'Merlin', 'Kaiden', 'Shana', 'Mujtaba',
         'Jemimah', 'Dominykas', 'Aaliyah', 'Emma', 'Zoe',
         'Reagan', 'Mylee', 'Imogen', 'Saarah', 'Rita',
         'Mica', 'Malakai', 'Edie', 'Romilly', 'Micheal',
         'Danielius', 'Julius', 'Laith', 'Danyaal', 'Sade',
         'Helen', 'Cordelia', 'Selena', 'Zakir', 'Kane',
         'Isadora', 'Lennox', 'Kristie', 'Wil', 'Kieren',
         'Aden', 'Keyaan', 'Marcelina', 'Kamile', 'Effie',
         'Betsy', 'Tomas', 'Berat', 'Alice', 'Cooper', 'Fox',
         'Aman', 'Khalil', 'Agata', 'Iga', 'Alysia', 'Valentino',
         'Kasper', 'Daniyal', 'Akash', 'Chanel', 'Kaya', 'Ivo', 'Isla',
         'Cara', 'Leena', 'Glyn', 'Zunaira', 'Paddy', 'Stefania', 'Lleyton']

def random_names(alln, size):
    return sample(alln, size)


def random_zeros(nam):
    n =len(nam)
    return [randint(0, 1) for _ in range(n)]


def question(n, bul, arrnam, arliar, m):
    string = str(n) + " " + str(bul) + "\n"
    for i in range(n):
        string += arrnam[i] + ' ' + str(arliar[i]) + "\n"
    string+= str(m) + "\n"
    return string

def answer(n, bul, arrnam, arliar, m):
    s = ''
    i = 0
    for j in range (m):
        if arliar[i] == 0:
            bul = (bul + 1) % 2
            if bul == 1:
                arliar[i] = 1
                i += 1
                i = i % len(arrnam)
            else:
                i += 1
                i = i % len(arrnam)
        else:
            if bul == 0:
                del arliar[i]
                del arrnam[i]
            else:
                i += 1
                i = i % len (arrnam)
            if len(arrnam) == 1:
                break
    for _ in range(len (arliar)):
        s+= arrnam[_] + ' ' + str(arliar[_]) +"\n"
    return s


tests = TestSet()
for size  in [5, 10, 15, 20]:
    arrnam = random_names(allnames, size)
    n = size
    arliar = random_zeros(arrnam)
    bul = random_zeros(arrnam)[0]
    m = randint(14)
    tests.add(
        question(n, bul, arrnam, arliar, m),
        answer(n, bul, arrnam, arliar, m)
    )
