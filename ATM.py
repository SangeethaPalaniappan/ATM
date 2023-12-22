import sys

# append a new directory to sys.path
sys.path.append(r'C:\Users\sange\ATM')

# now you can import your module
import Bank_Account as bk

from BankTransactions import BankTransactions as bt

class AtmMachine(bt):
    def __init__(self, account_array):   
        
        self.account_array = account_array
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
        for itr in range(len(self.account_array)):
            if itr == 0:
                print("Account_No.\t", "Balance\n")

            print(self.account_array[itr].get_acc_no(), "\t\t", self.account_array[itr].get_balance(), "\n")   
        
        print("\n")
        print("ATM_machine balance : ", self.__atm_balance)
        print("No. of hundred rupees notes      : ", self.__hundrd_counts)
        print("No. of two_hundred rupees notes  : ", self.__two_hundrd_counts)
        print("No. of five_hundred rupees notes : ", self.__five_hundrd_counts)      

    def deposit(self, acc_no, amount):

        for requested_account in self.account_array:
            if acc_no == requested_account.get_acc_no():
                if amount >= 500 and amount < 100000:
                    if self.__check_pin(requested_account) == True:
                        requested_account.account_deposit(amount)
                        print("Rs.", amount, "deposited Successfully")   
                    else:
                        return None                          
                else:
                    print("Dear", requested_account.get_name(),", You can deposit from Rs.500 to Rs.100000")
                    return self.balance
                break
        self.__atm_balance += amount
        return self.__atm_balance
    
    def withdraw(self, acc_no, amount):

        for requested_account in self.account_array:
            if acc_no == requested_account.get_acc_no():
                if amount > requested_account.get_balance():
                    print("Not enough Money") 
                    return None
                
                if amount <= 100000 and amount >= 500:
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
                    print("Dear", requested_account.get_name(), ", You can withdraw from Rs.500 to Rs.100000")
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
        
    def account_details(self, account_arr, acc_no):
        for accounts in range(len(account_arr)):
            if account_arr[accounts].get_acc_no() == acc_no:
                print("Dear", (account_arr[accounts]).get_name(), ",", "Your account details \n")
                print("Account No.         : ", account_arr[accounts].get_acc_no()) 
                print("Balance             : ", account_arr[accounts].get_balance())
                break
        print("ATM_machine balance : ", self.__atm_balance)
    
    def __cash_count(self, amount):
        
        hundrd_count        = int(input("No. of hundred rupees notes       : "))
        twohundr_count      = int(input("No. of two_hundred rupees notes   : "))
        five_hundr_count    = int(input("No. of five_hundred rupees notes  : "))
        total_count = (hundrd_count * 100) + (twohundr_count * 200) + (five_hundr_count * 500)
  
        if total_count == amount:
            self.__hundrd_counts       += hundrd_count
            self.__two_hundrd_counts   += twohundr_count
            self.__five_hundrd_counts  += five_hundr_count
            return 1
        return 0

    def __withdraw_process(self, amount, account_balance):
        final_balance = account_balance - amount
        if final_balance >= 500:
            count_of_five_hundrd, count_of_two_hundrd, count_of_one_hundrd  = 0, 0 ,0 

            five_hundrd = self.__five_hundrd_counts
            two_hundrd = self.__two_hundrd_counts
            one_hundrd = self.__hundrd_counts

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
                self.__hundrd_counts       -= count_of_one_hundrd
                self.__two_hundrd_counts   -= count_of_two_hundrd
                self.__five_hundrd_counts  -= count_of_five_hundrd 
                self.balance = final_balance
                return self.balance
            else:
                print("Account do not have the cash", amount)
                return None    
        else:
            print("Your account must have minimum balance of Rs.500")
            return None     


    
    def write_atm_details_in_file(self):
        g = open("AtmDetails.txt", 'w')
        g.write(str(self.__atm_balance) + "," + str(self.__hundrd_counts) + "," + str(self.__two_hundrd_counts) + "," + str(self.__five_hundrd_counts))
        g.close()


        print("ATM_machine balance : ", self.__atm_balance)
        print("No. of hundred rupees notes      : ", self.__hundrd_counts)
        print("No. of two_hundred rupees notes  : ", self.__two_hundrd_counts)
        print("No. of five_hundred rupees notes : ", self.__five_hundrd_counts)    

    
    def create_new_account(self):
        print("\nWelcome! You're here to create new account!\n")
        acc_no = int(input("Enter account number : "))
        name = input("Enter Your Name : ")
        pin = int(input("Enter 4 digit pin : "))      
        AMOUNT = 0
        password = int(input("Enter the password : "))
        self.account_array.append(bk.BankAccount(acc_no, name, pin, AMOUNT, password))
        print("Account created successfully\n")
        file_bank_account = open("AccountDetails.txt", "a")
        
        file_bank_account.close()


    def to_do_transactions(self):
        while True:    
            transaction_option = input("Do you want to do transactions? (Yes/No): ")
            if transaction_option == "Yes":
                try:    
                    match = 0
                    acc_No = int(input("Account_No : "))
                    for i in range(len(self.account_array)):
                        if acc_No == (self.account_array[i].get_acc_no()):
                            match = 1
                            self.transaction(acc_No, self.account_array)
                            break
                        
                            
                    if match == 0:
                        print("Enter correct Account Number")    
                        break    
                except Exception :
                    print("Error, Enter valid Number")
            else:
                break    
   
    
    def cash_handling(self, acc_no):
        amount = int(input("Enter the amount : "))
        counting_cash = self.__cash_count(amount)
        if counting_cash == True:
            if self.deposit(acc_no, amount) == None:
                return None
            else:
                return 1
        else:
            extra_amount = amount - counting_cash
            if extra_amount < 0:
                print("You have given", counting_cash, "Take", abs(extra_amount), "and deposit")
            else:
                print("You have given", counting_cash, "Put", extra_amount, "and deposit" )

    def authenticate(self, sender_acc_no, sender_acc_pin_no):
        
        acc_no_match = 0
        for sender_acc_obj in self.account_array:
            if sender_acc_obj.get_acc_no() == sender_acc_no:
                acc_no_match = 1
                break
        if acc_no_match == 1:
            pin_match = 0        
            if sender_acc_obj.get_acc_pin() == sender_acc_pin_no:
                pin_match = 1

            if pin_match == 1:
                bt.amount_transfer(sender_acc_obj, self.account_array)      
                               
            
            else:
                print("Enter correct password  ")        
        else:
            print("Enter correct Account Number ")


    def transaction(self, acc_no, arr):
        while True:
            print("\n")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Amount Transfer")
            print("4. Account Detail")
            print("5. Exit")
            try:

                option = int(input("Select any one option : "))
                print("\n")
                if option == 1:
                    if self.cash_handling(acc_no) == None:
                        continue              

                elif option == 2:
                    amount = int(input("Enter the amount : "))

                    if self.withdraw(acc_no, amount) == None:
                        continue
                elif option == 3:
                    print("AmountTransaction")
                    sender_acc_no = int(input("Enter your Account Number : "))
                    sender_pin_no = int(input("Enter your Pin No. : "))
                    self.authenticate(sender_acc_no, sender_pin_no)
                    
                    
                elif option == 4:
                    self.account_details(arr,acc_no)
                    
                elif option == 5:
                    print("Thank You! Visit Again!\n")
                    break
            except Exception:
                print("Error, Enter valid option")         
                        
    def options(self):
        while True:
            print("1. Create New Account") 
            print("2. Do Transactions")   
            print("3. Exit")
            option = int(input("Select any one of the options : "))
            if option == 2:
                self.to_do_transactions()                
        
            elif option == 1:
                self.create_new_account() 
                self.to_do_transactions()

            elif option == 3:
                break



