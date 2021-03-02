def list_create():
    L = {
        'head': None,
        'size': 0
    }
    return L

def list_node(value):
    node = {
        'value': value,
        'next': None
    }
    return node

def list_add(L, value):
    new_head = list_node(value)
    old_head = L['head']

    new_head['next'] = old_head
    L['head'] = new_head
    L['size'] += 1

def list_remove(L):
    if L['size'] == 0:
        return None

    old_head = L['head']
    new_head = old_head['next']
    L['head'] = new_head
    L['size'] -= 1

    return old_head['value']

def list_search(L, value):
    if L['size'] == 0:
        return -1

    node = L['head']
    i = 0
    while node is not None:
        if node['value'] == value:
            return i
        node = node['next']
        i += 1
    return -1
