class person:
    def __init__(self,name,age):
        self.name = name
        self.age =age
        print ("Welcome {}".format(name))  #This time call object eg p1 will return memory address

    def __str__(self):  #call special function
        return("name: {} \nage:{}".format(self.name,self.age))
    def __del__(self):  #specal function
        print("{} is dead n memory is free".format(self.name))

p1 = person("saw",35)
p2 = person("htet",25)
print (p1)
print (p2)
del(p1)
del(p2)
