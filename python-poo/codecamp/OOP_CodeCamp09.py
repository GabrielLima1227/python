# Static Methods
# A static method in Python is a method that belongs to the class itself rather than any instance of the class.
# To define a static method, we use the '@staticmethod' decorator

# Static vs. Instance Method Example

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0) -> None:
        self.owner = owner
        self._balance = balance

    def deposit (self, amount: float) -> None:
        if self._is_valid_amount(amount):
            self._balance += amount
            self.__log_transaction("Deposit", amount)
        else:
            print(f"Deposit amount must be positive.")

    def _is_valid_amount(self, amount: float) -> bool:
        return amount > 0

    def __log_transaction(self, transaction_typer, amount ) -> None:
        print(f"Logging {transaction_typer} of ${amount}. New balance: ${self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate: float) -> bool:
        return 0 <= rate <= 5

account = BankAccount("Alice", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))
