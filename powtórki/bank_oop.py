
class BankAccount:
    def __init__(self, account_number):
        self._balance = 0
        self._account_number = account_number


    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value <= 0:
            raise AttributeError("Account balance can not be on minus!")

        self._balance = value

    @balance.deleter
    def balance(self):
        raise AttributeError("U are blocked!")

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        raise AttributeError("U can not change account number!")

    @account_number.deleter
    def account_number(self):
        raise AttributeError("U can not delete this account number!")

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
            print(f"The money: {amount} has been sent from {sender.account_number} to {recipient.account_number}")
            print(f"\nSender account balance: {sender.balance} ")
            print(f"Recipient account balance: {recipient.balance}")

        else:
            print("U do not have enought money to make this transaction.")


Hiba_account = BankAccount.create_with_balance(2222222222222222222222, 200)
Rafal_account = BankAccount.create_with_balance(3333333333333333333, 500)

BankAccount.transfer(Hiba_account, Rafal_account, 100)



