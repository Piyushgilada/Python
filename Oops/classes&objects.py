# class Student:
#     def __init__(self): # this is special method known as constructor
#         self.age=19
#         self.name='Sahil'
#         self.gender='male'
#     def talk(self):     # this is instance method
#         print('my name is' ,self.name)
#         print("my age is ", self.age)
#
# m=Student()
# m.talk()
import socket


# class sample:
#     y = 10      # this is static/global variable
#     def __init__(self):
#         self.x=10   # this is instance/class variable
#
#     def modify(self):
#         self.y+=1
# s1=sample()
# s2=sample()
# print('x in s1= ',s1.y)
# print('x in s2= ',s2.y)
# s1.modify()
# print('x in s1= ',s1.y)
# print('x in s2= ',s2.y)

class Student:
    def setName(self, name):          #instance  // accessor methods
        self.name=name
    def getName(self):                  #instance // mutator metgod
        return self.name

    def setmarks(self, marks):
        self.marks=marks
    def getmarks(self):
        return self.marks
n=int(input("how many students"))
i=0
while(i<n):
    s=Student()
    name=input("enter name of student")
    s.setName(name)
    marks= int(input("enter marks of student"))
    s.setmarks(marks)
    print('hi',s.getName())
    print('yours marks',s.getmarks())
    i+=1
    print('----------------------')


