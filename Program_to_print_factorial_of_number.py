''' fact = 1
num = int(input("Enter any Number: "))
for i in range (1,num+1):
    fact = fact * i
print(fact)'''


fact = 1
num = int(input("Enter any Number: "))
i = 1
while(i<num):
    fact = fact * i
    i = i + 1
print ("the factor of",num , "is ",fact)

