import uuid
from typing import Self


class FinancialCalculator:
    def __init__(self):
        self.accounts: list[BankAccount] = []

    @property
    def total_money(self):
        money = 0
        for account in self.accounts:
            money += account.balance
        return money

    def get_first_account(self) -> "BankAccount":
        if self.accounts:
            return self.accounts[-1]


class Person(FinancialCalculator):
    def __init__(self, name: str):
        if not name.strip():
            raise ValueError('Name not provided')
        super().__init__()
        self.name = name.title()
        self.ipn = uuid.uuid4()

    def __str__(self) -> str:
        return f'<Person name {self.name}, ipn {self.ipn}, and I have got {self.total_money}grn on {len(self.accounts)} accounts already>'


class BankAccount:
    def __init__(self, client: Person):
        self.client = client
        self.balance = 0

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount

    def transfer(self, amount: float, other: Self):
        self.balance -= amount
        other.balance += amount

    def __str__(self) -> str:
        return f'<Account belongs to {self.client.name}: balance {self.balance}>'


class Bank(FinancialCalculator):
    def __init__(self, name: str):
        super().__init__()
        self.__name: str = f'PAT {name.strip().upper()}'

    def open_account(self, client: Person) -> BankAccount:
        new_account = BankAccount(client)
        self.accounts.append(new_account)
        client.accounts.append(new_account)
        return new_account

    @property
    def name(self):
        return self.__name

    def __str__(self) -> str:
        return f'<Come to us. We are "{self.__name}", and we have opened {len(self.accounts)} accounts already and accumulated {self.total_money}grn>'


# person_alex = Person(name='Alex')
# person_marta = Person(name='Marta')
# person_bob = Person(name='Bob')
# print(person_alex)
# # print(int("000002415ED4ED50", 16))
#
# monobank = Bank('mono')
# print(monobank)
#
# account = monobank.open_account(person_alex)
# account.deposit(5000)
# account.deposit(2000)
# print(person_alex)
#
# print('walking....')
# print(monobank.total_money)
#
# alex_card = person_alex.get_first_account()
# alex_card.withdraw(500)
#
# # monobank.name = 'd,fjvbhjdfkbhjkkkkkfg'
# # monobank.total_money = 5555 error
# new_bank = Bank("ProstoKredit")
# new_bank.open_account(person_alex).deposit(6666)
# new_bank.open_account(person_bob).deposit(14000)
#
# print('walking....')
#
# person_bob.get_first_account().transfer(4000, person_alex.get_first_account())
#
# pass
