import sys

# append a new directory to sys.path
sys.path.append(r'C:\Users\sange\ATM')

# now you can import your module
import Bank_Account as bank

arr = []
g = open("python2.txt")
for text in g:
    arr.append(text.split(","))
g.close()
print(arr)

account_holder_array = []
for i in range(len(arr) - 1):
    account_holder = input("Account_holder_count : ")
    account_holder_array.append(account_holder)
print(account_holder_array)    
for nums in range(len(arr) - 1):
    account_holder_array[nums] = bank.Bank_account(arr[nums][0], arr[nums][1], arr[nums][3])

