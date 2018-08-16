''' bo = open('C:/Users/ICT/OneDrive/Documents/GitHub/Python/text.txt','w')
bo.write('This is the test file')
bo.close()
bo = open('C:/Users/ICT/OneDrive/Documents/GitHub/Python/text.txt','r')
print (bo.read()) '''

file = open('C:/Users/ICT/OneDrive/Documents/GitHub/Python/myfile.txt','w')

file.write(input())
print ("your file text is",'\n')
file =open('C:/Users/ICT/OneDrive/Documents/GitHub/Python/myfile.txt','r')
print (file.read())
