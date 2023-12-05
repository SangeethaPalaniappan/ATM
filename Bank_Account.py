class BankAccount:
    def __init__(self, acc_no, name, pin, amount):
        self.__acc_no = acc_no
        self.__name = name
        self.__pin = pin
        self.__balance = amount

    def account_deposit(self, amount):
        self.__balance += amount
        return self.__balance
    
    def account_withdraw(self,amount):
        self.__balance -= amount
        return self.__balance
    
    def get_acc_no(self):
        return self.__acc_no
    
    def get_acc_pin(self):
        return self.__pin
    
    def get_balance(self):
        return self.__balance
    
    def get_name(self):
        return self.__name
    
        
        


        