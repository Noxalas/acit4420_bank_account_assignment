class BankAccount:
    """
    Base bank account class with deposit and withdrawal functionality.

    This class stores the account holder's name and current balance, and provides methods to deposit and withdraw funds.

    Attributes:
        `account_holder` (str): Name of the account holder.
        `balance` (float): Current balance of the account, initialized to 0.0
    """
    
    def __init__(self, account_holder_name: str):
        self.account_holder_name: str = account_holder_name
        self.balance: float = 0.0

    def deposit(self, amount: float) -> bool:
        """Attempts to deposit an `amount` to the account balance. Returns `True` if it succeeds and `False` if it fails."""
        if amount > 0.0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True
        elif amount < 0.0:
            print("Deposit amount must be positive.")
            return False
        else:
            print("Deposit amount cannot be zero.")
            return False


    def withdraw(self, amount: float) -> bool:
        """Attempts to withdraw an `amount` from the account balance. Returns `True` if it succeeds and `False` if it fails."""
        if amount < 0.0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount == 0.0:
            print("Withdrawal amount cannot be zero.")
            return False
        elif amount > self.balance:
            print("Insufficient funds.")
            return False
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
            return True


    def account_info(self) -> str:
        """
        Returns a human-readable summary of the account.
        
        Includes the account holder's name and current balance formatted to two decimal places.
        """
        return f"Account holder: {self.account_holder_name}, Balance: ${self.balance:.2f}"


# Derived account class
class SavingsAccount(BankAccount):
    """
    A bank account that accrues interest over time.

    Inherits from BankAccount and adds an interest rate. The balance
    can be increased automatically using the apply_interest method.

    Attributes:
        interest_rate (float): Annual interest rate as a decimal (default 0.02).
    """

    def __init__(self, account_holder_name: str, interest_rate: float = 0.02) -> None:
        super().__init__(account_holder_name)
        self.interest_rate: float = interest_rate
    

    def apply_interest(self) -> None:
        """Applies interest to the account balance specified by the `interest_rate` parameter."""
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest: ${interest:.2f}. New balance: ${self.balance:.2f}")
    
    
    def account_info(self):
        """
        Returns a human-readable summary of the account.

        Includes the account holder's name, current balance, and the interest rate. All numerical values are formatted to two decimal places.
        """
        return str(super().account_info() + f", Interest: {(self.interest_rate * 100):.2f}%")
    

class CheckingAccount(BankAccount):
    """
    A bank account with a transaction fee for withdrawals.

    Inherits from BankAccount and overrides the withdraw method to
    deduct a fixed fee on each withdrawal.

    Attributes:
        transaction_fee (float): Fee charged per withdrawal (default 1.0).
    """

    def __init__(self, account_holder_name, transaction_fee = 1.0):
        super().__init__(account_holder_name)
        self.transaction_fee = transaction_fee


    def withdraw(self, amount):
        """Attempts to withdraw an `amount` from the account balance, including a transaction fee. Returns `True` if it succeeds and `False` if it fails."""
        if super().withdraw(amount):
            self.balance -= self.transaction_fee
            print(f"A transaction fee of ${self.transaction_fee:.2f} was deducted. New balance: ${self.balance:.2f}")
            return True
        return False
