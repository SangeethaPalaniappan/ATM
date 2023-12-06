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
                receiver_acc_no = int(input("Enter receiver Account Number : "))
                for receiver_acc_obj in self.bank_acc_arr:
                    if receiver_acc_obj.get_acc_no() == receiver_acc_no:
                        if sender_acc_obj.get_acc_no() !=  receiver_acc_no:
                            bt.amount_transfer(sender_acc_obj, receiver_acc_obj)      
                             
                        else:
                            print("Sender and Receiver account no. should not be same")     
                            return None
            
            else:
                print("Enter correct password  ")       
                return None 
        else:
            print("Enter correct Account Number ")
            return None

net_banking = NetBanking(bk.arr_bank_acc_holders)
while True:
    sender_acc_no = int(input("Enter your Account Number : "))
    sender_password = int(input("Enter your password : "))
    if net_banking.authenticate(sender_acc_no, sender_password) != None:
        continue
    break
bk.BankAccount.write_acc_details_in_file()        