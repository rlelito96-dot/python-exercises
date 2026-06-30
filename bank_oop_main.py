
class NordeaAccount():
    def __init__(self, account_number):
        self._balance = 0
        self._account_number = account_number

    @property
    def balance(self):
        return self._balance


    @classmethod
    def create_with_balance(cls, account_number, initial_balance):
        account = cls(account_number)
        account.balance = initial_balance

        return account

    @staticmethod
    def transfer(sender, recipient, amount):
        if sender.balance >= amount:
            sender.balance -= amount
            recipient.balance += amount
            print()
            print("Communicat from Hiba: send me your money!")
            print("-------------------------------------------")
            print("Money:", amount,"$ has been sended from:", sender.account_number, "to:", recipient.account_number)
            print("-------------------------------------------")
            print("Your account balance after transaction is:", sender.balance, "$")

        else:
            print("You dont have enought money to complete this transaction!")


    @balance.setter
    def balance(self, value):
        if value < 0:
            print("You can not!")
            return
        self._balance = value

        # print("Warrning!")


    @balance.deleter
    def balance(self):
        print("You are blocked!")

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number != value

    @account_number.deleter
    def account_number(self):
        print("You are stopped!")


Hiba_account = NordeaAccount.create_with_balance("999888777666", 1000000)


Rafal_account = NordeaAccount.create_with_balance("3333333333333333333", 20)

NordeaAccount.transfer(Rafal_account, Hiba_account, 10 )

print("-------------------------------------------")

print("Hiba account balance after transaction is:", Hiba_account.balance, "$")

