import pytest


class Bank:
    def __init__(self):
        self.amount = 0

    def deposit(self, money):
        self.amount += money

    def deposit_twice(self, money):
        self.amount += money

    def withdraw(self, money):
        if money > self.amount:
            raise NotMoney('Nie masz kasy!')

        self.amount -= money

        return self.amount


class NotMoney(Exception):
    pass


class TestBank:
    def test_not_enought_money(self):
        with pytest.raises(NotMoney):
            bank = Bank()
            bank.withdraw(200)

    def test_create_bank(self):
        bank = Bank()
        assert bank.amount == 0
        assert isinstance(bank, Bank)

    def test_deposit(self):
        bank = Bank()

        bank.deposit(100)

        assert bank.amount == 100

    def test_deposit_twice(self):
        bank = Bank()

        bank.deposit_twice(100)
        bank.deposit_twice(100)


        assert bank.amount == 200


    def test_withdraw(self):
        bank = Bank()

        bank.deposit(100)
        bank.withdraw(50)

        assert bank.amount == 50


