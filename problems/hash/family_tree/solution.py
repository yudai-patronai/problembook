def parents(tree, name):
    return tree.get(name, set())

def grandparents(tree, name):
    parents_set = parents(tree, name)
    gp = set()
    for prnt in parents_set:
        gp.update(parents(tree, prnt))
    return gp

def children(tree, name):
    chld = set()
    for k in tree:
        if name in parents(tree, k):
            chld.add(k)
    return chld

def grandchildren(tree, name):
    gchld = set()
    for child in children(tree, name):
        gchld.update(children(tree, child))
    return gchld        

def siblings(tree, name):
    sibs = set()
    for p in parents(tree, name):
        sibs.update(children(tree, p))
    if sibs:  # если цикл запустился, нужно удалить name
        sibs.remove(name)
    return sibs
