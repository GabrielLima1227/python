# Encapsulation

# No Encapsulation 
class BadBankAccount:
    def __init__(self, balance):
        self.balance = balance

account01 = BadBankAccount(0.0)
account01.balance = -1

print(account01.balance)

# With Encapsulation
class GoodBankAccount:
    def __init__(self) -> None:
        self._balance = 0.0

    @property
    def balance(self) -> None:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            # raise: Essa é uma palavra-chave em Python usada para "lançar" ou "disparar" uma exceção. Exceções são eventos que alteram o fluxo normal de um programa.
            # ValueError: Este é o tipo de exceção que está sendo levantada. É tipicamente usada quando uma função recebe um argumento que tem o tipo correto, mas um valor inadequado.
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

print("-=" * 25)

account02 = GoodBankAccount()
print(account02.balance)

print("-=" * 25)

account02.deposit(1.99)
print(account02.balance)

print("-=" * 25)

account02.withdraw(1.00)
print(account02.balance)