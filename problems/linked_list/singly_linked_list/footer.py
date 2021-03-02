
### tests
def test_create_add():
    L = list_create()
    assert L == {'head': None, 'size': 0}, 'Incorrect list_create'

    list_add(L, 'a')
    assert L['size'] == 1, 'wrong size of list'
    assert L['head'].keys() == {'value', 'next'}, 'implentation of node: wrong dict keys'
    assert L['head']['value'] == 'a', 'wrong node value'

    list_add(L, 'b')
    assert L['head']['value'] == 'b', 'list_add does not update head of list'
    assert L['size'] == 2, 'wrong size of list'
    assert L['head']['next']['value'] == 'a', 'list_add lost node'

def test_remove():
    L = list_create()
    list_add(L, 'a')
    list_add(L, 'b')
    list_add(L, 'c')
    list_add(L, 'a')

    x = list_remove(L)
    assert L['size'] == 3, 'wrong size of list'
    assert x == 'a', 'list_remove returned incorrect value'

    list_remove(L)
    list_remove(L)
    list_remove(L)

    assert L == {'head': None, 'size': 0}, 'wrong empty list after removing all items'

def test_search():
    L = list_create()
    list_add(L, 'a')
    list_add(L, 'b')
    list_add(L, 'c')
    list_add(L, 'a')
    assert list_search(L, 'a') == 0, 'wrong list_search'
    list_remove(L)
    assert list_search(L, 'a') == 2, 'wrong list_search'

def test_all():
    test_create_add()
    test_remove()
    test_search()

    L = list_create()

    s = 'abcdefgh'
    for c in reversed(s):
        list_add(L, c)

    for i, c in enumerate(s):
        assert list_search(L, c) == i, 'wrong list_search'

    assert L['size'] == len(s), 'wrong size of list'

    for i, c in enumerate(s):
        assert list_remove(L) == c, 'wrong list_remove'

    assert L == {'head': None, 'size': 0}, 'wrong empty list after removing all items'

### main

test_label = input()

if test_label == 'correctness of `list_create` and `list_add`':
    test_create_add()
elif test_label == 'correctness of `list_remove`':
    test_remove()
elif test_label == 'correctness of `list_search`':
    test_search()
elif test_label == 'correctness of whole interface':
    test_all()
else:
    print('Incorrect test. Call judge.')

print('YES')  # otherwise AssertionError
