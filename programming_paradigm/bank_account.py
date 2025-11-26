class BankAccount: 
    def __init__(self, account_balance):
        self.account_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount}"
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return f"Withdrew: ${amount}"

        # Insufficient funds
        return "Insufficient funds."
        
    def display_balance(self):
        if self.account_balance >= 0:
            return f"Current Balance: ${self.account_balance}"
        else:
            return "Account balance is negative."
    

        


