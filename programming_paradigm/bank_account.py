class BankAccount: 
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount}"
    
    # withdraw method with insufficient fund check
    
    def withdraw(self, amount):
        # Return True when withdrawal succeeds, False when funds are insufficient.
        if amount > self.account_balance:
            return False

        self.account_balance -= amount
        return True
        
    def display_balance(self):
        if self.account_balance >= 0:
            return f"Current Balance: ${self.account_balance}"
        else:
            return "Account balance is negative."




