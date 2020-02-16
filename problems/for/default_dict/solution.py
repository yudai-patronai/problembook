class PrefixClass(object):
    def __init__(self, PREFIX):
        self.run = 0
        self.PREFIX = PREFIX

    def __call__(self):
        self.run += 1
        if self.PREFIX:
            return '>>{}>>'.format(self.run)
        return ''
