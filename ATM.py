import sys

# append a new directory to sys.path
sys.path.append(r'C:\Users\sange\ATM')

# now you can import your module
import Bank_Account as bk



class ATM:
    def __init__(self):   
        
        arr = []
        g = open("python2.txt")
        for text in g:
            arr.append(text.split(","))
        g.close()
        print(arr)
        account_holder_array = []
        for i in range(len(arr) - 1):
            account_holder = input("Account_holder_count : ")
            account_holder_array.append(account_holder)
        print(account_holder_array)    
        for nums in range(len(arr) - 1):
            account_holder_array[nums] = bk.Bank_account(int(arr[nums][0]), arr[nums][1], int(arr[nums][3]))

        print(account_holder_array)
        length_of_acc_holder_array = len(account_holder_array)
        for nums in range(length_of_acc_holder_array):
            for req_acc in account_holder_array:
                if req_acc.acc_no == account_holder_array[nums].acc_no:
                    req_acc.balance += account_holder_array[nums].balance
                    break
        self.arr_bank_holders = account_holder_array
        atm_machine_details = []

        file_atm = open("python.txt")
        for text in file_atm:
            atm_machine_details.append(text.split(","))
        file_atm.close()    
        
        atm_array = atm_machine_details[0]
        print(atm_array)
        self.__atm_balance = int(atm_array[0])
        
        self.hundrd_counts = int(atm_array[1])
        self.two_hundrd_counts = int(atm_array[2])
        self.five_hundrd_counts = int(atm_array[3])
        self.printing_details(account_holder_array)


    def printing_details(self, arr):
        for i in range(len(arr)):
            if i == 0:
                print("Account_No.\t", "Balance\n")

            print(arr[i].acc_no, "\t\t", arr[i].balance, "\n")   
        
        print("\n")
        print("ATM_machine balance : ", self.__atm_balance)
        print("No. of hundred rupees notes      : ", self.hundrd_counts)
        print("No. of two_hundred rupees notes  : ", self.two_hundrd_counts)
        print("No. of five_hundred rupees notes : ", self.five_hundrd_counts)      

    def deposit(self, acc_no, amount):

        for requested_account in self.arr_bank_holders:
            if acc_no == requested_account.acc_no:
                if amount > 1000 and amount < 100000:
                    if self.check_pin(requested_account) == True:
                        requested_account.deposits(amount)
                        print("Rs.", amount, "deposited Successfully")   
                    else:
                        return None                          
                else:
                    print("Dear", requested_account.name,", You can deposit only between Rs.1000 and Rs.100000")
                    return self.balance
                break
        self.__atm_balance += amount
        return self.__atm_balance
    
    def withdraw(self, acc_no, amount):

        for requested_account in self.arr_bank_holders:
            if acc_no == requested_account.acc_no:
                if amount > requested_account.balance :
                    print("Not enough Money") 
                    return None
                
                if amount < 100000 and amount > 1000:
                    if self.check_pin(requested_account) == True:
                            obj_withdraw_process = self.withdraw_process(amount, requested_account.balance )
                            if obj_withdraw_process != None:
                                requested_account.withdraws(amount)
                                print("Rs.", amount, "withdrawn Successfully")
                            else:
                                return None    
                    else:
                        return None    
                else:
                    print("Dear", requested_account.name, ", You can withdraw only between Rs.1000 and Rs.100000")
                    return self.balance
                break    
        self.__atm_balance -= amount
        return self.__atm_balance
    
    def check_pin(self, bank_account):
        enter_pin = int(input("Enter the Pin : "))
        if enter_pin == bank_account.pin:
            return True
        else:
            print("Enter valid pin")
            return None
        
    def account_details(self, account_arr, acc_no):
        for accounts in range(len(account_arr)):
            if account_arr[accounts].acc_no == acc_no:
                print("Dear", (account_arr[accounts]).name, ",", "Your account details \n")
                print("Account No.         : ", account_arr[accounts].acc_no, ) 
                print("Balance             : ", account_arr[accounts].balance)
                break
        print("ATM_machine balance : ", self.__atm_balance)
    
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
        final_balance = account_balance - amount
        if final_balance >= 500:
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
                self.balance = final_balance
                return self.balance
            else:
                print("Account do not have the cash", amount)
                return None    
        else:
            print("Your account must have minimum balance of Rs.500")
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
                            print("You have given", counting_cash, "Take", abs(extra_amount), "and deposit")
                        else:
                            print("You have given", counting_cash, "Put", extra_amount, "and deposit" )               

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
                        


    def atm_details(self):
        g = open("python.txt", 'w')
        g.write(str(atm_machine.__atm_balance) + "," + str(atm_machine.hundrd_counts) + "," + str(atm_machine.two_hundrd_counts) + "," + str(atm_machine.five_hundrd_counts))
        g.close()


        print("ATM_machine balance : ", atm_machine.__atm_balance)
        print("No. of hundred rupees notes      : ", atm_machine.hundrd_counts)
        print("No. of two_hundred rupees notes  : ", atm_machine.two_hundrd_counts)
        print("No. of five_hundred rupees notes : ", atm_machine.five_hundrd_counts)    

    def accounts_details(self):
        f = open('python2.txt', 'w')
        for accounts in self.arr_bank_holders:  
            
            account_no = str(accounts.acc_no)
            account_bal = str(accounts.balance)
            account_pin = str(accounts.pin)

            f.write(account_no + "," + accounts.name + "," + account_bal + ","  + account_pin + ",")
            f.write("\n")
        f.write("\n")
        f.close()
    
    def new_account(self):
        print("Welcome! You're here to create new account!")
        acc_no = int(input("Enter account number : "))
        name = input("Enter Your Name : ")
        pin = int(input("Enter 4 digit pin : "))      
        amount = 0
        self.arr_bank_holders.append(bk.Bank_account(acc_no, name, pin))
        file_bank_account = open("python2.txt", "a")
        account_no = str(acc_no)
        account_bal = str(amount)
        account_pin = str(pin)

        file_bank_account.write(account_no + "," + name + "," + account_bal + ","  + account_pin + ",")
        file_bank_account.write("\n")

        file_bank_account.close()

       





atm_machine = ATM()
length = len(atm_machine.arr_bank_holders)
hold_arr = atm_machine.arr_bank_holders

while True:
    option = input("Do you want to do transactions? (Yes/No) ")
    if option == "Yes":
        try :    
            Acc_No = int(input("Account_No : "))
            for i in range(length):
                print(hold_arr[i].acc_no)
                if Acc_No == (hold_arr[i].acc_no):
                    call = atm_machine.transaction(Acc_No, atm_machine.arr_bank_holders)
                    break
        except Exception :
            print("Error, Enter valid option")
    else:
        break   
while True:        
    option_new_acc = input("Do you want to create new account? (Yes/No) ")
    if option_new_acc == "Yes":
        atm_machine.new_account()
    else:
        break
atm_machine.accounts_details()
atm_machine.atm_details()
atm_machine.printing_details(atm_machine.arr_bank_holders)


