import sys

# append a new directory to sys.path
sys.path.append(r'C:\Users\sange\ATM')

# now you can import your module
import Bank_Account as bk



class AtmMachine:
    def __init__(self):   
        
        arr = []
        g = open("AccountDetails.txt")
        for text in g:
            arr.append(text.split(","))
        g.close()
        print(arr)
        self.__arr_bank_holders = []
        for nums in range(len(arr) - 1):
            self.__arr_bank_holders.append(bk.BankAccount(int(arr[nums][0]), arr[nums][1], int(arr[nums][3]), int(arr[nums][2])))
        
        self.__atm_machine_details = []

        file_atm = open("AtmDetails.txt")
        for text in file_atm:
            self.__atm_machine_details.append(text.split(","))
        file_atm.close()    
        
        atm_array = self.__atm_machine_details[0]
        print(atm_array)
        self.__atm_balance = int(atm_array[0])
        
        self.__hundrd_counts = int(atm_array[1])
        self.__two_hundrd_counts = int(atm_array[2])
        self.__five_hundrd_counts = int(atm_array[3])


    def printing_details(self):
        for itr in range(len(self.__arr_bank_holders)):
            if itr == 0:
                print("Account_No.\t", "Balance\n")

            print(self.__arr_bank_holders[itr].get_acc_no(), "\t\t", self.__arr_bank_holders[itr].get_balance(), "\n")   
        
        print("\n")
        print("ATM_machine balance : ", self.__atm_balance)
        print("No. of hundred rupees notes      : ", self.__hundrd_counts)
        print("No. of two_hundred rupees notes  : ", self.__two_hundrd_counts)
        print("No. of five_hundred rupees notes : ", self.__five_hundrd_counts)      

    def __deposit(self, acc_no, amount):

        for requested_account in self.__arr_bank_holders:
            if acc_no == requested_account.get_acc_no():
                if amount > 1000 and amount < 100000:
                    if self.__check_pin(requested_account) == True:
                        requested_account.account_deposit(amount)
                        print("Rs.", amount, "deposited Successfully")   
                    else:
                        return None                          
                else:
                    print("Dear", requested_account.get_name(),", You can deposit only between Rs.1000 and Rs.100000")
                    return self.balance
                break
        self.__atm_balance += amount
        return self.__atm_balance
    
    def __withdraw(self, acc_no, amount):

        for requested_account in self.__arr_bank_holders:
            if acc_no == requested_account.get_acc_no():
                if amount > requested_account.get_balance():
                    print("Not enough Money") 
                    return None
                
                if amount < 100000 and amount > 1000:
                    if self.__check_pin(requested_account) == True:
                            obj_withdraw_process = self.__withdraw_process(amount, requested_account.get_balance())
                            if obj_withdraw_process != None:
                                requested_account.account_withdraw(amount)
                                print("Rs.", amount, "withdrawn Successfully")
                            else:
                                return None    
                    else:
                        return None    
                else:
                    print("Dear", requested_account.get_name(), ", You can withdraw only between Rs.1000 and Rs.100000")
                    return self.balance
                break    
        self.__atm_balance -= amount
        return self.__atm_balance
    
    def __check_pin(self, bank_account):
        enter_pin = int(input("Enter the Pin : "))
        if enter_pin == bank_account.get_acc_pin():
            return True
        else:
            print("Enter valid pin")
            return None
        
    def __account_details(self, account_arr, acc_no):
        for accounts in range(len(account_arr)):
            if account_arr[accounts].get_acc_no() == acc_no:
                print("Dear", (account_arr[accounts]).get_name(), ",", "Your account details \n")
                print("Account No.         : ", account_arr[accounts].get_acc_no()) 
                print("Balance             : ", account_arr[accounts].get_balance())
                break
        print("ATM_machine balance : ", self.__atm_balance)
    
    def __cash_count(self):
        
        self.hundrd_count        = int(input("No. of hundred rupees notes       : "))
        self.twohundr_count      = int(input("No. of two_hundred rupees notes   : "))
        self.five_hundr_count    = int(input("No. of five_hundred rupees notes  : "))
        total_count = (self.hundrd_count * 100) + (self.twohundr_count * 200) + (self.five_hundr_count * 500)
        return total_count
    
    def __add_cash_count(self):
        self.__hundrd_counts       += self.hundrd_count
        self.__two_hundrd_counts   += self.twohundr_count
        self.__five_hundrd_counts  += self.five_hundr_count

    def __withdraw_process(self, amount, account_balance):
        final_balance = account_balance - amount
        if final_balance >= 500:
            COUNT_OF_FIVE_HUNDRD, COUNT_OF_TWO_HUNDRD, COUNT_OF_ONE_HUNDRD  = 0, 0 ,0 

            five_hundrd = self.__five_hundrd_counts
            two_hundrd = self.__two_hundrd_counts
            one_hundrd = self.__hundrd_counts

            while (amount % 500 == 0 or amount % 500 == 200 or amount % 500 == 100)and amount != 0 and five_hundrd != 0:
                amount -= 500
                COUNT_OF_FIVE_HUNDRD += 1
                five_hundrd -= 1
                if amount == 100 or amount == 200:
                    break
                
            while (amount % 200 == 0 or amount % 200 == 100) and amount != 0 and two_hundrd != 0:
                
                amount -= 200
                COUNT_OF_TWO_HUNDRD += 1
                two_hundrd -= 1
                if amount == 100:
                    break
                
            while amount % 100 == 0 and amount != 0 and one_hundrd != 0:
                
                amount -= 100
                COUNT_OF_ONE_HUNDRD += 1  
                one_hundrd -= 1 
                
            if amount == 0:       
                self.__hundrd_counts       -= COUNT_OF_ONE_HUNDRD
                self.__two_hundrd_counts   -= COUNT_OF_TWO_HUNDRD
                self.__five_hundrd_counts  -= COUNT_OF_FIVE_HUNDRD 
                self.balance = final_balance
                return self.balance
            else:
                print("Account do not have the cash", amount)
                return None    
        else:
            print("Your account must have minimum balance of Rs.500")
            return None     


    def __transaction(self, acc_no, arr):
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
                    counting_cash = self.__cash_count()
                    if counting_cash == amount:
                        if self.__deposit(acc_no, amount) == None:
                            continue
                        else:
                            self.__add_cash_count()
                    else:
                        extra_amount = amount - counting_cash
                        if extra_amount < 0:
                            print("You have given", counting_cash, "Take", abs(extra_amount), "and deposit")
                        else:
                            print("You have given", counting_cash, "Put", extra_amount, "and deposit" )               

                elif option == 2:
                    amount = int(input("Enter the amount : "))

                    if self.__withdraw(acc_no, amount) == None:
                        continue
                elif option == 3:
                    self.__account_details(arr,acc_no)
                    
                elif option == 4:
                    print("Thank You! Visit Again!\n")
                    break
            except Exception:
                print("Error, Enter valid option")         
                        


    def atm_details(self):
        g = open("AtmDetails.txt", 'w')
        g.write(str(self.__atm_balance) + "," + str(self.__hundrd_counts) + "," + str(self.__two_hundrd_counts) + "," + str(self.__five_hundrd_counts))
        g.close()


        print("ATM_machine balance : ", self.__atm_balance)
        print("No. of hundred rupees notes      : ", self.__hundrd_counts)
        print("No. of two_hundred rupees notes  : ", self.__two_hundrd_counts)
        print("No. of five_hundred rupees notes : ", self.__five_hundrd_counts)    

    def accounts_details(self):
        f = open('AccountDetails.txt', 'w')
        for accounts in self.__arr_bank_holders:  
            
            account_no = str(accounts.get_acc_no())
            account_bal = str(accounts.get_balance())
            account_pin = str(accounts.get_acc_pin())

            f.write(account_no + "," + accounts.get_name() + "," + account_bal + ","  + account_pin + ",")
            f.write("\n")
        f.write("\n")
        f.close()
    
    def __create_new_account(self):
        print("\nWelcome! You're here to create new account!\n")
        acc_no = int(input("Enter account number : "))
        name = input("Enter Your Name : ")
        pin = int(input("Enter 4 digit pin : "))      
        AMOUNT = 0
        self.__arr_bank_holders.append(bk.BankAccount(acc_no, name, pin, AMOUNT))
        print("Account created successfully\n")
        file_bank_account = open("AccountDetails.txt", "a")
        account_no = str(acc_no)
        account_bal = str(AMOUNT)
        account_pin = str(pin)

        file_bank_account.write(account_no + "," + name + "," + account_bal + ","  + account_pin + ",")
        file_bank_account.write("\n")
        file_bank_account.close()


    def __to_do_transactions(self):
        while True:    
            transaction_option = input("Do you want to do transactions? (Yes/No): ")
            if transaction_option == "Yes":
                try:    
                    MATCH = 0
                    Acc_No = int(input("Account_No : "))
                    for i in range(len(self.__arr_bank_holders)):
                        if Acc_No == (self.__arr_bank_holders[i].get_acc_no()):
                            MATCH = 1
                            self.__transaction(Acc_No, self.__arr_bank_holders)
                            break
                        
                            
                    if MATCH == 0:
                        print("Enter correct Account Number")    
                        break    
                except Exception :
                    print("Error, Enter valid Number")
            else:
                break        
   
    def options(self):
        while True:
            print("1. Create New Account") 
            print("2. Do Transactions")   
            print("3. Exit")
            option_1_or_2_or_3 = int(input("Select any one of the options(1/2/3) : "))
            if option_1_or_2_or_3 == 2:
                self.__to_do_transactions()        
        
            elif option_1_or_2_or_3 == 1:
                self.__create_new_account()
                self.__to_do_transactions() 
            elif option_1_or_2_or_3 == 3:
                break

atm_machine = AtmMachine()
atm_machine.options()
atm_machine.accounts_details()
atm_machine.atm_details()
atm_machine.printing_details()


