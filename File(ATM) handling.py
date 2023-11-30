arr = []
g = open("python.txt")
for text in g:
    arr.append(text)
g.close()
print(arr)
array = []
for amount in arr:
    array.append(amount.split(","))
print(array)  

for nums in range(len(array) - 2):
    acc_no = int(array[nums][0])
    acc_bal = int(array[nums][1])
    print("acc_no   :", acc_no)
    print("acc_bal  :", acc_bal)
    
atm_balance = 0
atm_balance += int(array[len(array) - 1][0])
hundrd_count = 0
hundrd_count += int(array[len(array) - 1][1])
two_hundrd_count = 0
two_hundrd_count += int(array[len(array) - 1][2])
five_hundrd_count = 0
five_hundrd_count += int(array[len(array) - 1][3])
print(hundrd_count)
print(two_hundrd_count)
print(five_hundrd_count)
print(atm_balance)
