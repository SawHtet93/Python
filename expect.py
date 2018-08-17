num1 = int(input("Enter a Number: "))
num2 = int(input("Enter divided value: "))

try:
    num3 = num1/num2
except:
    print("You can\'t divide the number with zero")
else:
    print (num3)
