class Bank_Account:
    def __init__(self, acc_no, name, pin, amount = 0):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = amount

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self,amount):
        account_balance = self.balance - amount
        if account_balance >= 500:
            return self.balance
            
        else:
            print("Your account must have minimum balance of Rs.500")
            return None 
        


        
