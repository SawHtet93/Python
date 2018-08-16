import time
#time.time()
#t = time.asctime()
#print(t)
print("image1")
time.sleep(3)
print("image2")
time.sleep(3)

for a in range(1,11):
    print('\n')
    time.sleep(3)
    for b in range(1,11):
        print(a,"x",b,"=",a*b)
