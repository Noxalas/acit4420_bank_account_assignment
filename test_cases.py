from bank_account import *

def test_bank_account():
    """Test cases for the BankAccount class"""
    acc = BankAccount("Alice")
    assert acc.deposit(100) == True
    assert acc.balance == 100
    assert acc.deposit(-50) == False # Cannot be negative
    assert acc.deposit(0) == False # Cannot be zero
    assert acc.withdraw(30) == True
    assert acc.balance == 70
    assert acc.withdraw(100) == False # Insufficient funds
    assert acc.withdraw(-10) == False # Cannot be negative
    assert acc.withdraw(70) == True
    assert acc.withdraw(0) == False # Cannot be zero
    print(acc.account_info())


def test_savings_account():
    """Test cases for the SavingsAccount class"""
    sav = SavingsAccount("Bob", interest_rate=0.05)
    sav.deposit(200)
    sav.apply_interest()
    assert round(sav.balance, 2) == 210.00 # 200 + 5% interest
    sav.withdraw(50)
    assert round(sav.balance, 2) == 160.00
    sav.apply_interest()
    assert round(sav.balance, 2) == 168.00 # 160 + 5% interest
    print(sav.account_info())


def test_checking_account():
    """Test cases for the CheckingAccount class"""
    chk = CheckingAccount("Charlie", transaction_fee=2.0)
    chk.deposit(100)
    assert chk.withdraw(50) == True # withdraws 52 including fee
    assert chk.balance == 48
    assert chk.withdraw(50) == False # insufficient funds after fee
    chk.deposit(10)
    assert chk.withdraw(60) == False # still insufficient after fee
    print(chk.account_info())


if __name__ == "__main__":
    test_bank_account()
    test_savings_account()
    test_checking_account()

    print("All tests succeeded! Exiting...")