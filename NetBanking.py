import sys

# append a new directory to sys.path
sys.path.append(r'C:\Users\sange\ATM')

# now you can import your module
import Bank_Account as bk
from BankTransactions import BankTransactions as bt

class NetBanking(bt):
    def __init__(self, bank_acc_arr):
        self.bank_acc_arr = bank_acc_arr
        

    def authenticate(self, sender_acc_no, sender_acc_password):
        
        acc_no_match = 0
        for sender_acc_obj in self.bank_acc_arr:
            if sender_acc_obj.get_acc_no() == sender_acc_no:
                acc_no_match = 1
                break
        if acc_no_match == 1:
            password_match = 0        
            if sender_acc_obj.get_acc_password() == sender_acc_password:
                password_match = 1

            if password_match == 1:
                
                bt.amount_transfer(sender_acc_obj, self.bank_acc_arr)      
                             
                        
            
            else:
                print("Enter correct password  ")       
                return None 
        else:
            print("Enter correct Account Number ")
            return None

   