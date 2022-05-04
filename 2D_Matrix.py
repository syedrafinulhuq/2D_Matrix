Rows = int(input("Enter Rows : "))
Column = int(input("Enter Column : "))
M = []
for i in range(Rows):
  I = []
  for j in range(Column):
    v = int(input())
    I.append(v)
    M.append(I)

print(M)

user_wish = input("Do You Want To Print M[1][2] : ")

if Rows > 1 and Column > 1 and user_wish == "Yes":
  print("M[1][2] is not possible because rows and column are small ")
  print("So we printed M[1][1]")
  print("The answer is : ",M[1][1])
  
  
elif Rows > 2 and Column > 2 and user_wish == "Yes"  :
  print(M[1][2])  
  
print("Happy Ending")