from abc import ABC, abstractclassmethod

class BankTransactions(ABC):
    @abstractclassmethod
    def authenticate(self):
        pass

    def amount_transfer(sender_acc_obj, receiver_acc_obj):
        transfer_acc_no = 0  
        amount = int(input("Enter the amount you need to transfer : "))
        if sender_acc_obj.get_balance() < amount:
            print("You don't have enough money in your account")
            return None
        # need to include the minimum balance condition
        else:
            sender_acc_obj.account_withdraw(amount)
            receiver_acc_obj.account_deposit(amount)
            transfer_acc_no = 1
            
        if transfer_acc_no == 1:
            print("Amount transfered Successfully!")
        else:
            print("Enter correct receiver account no.")

          

               
   
                    

