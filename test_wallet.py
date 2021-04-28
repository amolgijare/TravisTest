"""
This is test program to learn pytest module
This will test wallet function
"""
# test_wallet.py
# https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest

import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet()

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    '''Test wallet with zero initial balance'''
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    '''Test wallet with 20 initial balance'''
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    '''Test add cash function'''
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    '''Test spend cash function'''
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    '''Test insufficient amount exception'''
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)

@pytest.mark.parametrize("earned,spent,expected", [
    (30, 10, 20),
    (20, 2, 18),
])
def test_transactions(empty_wallet, earned, spent, expected):
    '''Test transactions function'''
    my_wallet = empty_wallet
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
