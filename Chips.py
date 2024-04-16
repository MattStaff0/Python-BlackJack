class Chips():
    # init method 
    def __init__(self, bal):
        self.bal = bal

    def deposit(self, amount):
        self.bal += amount
        print(f'Successfully deposited into account!')
        print(f'Current Balance: {self.bal}')

    def bet(self, amount):
        if self.bal < amount:
            print("Cannot place bet, balance too low.")
            return False
        print("Bet successfully placed!")
        return True
    
    def withdraw(self,amount):
        self.bal -= amount
        print(f'Current Balance: {self.bal}')

    def __str__(self):
        return f'Your balance: {self.bal}'
        
