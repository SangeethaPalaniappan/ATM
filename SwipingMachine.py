import sys

sys.path.append(r'C:\Users\sangee\ATM')

from BankTransactions import BankTransactions as bt

import Bank_Account as bk


class SwipingMachine(bt):
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
                RECEIVER_ACC_NO = 2209
                for receiver_acc_obj in bk.arr_bank_acc_holders:
                    if receiver_acc_obj.get_acc_no() == RECEIVER_ACC_NO:
                        if sender_acc_obj.get_acc_no() !=  RECEIVER_ACC_NO:
                            bt.amount_transfer(sender_acc_obj, receiver_acc_obj) 
                            break     
                             
                        else:
                            print("Sender and Receiver account no. should not be same")     
                            return None
            
            else:
                print("Enter correct password  ")       
                return None 
        else:
            print("Enter correct Account Number ")
            return None
        
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