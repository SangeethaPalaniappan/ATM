class ATM:
    def __init__(self, arr):    
        self.balance = 0
        self.arr_bank_holders = arr
        self.hundrd_counts = 0
        self.two_hundrd_counts = 0
        self.five_hundrd_counts = 0

    def deposit(self, acc_no, amount):

        for requested_account in self.arr_bank_holders:
            if acc_no == requested_account.acc_no:
                if amount > 1000 and amount < 100000:
                    if self.check_pin(requested_account) == True:
                        requested_account.deposit(amount)
                        print("Rs.", amount, "deposited Successfully")                        
                else:
                    print("Dear", requested_account.name,", You can deposit only between Rs.1000 and Rs.100000")
                    return self.balance
                break
        self.balance += amount
        return self.balance
    
    def withdraw(self, acc_no, amount):

        for requested_account in self.arr_bank_holders:
            if acc_no == requested_account.acc_no:
                if amount > requested_account.balance :
                    print("Not enough Money") 
                    return None
                
                if amount < 100000 and amount > 1000:
                    if self.check_pin(requested_account) == True:
                            if requested_account.withdraw(amount) != None:
                                print("Rs.", amount, "withdrawn Successfully")
                            else:
                                return None    
                    else:
                        return None    
                else:
                    print("Dear", requested_account.name, ", You can withdraw only between Rs.1000 and Rs.100000")
                    return self.balance
                break    
        self.balance -= amount
        return self.balance
    
    def check_pin(self, bank_account):
        enter_pin = int(input("Enter the Pin : "))
        if enter_pin == bank_account.pin:
            return True
        else:
            print("Enter valid pin")
            return None
        
    def account_details(self, account_arr,acc_no):
        for accounts in range(len(account_arr)):
            if account_arr[accounts].acc_no == acc_no:
                print("Dear", (account_arr[accounts]).name, ",", "Your account details \n")
                print("Account No.         : ", account_arr[accounts].acc_no, ) 
                print("Balance             : ", account_arr[accounts].balance)
                break
        print("ATM_machine balance : ", self.balance)
    
    def cash_count(self):
        
        self.hundrd_count        = int(input("No. of hundred rupees notes       : "))
        self.twohundr_count      = int(input("No. of two_hundred rupees notes   : "))
        self.five_hundr_count    = int(input("No. of five_hundred rupees notes  : "))

        total_count = (self.hundrd_count * 100) + (self.twohundr_count * 200) + (self.five_hundr_count * 500)
        return total_count
    def add_cash_count(self):
        self.hundrd_counts       += self.hundrd_count
        self.two_hundrd_counts   += self.twohundr_count
        self.five_hundrd_counts  += self.five_hundr_count

        def withdraw_process(self, amount, account_balance):
            count_of_five_hundrd, count_of_two_hundrd, count_of_one_hundrd  = 0, 0 ,0 

            five_hundrd = atm_machine.five_hundrd_counts
            two_hundrd = atm_machine.two_hundrd_counts
            one_hundrd = atm_machine.hundrd_counts

            while (amount % 500 == 0 or amount % 500 == 200 or amount % 500 == 100)and amount != 0 and five_hundrd != 0:
                amount -= 500
                count_of_five_hundrd += 1
                five_hundrd -= 1
                if amount == 100 or amount == 200:
                    break
                
            while (amount % 200 == 0 or amount % 200 == 100) and amount != 0 and two_hundrd != 0:
                
                amount -= 200
                count_of_two_hundrd += 1
                two_hundrd -= 1
                if amount == 100:
                    break
                
            while amount % 100 == 0 and amount != 0 and one_hundrd != 0:
                
                amount -= 100
                count_of_one_hundrd += 1  
                one_hundrd -= 1 
                
            if amount == 0:       
                atm_machine.hundrd_counts       -= count_of_one_hundrd
                atm_machine.two_hundrd_counts   -= count_of_two_hundrd
                atm_machine.five_hundrd_counts  -= count_of_five_hundrd 
                self.balance = account_balance
                return self.balance
            else:
                print("Account do not have the cash", amount)
                return None    
  

    def transaction(self, acc_no, arr):
        while True:
            print("\n")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Account Detail")
            print("4. Exit")
            try:
                option = int(input("Select any one option : "))
                print("\n")
                if option == 1:
                    amount = int(input("Enter the amount : "))
                    counting_cash = self.cash_count()
                    if counting_cash == amount:
                        if self.deposit(acc_no, amount) == None:
                            continue
                        else:
                            self.add_cash_count()
                    else:
                        extra_amount = amount - counting_cash
                        if extra_amount < 0:
                            print("You have given more than", amount, "Take", abs(extra_amount), "and deposit")
                        else:
                            print("You have given lesser than", amount, "Put", extra_amount, "and deposit" )               

                elif option == 2:
                    amount = int(input("Enter the amount : "))

                    if self.withdraw(acc_no, amount) == None:
                        continue
                elif option == 3:
                    self.account_details(arr,acc_no)
                    
                elif option == 4:
                    print("Thank You! Visit Again!\n")
                    break
            except Exception:
                print("Error, Enter valid option")         
                        
    

accholder_1 = Bank_Account(1234, "Sangeetha", 2345)
accholder_2 = Bank_Account(2345, "Padmaja", 3456)
accholder_3 = Bank_Account(3456, "Abinaya", 5678)
accholder_4 = Bank_Account(5678, "Akshaya", 6789)
accholder_5 = Bank_Account(6789, "Keerthana", 7890)
accholder_6 = Bank_Account(7890, "Kaviya", 8901)

print(accholder_1.balance)
arr = [accholder_1, accholder_2, accholder_3, accholder_4, accholder_5, accholder_6]
for i in range(len(arr)):
    if i == 0:
        print("Account_No.\t", "Balance\n")

    print(arr[i].acc_no, "\t\t", arr[i].balance, "\n")

atm_machine = ATM(arr)
while True:
    option = input("Do you want to do transactions? (Yes/No) ")
    if option == "Yes":
        try :    
            Acc_No = int(input("Account_No : "))
            for i in arr:
                if Acc_No == i.acc_no:
                    call = atm_machine.transaction(Acc_No, arr)
                    break
        except Exception :
            print("Error, Enter valid option")
    else:
        break        

for i in range(len(arr)):
    if i == 0:
        print("Account_No.\t", "Balance\n")
    print(arr[i].acc_no, "\t\t", arr[i].balance, "\n")

print("ATM_machine balance : ", atm_machine.balance)
print("No. of hundred rupees notes      : ", atm_machine.hundrd_counts)
print("No. of two_hundred rupees notes  : ", atm_machine.two_hundrd_counts)
print("No. of five_hundred rupees notes : ", atm_machine.five_hundrd_counts)