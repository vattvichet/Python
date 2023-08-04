# class Emp: 
#     def __init__(self, id,name,salary):
#         self.id = id
#         self.name = name
#         self.salary = salary
#     def __str__(self):
#         return (str(self.id)+ ' , '+self.name+' , '+str(self.salary)) # use with print(e) and e2
#     def output(self):
#         print(self.id, "\t", self.name, "\t",self.salary)

# e = Emp(1,"Dara", 500)
# e2 = Emp(2,"Vanna",400)
# e.output()
# e2.output()
# print(e)
# print(e2)

class Student: 
    def __init__(self, id,name,gender, math,english,java):
        self.id = id
        self.name = name
        self.gender = gender
        self.math = math
        self.english= english
        self.java= java
    def __str__(self):
        return (str(self.id)+ ' , '+self.name+' , '+self.gender+' , '+str(self.math)+ ' , ' + str(self.english)+ ' , '+ str(self.java)) 

s1 = Student(1,"Dara","Male", 100,95,89)
s2 = Student(2,"Pisey","Female", 98,98,92)
print(s1)
print(s2)
