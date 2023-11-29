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
            return self.withdraw_process(amount, account_balance)
            
        else:
            print("Your account must have minimum balance of Rs.500")
            return None 
        
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

        
