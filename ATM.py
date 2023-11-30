import sys

# append a new directory to sys.path
sys.path.append(r'C:\Users\sange\ATM')

# now you can import your module
import Bank_Account as bk


class ATM:
    def __init__(self, array):   

        arr = []
        g = open("python.txt")
        for text in g:
            arr.append(text)
        g.close()

        arrays = []
        for amount in arr:
            arrays.append(amount.split(","))


        for nums in range(len(arrays)):
            if arrays[nums][0] == "\n":
                continue
            for req_acc in array:
                if arrays[nums][0] == "\n":
                    continue
                if req_acc.acc_no == int(arrays[nums][0]):
                    req_acc.balance += int(arrays[nums][1])
                    break
            
        self.__atm_balance = int(arrays[len(arrays) - 1][0])
        self.arr_bank_holders = array
        self.hundrd_counts = int(arrays[len(arrays) - 1][1])
        self.two_hundrd_counts = int(arrays[len(arrays) - 1][2])
        self.five_hundrd_counts = int(arrays[len(arrays) - 1][3])
        self.printing_details(array)


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
        
    def account_details(self, account_arr,acc_no):
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
                        


    def atm_details(self):
        g = open("python.txt", 'a')
        g.write(str(atm_machine.__atm_balance) + "," + str(atm_machine.hundrd_counts) + "," + str(atm_machine.two_hundrd_counts) + "," + str(atm_machine.five_hundrd_counts))
        g.close()


        print("ATM_machine balance : ", atm_machine.__atm_balance)
        print("No. of hundred rupees notes      : ", atm_machine.hundrd_counts)
        print("No. of two_hundred rupees notes  : ", atm_machine.two_hundrd_counts)
        print("No. of five_hundred rupees notes : ", atm_machine.five_hundrd_counts)    

    def accounts_details(self):
        f = open('python.txt', 'w')
        for accounts in arr:  
            
            account_no = str(accounts.acc_no)
            account_bal = str(accounts.balance)

            f.write(account_no + "," +  account_bal + "," + accounts.name)
            f.write("\n")
        f.write("\n")
        f.close()


accholder_1 = bk.Bank_account(1234, "Sangeetha", 2345)
accholder_2 = bk.Bank_account(2345, "Padmaja", 3456)
accholder_3 = bk.Bank_account(3456, "Abinaya", 5678)
accholder_4 = bk.Bank_account(5678, "Akshaya", 6789)
accholder_5 = bk.Bank_account(6789, "Keerthana", 7890)
accholder_6 = bk.Bank_account(7890, "Kaviya", 8901)


arr = [accholder_1, accholder_2, accholder_3, accholder_4, accholder_5, accholder_6]


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

atm_machine.accounts_details()
atm_machine.atm_details()
atm_machine.printing_details(arr)



