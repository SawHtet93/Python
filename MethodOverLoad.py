'''Method OverLoading'''

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return("name : {} \nage:{}\n".format(name,age))

class teacher(person):
    def __init__(self,name,age,sub):
        self.sub = sub
        person.__init__(self,name,age)
    def __str__(self):
        return(person.__str__(self)+"sub: {}".format(self.sub))

class student(person):
    def __init__(self,name,age,lone):
        self.lone = lone
        person.__init__(self,name,age)
    def __str__(self):
        return(person.__str__(self)+"lone: {}".format(self.lone))
