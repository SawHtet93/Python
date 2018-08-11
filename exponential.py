#pow(2,3) (Same working)
num = int(input("Enter a number: "))
exp = int(input("Enter exponential number: "))
result = 1
for i in range(1,(exp+1)):
    result = result * num
print("The result is: ",result)
