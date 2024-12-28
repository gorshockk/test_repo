class BankAccount:
    def __init__(self, accountNumber: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def getBalance(self) -> float:
        return self.balance

import unittest

class TestBankAccount(unittest.TestCase):
    #создание обьекта с корректным некорректным балансом
    def test_create_account_with_positive_balance(self):
        account = BankAccount("123456", 100.0)
        self.assertEqual(account.getBalance(), 100.0)


    def test_create_account_with_negative_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("123456", -10.0)
    #Успешное добавление средств.
    def test_successful_deposit(self):
        account = BankAccount("123456")
        account.deposit(50.0)
        self.assertEqual(account.getBalance(), 50.0)
    #Попытка пополнить некорректную сумму (0 или отрицательное значение).
    def test_deposit_invalid_amount(self):
        account = BankAccount("123456")
        with self.assertRaises(ValueError):
            account.deposit(0.0)
        with self.assertRaises(ValueError):
            account.deposit(-10.0)
    #Успешное снятие, если сумма не превышает баланс.
    def test_successful_withdrawal(self):
        account = BankAccount("123456", 100.0)
        account.withdraw(40.0)
        self.assertEqual(account.getBalance(), 60.0)
    #Ошибка при попытке снять сумму больше текущего баланса.
    def test_withdrawal_exceeding_balance(self):
        account = BankAccount("123456", 50.0)
        with self.assertRaises(ValueError) as context:
            account.withdraw(60.0)
        self.assertEqual(str(context.exception), "Insufficient funds.")
    #Ошибка при попытке снять некорректную сумму (0 или отрицательное значение).
    def test_withdraw_invalid_amount(self):
        account = BankAccount("123456", 50.0)
        with self.assertRaises(ValueError):
            account.withdraw(0.0)
        with self.assertRaises(ValueError):
            account.withdraw(-20.0)
    #Проверка текущего баланса после операций.
    def test_balance_after_operations(self):
        account = BankAccount("123456", 100.0)
        account.deposit(50.0)
        account.withdraw(30.0)
        self.assertEqual(account.getBalance(), 120.0)

if __name__ == "__main__":
    unittest.main()
