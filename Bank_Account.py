class BankAccount:
    def __init__(self, acc_no, name, pin, amount, password):
        self.__acc_no = acc_no
        self.__name = name
        self.__pin = pin
        self.__balance = amount
        self.__password = password

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
    
    def get_acc_password(self):
        return self.__password

    @classmethod
    def write_acc_details_in_file(self):
        f = open('AccountDetails.txt', 'w')
        for accounts in arr_bank_acc_holders:  
            account_no = str(accounts.get_acc_no())
            account_bal = str(accounts.get_balance())
            account_pin = str(accounts.get_acc_pin())
            account_password = str(accounts.get_acc_password())

            f.write(account_no + "," + accounts.get_name() + "," + account_bal + ","  + account_pin + "," + account_password + ",")
            f.write("\n")
        f.close()

    
arr = []
g = open("AccountDetails.txt")
for text in g:
    arr.append(text.split(","))
g.close()
print(arr)
arr_bank_acc_holders = []
for nums in range(len(arr)):
    arr_bank_acc_holders.append(BankAccount(int(arr[nums][0]), arr[nums][1], int(arr[nums][3]), int(arr[nums][2]), int(arr[nums][4])))

        
        


        