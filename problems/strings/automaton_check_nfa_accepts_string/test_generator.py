import string
from lib.testgen import TestSet
from lib import random
import math
import queue

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

kTrashState = -1
kInitialState = 0

class Automaton:
    def __init__(self, n_a, n_st):
        self.na = n_a
        self.n = n_st
        self.T = [[set() for _ in range(n_a)] for _ in range(n_st)]
        self.t = [False for i in range(n_st)]
    
    def add_transition(self, sfrom, sto, sc):
        #print(sfrom, sto, sc, ord(sc) - ord('a'))
        self.T[sfrom][ord(sc) - ord('a')].add(sto)
        
    def add_terminal(self, state):
        self.t[state] = True
        
def rand_state(au):
    return random.randrange(0, au.n)

def add_rand_from(au, sfrom):
    au.add_transition(sfrom, rand_state(au), random.choice(ALPHABET[:au.na]))
    
def add_rand_to(au, sto):
    au.add_transition(rand_state(au), sto, random.choice(ALPHABET[:au.na]))
    
def add_rand(au):
    au.add_transition(rand_state(au), rand_state(au), random.choice(ALPHABET[:au.na]))
    
def get_reachable_unreachable(au, start):
    ns = au.n
    unreachable = [True for _ in range(ns)]
    q = queue.Queue()
    
    q.put(start)
    
    while not q.empty():
        state = q.get()
        if unreachable[state]:
            for i in range(au.na):
                for opt in au.T[state][i]: 
                    if unreachable[opt]:
                        q.put(opt)
            unreachable[state] = False
        q.task_done()
    
    return list(filter(lambda i, u=unreachable: not u[i], range(ns))), \
           list(filter(lambda i, u=unreachable: u[i], range(ns))),
       
def make_all_reachable_from(au, start):
    adds = 0
    
    res, urs = get_reachable_unreachable(au, start)
    
    #print("unreachable from", start, ":\t", urs)
    for ur in urs:
        while True:
            from_candidate = random.choice(res)
            # To get an NFA for sure
            from_opts = list(filter(lambda i, col=au.T[from_candidate]: col[i],
                                    range(au.na)))
            if len(from_opts) == 0:
                continue
            
            au.add_transition(from_candidate, ur, chr(ord('a') + random.choice(from_opts)))
            res.append(ur)
            adds += 1
            break
    if adds:
        print("Added ", adds, "\ttransitions for reachability")
     
