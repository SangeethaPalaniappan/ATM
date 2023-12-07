import sys

sys.path.append(r'C:\Users\sangee\ATM')
import Bank_Account as bk
class Details:
    def write_acc_details_in_file(self):
        f = open('AccountDetails.txt', 'w')
        for accounts in bk.arr_bank_acc_holders:  
            account_no = str(accounts.get_acc_no())
            account_bal = str(accounts.get_balance())
            account_pin = str(accounts.get_acc_pin())
            account_password = str(accounts.get_acc_password())

            f.write(account_no + "," + accounts.get_name() + "," + account_bal + ","  + account_pin + "," + account_password + ",")
            f.write("\n")
        f.close()
