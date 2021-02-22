# the __TREE is
#
# `+` means married pair
# `/` and `\` mean parent-child relationship (parent is above child on diagram)
#
#       A + B
#       /  \
# E + C     D
#  \ /     /| \
#   F     G H  I + J
#               \ /
#                K

__TREE = {
    'C': set(['A', 'B']),
    'D': set(['A', 'B']),
    'F': set(['E', 'C']),
    'G': set(['D']),
    'H': set(['D']),
    'I': set(['D']),
    'K': set(['I', 'J'])
}
