# import pandas
# import numpy
# flag=True
# def calculator(n1,n2):
#     if n=="add":
#         print(n1+n2)
#     if n=="sub":
#         print(n1-n2)
#     if n=="mul":
#         print(n1*n2)
#     if n=="div":
#         print(n1/n2)
# while flag==True :
#     n1=int(input("Enter  first number"))
#     n2=int(input("Enter second number"))
#     n=input("Which operation do you want to perform ?")
#     calculator(n1,n2)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)


# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
# print(p1)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def __str__(self):
#     return f"{self.name}({self.age})"
#
# p1 = Person("John", 36)
#
# print(p1)

#function # day 31 july

# def addition(x1,x2):
#   sum=x1+x2;
#   return sum;
# sum=addition(10,20)
# print(sum)

# i=0
# while i<10 :
#   print(i ,end=" ")
#   i+=1

# car=["BMW","JAGUAR","LAMBO","TATA"]
# for i in car:
#   print(i,end=" ")

# a=int(input("enter first number..."))
# b=int(input("enter second number..."))
# if a>b:print(a,"is greater than ",b)

# a=int(input("enter first number..."))
# b=int(input("enter second number..."))
# if a>b:
#   print(a, "is greater than ", b)
# elif a<b:
#   print(a, "is less than ", b)
# else:
#   print(a, "is equal to ", b)


# class Person:
#   def __init__(object, name, age):
#     object.name = name
#     object.age = age
#   def myfunc(naam):
#     print("Hello my name is " + naam.name)
#
# obj1 = Person("Piyush", 20)
# obj1.myfunc()

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname
#   def printname(self):
#     print(self.firstname, self.lastname)
#
# x = Person("Cillian", "Morphy")
# x.printname()
#
# class Student(Person):
#   def __init__(self, fname, lname):
#     Person.__init__(self, fname, lname)
#
# y=Student("jr.Robert", "Downey")
# y.printname()
#
# class vehicle:
#   def __init__(self,name,year):
#     self.name=name
#     self.year=year
#   def move(self):
#     print("drive ")
#
# class car(vehicle):
#   pass
#
# class boat(vehicle):
#   def __init__(self,name,year):
#     self.name=name
#     self.year=year
#   def move(self):
#     print("sail ")
#
# class plane(vehicle):
#   def __init__(self,name,year):
#     self.name=name
#     self.year=year
#   def move(self):
#     print("fly ")
#
# car1=car("maruti suzuki",1992)
# boat1=boat("myboat",1990)
# plane1=plane("myplane",2000)
# for x in (car1,boat1,plane1):
#   x.move()

# import json
# x = '{ "name":"John", "age":30, "city":"New York"}'
# y = json.loads(x)
# print(y["age"])
# a = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# b = json.dumps(a)
# print(b)

# import json
# print(json.dumps({"name": "John", "age": 30}))

# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
#
# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

#
# import camelcase
# c = camelcase.CamelCase()
# txt = "hello world"
# print(c.hump(txt))

# try:
#   print(x)
# except ConnectionError:
#   print("Something else went wrong")

# price = 49
# penne=23
# chillar=98
# txt = "The price is {}.{}{} dollars"
# print(txt.format(price,penne,chillar))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))