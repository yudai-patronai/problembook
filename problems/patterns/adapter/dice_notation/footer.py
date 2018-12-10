

class Randomizer:

    def __init__(self)
    
    def generate_by_seq(self, seq):
        _sum = 0
        for (n, mx) in seq:
            _sum += n*mx
        return _sum

def get_dice_res(rnd, dice_seq):
        return ( rnd.generate_result(dice_seq) ** 257 % 337 ) 

rnd = RandomiserAdapter(Randomizer())

print(get_dice_res(rnd, input()))
