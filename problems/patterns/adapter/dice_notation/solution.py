class RandomiserAdapter:

    def __init__(self, randomiser):
        self.rnd = randomiser

    def dice_res(self, dice):
        _lst = [int(x) for x in dice.split("d")]
        _lst.append(1)
        return _lst[:2]

    def generate_result(self, dice_seq):
        dice_lst = [self.dice_res(i) for i
                    in dice_seq.replace(" ", "").split("+")]
        return self.rnd.generate_by_seq(dice_lst)
