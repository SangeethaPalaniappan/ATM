class Bank_account:
    def __init__(self):
        file = open("python2.txt")
        account_details = []
        for accounts in file:
            account_details.append(accounts)
        print(account_details)    
        file.close()
        print("\n")
        self.arrays = []
        for line in account_details:
            self.arrays.append(line.split(","))
        print(self.arrays)

    def account_creation(self, acc_no, name, pin, amount = 0):
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
            
        
account  =  Bank_account()             


        