def make_random_automaton(na = len(ALPHABET), ns=None):
    if ns is None:
        ns = 5 + random.randint(5)
        
    au = Automaton(na, ns)
    
    for i in range(ns):
        for _ in range(max(random.randrange(1, 3), min(na // 10, ns // 10))):
            add_rand_from(au, i)
            
        for _ in range(max(random.randrange(1, 3), min(na // 10, ns // 10))):
            add_rand_to(au, i)
           
    print("Fwd")
    make_all_reachable_from(au, 0)
    print("Rev")
    
    for i in range(max(
        int(math.sqrt(ns)) + 1,
        min(
            random.randrange(3, 7),
            ns // 8)
        )):
        new_terminal = random.randrange(ns)
        au.add_terminal(new_terminal)
        make_all_reachable_from(au, new_terminal)
        
    order = list(range(ns))
    random.shuffle(order)
    for i in order:
        make_all_reachable_from(au, i)
    
    return au



def make_good_string(au, minlen=5):
    parts = []
    state = 0
    
    for i in range(random.randrange(minlen, min(2*minlen, minlen+5))):
        opt = random.choice(list(filter(lambda i, col=au.T[state]: (col[i]) , range(au.na))))
        opt_state = random.choice(list(au.T[state][opt]))
        parts.append(chr(ord('a') + opt))
        state = opt_state
        
    #print(parts)
        
    seen = [None for _ in range(au.n)]
    q = queue.Queue()
    
    q.put(state)
    seen[state] = ''
    done = None
    
    while not q.empty():
        cur = q.get()
        for candidate in range(au.na):
            for other in au.T[cur][candidate]:
                if other == kTrashState:
                    continue
                if seen[other] is not None:
                    continue
                seen[other] = seen[cur] + chr(candidate + ord('a'))
                if au.t[other]:
                    done = other
                    #print("We are done, our champion is ", other, " with string ", seen[other])
                else:
                    q.put(other)
        q.task_done()
        if done is not None:
            #print("We are done, our champion is ", done, " with string ", seen[done])
            while not q.empty():
                _ = q.get()
                q.task_done()
            parts.append(seen[done])
            #print("It's all ogre now", parts)
                
    return "".join(parts)

# Cheap tricks time
# Finding the trash-path explicitly is quite hard
# Instead, we leave the last alphabet char unused
def make_trash_string(au, minlen=5):
    parts = []
    state = 0
        
    for i in range(random.randrange(minlen, min(2*minlen, minlen+5))):
        opt = random.choice(list(filter(lambda i, col=au.T[state]: col[i] , range(au.na))))
        opt_state = random.choice(list(au.T[state][opt]))
        parts.append(chr(ord('a') + opt))
        state = opt_state
        
    parts.append(chr(ord('a') + au.na))
    
    return "".join(parts)


def automaton_to_string(au):
    parts = []
    parts.append("{0} {1}".format(au.na, au.n))
    
    trans = 0
    for f in range(au.n):
        for c in range(au.na):
            # Workaround for alphabet resize, see make_trash_string
            if c >= len(au.T[f]):
                continue
            if au.T[f][c]:
                trans += len(au.T[f][c])
    parts.append(str(trans))
    
    for f in range(au.n):
        for c in range(au.na):
            # Workaround for alphabet resize, see make_trash_string
            if c >= len(au.T[f]):
                continue
            for dst in au.T[f][c]:
                parts.append("{0} {1} {2}".format(f, dst, chr(c + ord('a'))))
                
    parts.append(str(sum(map(int, au.t))))
    parts.append(" ".join(map(str, filter(lambda i, au=au: au.t[i], range(au.n)))))
    
    return "\n".join(map(str, parts))
    

def make_test(alpha_size, n_states, test_sizes):
    au = make_random_automaton(alpha_size, n_states)
    au.na += 1
    statement = [automaton_to_string(au)]
    au.na -= 1
    
    answer = []
    
    statement.append(str(sum(test[1] * 2 for test in test_sizes)))
    
    for minlen, n in test_sizes:
        test_strings = [*((make_good_string(au, minlen), 1) for _ in range(n)),
                        *((make_trash_string(au, minlen), 0) for _ in range(n))
                        ]

        random.shuffle(test_strings)

        statement.append("\n".join(one[0] for one in test_strings))
        answer.append(" ".join(map(str, (one[1] for one in test_strings))))
    
    return "\n".join(statement), " ".join(answer)


tests = TestSet()

tests.add("""1
1

1
0 0 a

1
0

4
a
aa
aaaa
aaaaaaaaaaa""", "1 1 1 1")

tests.add("""1
2

1
0 0 a

1
1

4
a
aa
aaaa
aaaaaaaaaaa""", "0 0 0 0")

tests.add("""2
2

4
0 1 a
1 0 a
0 0 b
1 1 b

1
1

5
abbabbbbabb
bbbbbbabbbb
ababababaab
baaaaaabbbb
aaaaaaaaaaa""", "1 1 0 0 1")

tests.add("""2
3

3
0 1 a
1 2 a
0 2 b

1
2

5
aa
a
b
ba
ab""", "1 0 1 0 0")

tests.add("""3
5

9
0 1 a
0 2 b
0 3 c
1 2 b
3 2 a
2 4 a
4 1 c
1 0 c
3 3 b

2
2 3

7
bacccbb
ccccccc
bacca
bacccbbaaccab
bacb
cbbbbbbbb
abaccacacba""", "1 0 0 1 1 1 0")
tests.add("""2
8

16
0 1 a
1 2 a
2 3 a
3 4 a
0 5 b
5 6 b
6 7 b
1 5 b
2 5 b
3 5 b
5 1 a
6 1 a
4 4 a
4 4 b
7 7 a
7 7 b

2
4 7

20
abaab
abaaa
bbaaabaabb
babbababaabaaa
babbbbabbaaaa
baabaa
bbbabb
bbaaab
bbbaabababbb
baaaaaaaabab
bababababa
abaab
abaababbb
abbbbaa
ababa
abaab
bbababbb
baabbbba
aabaab
baaaa""", "0 0 0 0 1 0 1 0 1 1 0 0 1 1 0 0 1 1 0 1")


tests.add(*make_test(4,  5,    [(5, 5)]    ))
tests.add(*make_test(4,  10,   [(10, 5)]   ))
tests.add(*make_test(4,  20,   [(10, 5)]   ))
tests.add(*make_test(10, 60,  [(20, 5)]   ))
tests.add(*make_test(10, 60,  [(200, 5)]  ))
print("*******************")
tests.add(*make_test(20, 60,  [(10, 5), (20, 5), (2000, 5)] ))
    
