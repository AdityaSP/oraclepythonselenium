''' My Bank software'''

class Account(object):
    def __init__(self, n, b, t):
        self.n = n
        self.b = b
        self.t = t
    def debit(self, amount):
        self.b -= amount
        
    def credit(self, amount):
        self.b += amount

class CurrentAccount(Account):
    ''' Current Account Class handles CA'''
    def __init__(self, n, b):
        Account.__init__(self,n,b,'C')

    def __repr__(self):
        return 'CA({},{})'.format(self.n, self.b)

        
class SavingsAccount(Account):
    ''' Base Account Class handles everythin'''
    def __init__(self, n, b):
        Account.__init__(self,n,b,'S')

    def __repr__(self):
        return 'SA({},{})'.format(self.n, self.b)
        
    def debit(self, amount):
        if self.b < amount :
            raise ValueError("Insufficient Balance")
        else :    
            Account.debit(self,amount)
