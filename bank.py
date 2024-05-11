# bank.py

class Bank:
    bank_name = 'HDFC'
    branch_name = 'Marathahalli'
    IFSC = 'HDFC00024'
    roi = 0.07
    accounts = []  # List to store account instances

    def __init__(self, name, mno, accno, pan, balance, pin):
        self.name = name
        self.mno = mno
        self.accno = accno
        self.pan = pan
        self.balance = balance
        self.pin = pin

    @classmethod
    def create_account(cls, name, mno, pan, initial_deposit, pin):
        accno = len(cls.accounts) + 1  # Generate a unique account number
        new_account = cls(name, mno, accno, pan, initial_deposit, pin)
        cls.accounts.append(new_account)
        return f'Account created successfully. Account Number: {accno}'

    def validate_pin(self, entered_pin):
        return self.pin == entered_pin

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f'Amount withdrawn: {amount}'
        else:
            return 'Insufficient balance.'

    def deposit(self, amount):
        self.balance += amount
        return f'Amount deposited: {amount}'

    def change_pin(self, old_pin, new_pin):
        if self.pin == old_pin:
            self.pin = new_pin
            return 'PIN updated successfully.'
        else:
            return 'Incorrect old PIN.'
