class BankAccount():
    def __init__(self, accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    
    def Deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f"Deposit amount: {deposit_amount}, balance: {self.balance}") 

    def Withdrawal(self, withdraw_amount):
        self.balance -= withdraw_amount
        print(f"Withdraw amount: {withdraw_amount}, balance: {self.balance}")

    def bankFees(self):
        self.balance -= (0.05 * self.balance)
        print(f"Fees: {0.05 * self.balance}, balance: {self.balance}")

    def display(self):
        print(f"Account Detail \n\tAccount Number: {self.accountNumber}\n\tAccount Name: {self.name}\n\tBalance: {self.balance}")

kplus = BankAccount(3, "Sarm", 10000)
kplus.Deposit(1000)
kplus.Withdrawal(10)
kplus.bankFees()
kplus.display()
