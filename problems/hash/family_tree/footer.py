
# tests are here

# error messages
message_template = 'Error: function `{}` is incorrect'
parents_error = message_template.format('parents(tree, name)')
grandparents_error = message_template.format('grandparents(tree, name)')
children_error = message_template.format('children(tree, name)')
grandchildren_error = message_template.format('grandchildren(tree, name)')
siblings_error = message_template.format('siblings(tree, name)')

#####
##### parents(tree, name)
#####

for name in ('C', 'D'):
    assert parents(__TREE, name) == {'A', 'B'}, parents_error

assert parents(__TREE, 'F') == {'C', 'E'}, parents_error

for name in ('G', 'H', 'I'):
    assert parents(__TREE, name) == {'D'}, parents_error

for name in ('A', 'B', 'E', 'J'):
    assert parents(__TREE, name) == set(), parents_error

#####
##### grandparents(tree, name)
#####

for name in ('F', 'G', 'H', 'I'):
    assert grandparents(__TREE, name) == {'A', 'B'}, grandparents_error

assert grandparents(__TREE, 'K') == {'D'}, grandparents_error

for name in ('A', 'B', 'C', 'E', 'D', 'J'):
    assert grandparents(__TREE, name) == set(), grandparents_error

#####
##### children(tree, name)
#####

for name in ('A', 'B'):
    assert children(__TREE, name) == {'C', 'D'}, children_error

for name in ('E', 'C'):
    assert children(__TREE, name) == {'F'}, children_error

assert children(__TREE, 'D') == {'G', 'H', 'I'}, children_error

for name in ('I', 'J'):
    assert children(__TREE, name) == {'K'}, children_error

for name in ('F', 'G', 'H', 'K'):
    assert children(__TREE, name) == set(), children_error

#####
##### grandchildren(tree, name)
#####

for name in ('A', 'B'):
    assert grandchildren(__TREE, name) == {'F', 'G', 'H', 'I'}, grandchildren_error

assert grandchildren(__TREE, 'D') == {'K'}, grandchildren_error

for name in ('E', 'C', 'G', 'H', 'J', 'K'):
    assert grandchildren(__TREE, name) == set(), grandchildren_error

#####
##### siblings(tree, name)
#####

assert siblings(__TREE, 'C') == {'D'}, siblings_error
assert siblings(__TREE, 'D') == {'C'}, siblings_error

assert siblings(__TREE, 'G') == {'H', 'I'}, siblings_error
assert siblings(__TREE, 'H') == {'G', 'I'}, siblings_error
assert siblings(__TREE, 'I') == {'H', 'G'}, siblings_error

for name in ('A', 'B', 'E', 'F', 'J', 'K'):
    assert siblings(__TREE, name) == set(), siblings_error


# all tests are passed
print('YES')
