"""  Inheritance : if you have already created a class you can call from another call
is call inheritance """

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("name is {} and agie is {}".format(name,age))
class teacher(person):
    def print(self,name,age):
        person.__init__(self,name,age)

class student(person):
    def print(self,name,age):
        person.__init__(self,name,age)
