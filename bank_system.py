class Bank_account:
    def __init__(self, account_number, account_holder, balance = 0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance+=amount
        print(f"Amount deposited is : {amount} and the New Balance is : {self.balance}")
        
    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"{amount} is withdrawn and the remaining balance is {self.balance}")
            
        else:
            print("Insufficient balance")
            
    def check_balance(self):
        print(f"The balance is {self.balance}")
        
    def transfer(self, other_account, amount):
        if self.balance>= amount:
            self.balance-=amount
            other_account.balance+=amount
            print(f"Transferred Rs: {amount} to account number : {other_account.account_number}")
            
        else:
            print("Insufficient balance to transfer")
            
account1 = Bank_account("56437", "A", 1000)
account2 = Bank_account("67890", "B", 500)

account1.deposit(200)
account1.withdraw(150)
account1.transfer(account2, 300)
account1.check_balance()
account2.check_balance()

            
            
             