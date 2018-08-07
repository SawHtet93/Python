num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
num3 = int(input("Enter a number3: "))

if ((num1>num2) & (num1>num3)):
    print (num1,"is the greates among three")
elif((num2>num1) & (num2>num3)):
    print (num2,"is the greates among three")
else:
    print (num3,"is the greates among three")

