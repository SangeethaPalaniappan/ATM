import sys

sys.path.append(r'C:\Users\sangee\ATM')
import ATM as atm
import NetBanking as netbanking
import SwipingMachine as swiping
import Bank_Account as bk
import WritingAccountDetailsInFile as acc_details

class TransactionOptions:
    def options(self):
        while True:
            print("1. ATM")
            print("2. NetBanking")
            print("3. Swiping")
            print("4. Exit")
            option = int(input("Select any one of the options : "))
            if option == 1:
                self.option_one()

            elif option == 2:
                  self.option_two()

            elif option == 3:
                  self.option_three()

            else:
                break    

    def option_one(self):
        atm_machine = atm.AtmMachine(bk.arr_bank_acc_holders)
        atm_machine.options()
        self.acc_details_file_obj() 
        atm_machine.write_atm_details_in_file()
        atm_machine.printing_details()      

    def option_two(self):
        net_banking = netbanking.NetBanking(bk.arr_bank_acc_holders)
        while True:
            sender_acc_no = int(input("Enter your Account Number : "))
            sender_password = int(input("Enter your password : "))
            if net_banking.authenticate(sender_acc_no, sender_password) != None:
                continue
            break
        
        self.acc_details_file_obj() 

    def option_three(self):
        RECEIVER_ACC_NO = 2209
        for receiver_acc_obj in bk.arr_bank_acc_holders:
            if receiver_acc_obj.get_acc_no() == RECEIVER_ACC_NO:
                swipe = swiping.SwipingMachine(receiver_acc_obj) 
                break
        sender_acc_no = int(input("Enter your Account Number : "))
        sender_password = int(input("Enter your password : "))
        swipe_obj = swipe.authenticate(sender_acc_no, sender_password)
        if swipe_obj == None:
            print("Try Again!")
        else:
            print(swipe_obj)    
        self.acc_details_file_obj() 
          

    def acc_details_file_obj(self): 
        acc_details_in_file = acc_details.Details()
        acc_details_in_file.write_acc_details_in_file()    