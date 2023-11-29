class Bank_account:
    def __init__(self, acc_no, name, pin, amount = 0):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = amount

    def deposits(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraws(self,amount):
        self.balance -= amount
        return self.balance
            
        
        


        
