password = "sawhtet"
for i in range(3):
    j = 3
    pwd = input("Enter the Password: ")
    if (pwd==password):
        print ("welcome")
        break
    else:
        print("wrong password,Leave chance",j-i)
        continue
if(i==2):
    print("System locked")
