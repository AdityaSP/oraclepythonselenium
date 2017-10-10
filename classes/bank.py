''' My Bank software'''
class Account(object):
    def __init__(self, n, b, t):
        self.n = n
        self.b = b
        self.t = t
    def __repr__(self):
        return 'Account({},{})'.format(self.n, self.b)
    def __str__(self):
        return '[Account -> {},{}]'.format(self.n, self.b)
