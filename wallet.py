'''
wallet functionality implementation
'''
# wallet.py
class InsufficientAmount(Exception):
    '''
    InsufficientAmount class definition
    '''
    # pass


class Wallet():
    '''
    wallet class definition
    '''
    def __init__(self, initial_amount=0):
        ''' wallet init function'''
        self.balance = initial_amount

    def spend_cash(self, amount):
        ''' wallet spend cash function'''
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        ''' wallet add cash function'''
        self.balance += amount
