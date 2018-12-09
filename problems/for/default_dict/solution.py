class PrefixClass(object):
    def __init__(self):
        self.run = 0
    def __call__(self):
        global PREFIX
        self.run += 1
        if PREFIX:
            return '>>{}>>'.format(self.run)
        return ''