'''#Object Oriented Programming system
#Empty class creation
class car():
   pass
c=car()#object creation
c.carname='Exter' # Dictionary
c.model=2024
c.color='grey'
print('My car name is:',c.carname)
print(c.__dict__)
#Variable Declaration inside the class
class emp:
    name='fathima'
    deg='cs'
    age=20
e=emp()
print(f'My name is {e.name}  degree {e.deg} Age {e.age}')
#Single inheritance
class emp():
   def __init__(self,name,age,salary):
      self.name = name
      self.age = age
      self.salary = salary
class emp1(emp):
   def __init__(self,name,age,salary,id):
      self.name = name
      self.age = age
      self.salary = salary
      self.id = id
employee = emp('fathima',22,1000)
print(employee.age)
#multilevel inheritance
class employee():
   def __init__(self,name,age,salary):
      self.name = name
      self.age = age
      self.salary = salary
class employee1(employee):
   def __init__(self,name,age,salary):
      self.name = name
      self.age = age
      self.salary = salary
      self.id = id
class employee2(employee1):
   def __init__(self,name,age,salary):
      self.name = name
      self.age = age
      self.salary = salary
      self.id = id
emp1 = employee('fathima',22,1000)
emp2 = employee1('aysha',23,2000)
print(emp1.age)
print(emp2.age)
#Hierarchical inheritance
class employee():
   def __init__(self,name,age,salary):
      self.name = name
      self.age = age
      self.salary = salary
class employee1(employee):
   def __init__(self,name,age,salary):
      self.name = name
      self.age = age
      self.salary = salary
      self.id = id
class employee2(employee):
   def __init__(self,name,age,salary):
      self.name = name
      self.age = age
      self.salary = salary
      self.id = id
emp1 = employee('fathima',22,1000)
emp2 = employee1('aysha',23,2000)
print(emp1.age)
print(emp2.age)
#Hybrid inheritance
class school:
   def fun1(self):
      print("This function is in school")
class std1(school):
   def fun2(self):
      print("This function is in student")
class std2(school):
   def fun3(self):
      print("This function is in student2")
class std3(std1,school):
   def fun1(self):
      print("This function is in student3")
#object creation
object = std3()
object.fun1()
object.fun2()
#arithmetic op using mutilevel
class add:
   def __init__(self,no1,no2):
      self.no1 = no1
      self.no2 = no2
      print('Addition',no1+no2)
class sub(add):
   def __init__(self,no1,no2):
      self.no1 = no1
      self.no2 = no2
      a=add(no1,no2)
      print('Subractiontion',no1-no2)
class mul(sub):
   def __init__(self,no1,no2):
      self.no1 = no1
      self.no2 = no2
      b=sub(no1,no2)
      print('Multiplication',no1*no2)
class div(mul):
   def __init__(self,no1,no2):
      self.no1 = no1
      self.no2 = no2
      c=mul(no1,no2)
      print('division',no1/no2)
no1=int(input('Enter the number'))
no2=int(input('Enter the number'))
div(no1,no2)
#animal example
class animal:
   def __init__(self,name):
      self.name=name
class dog(animal):
   def speak(self):
      return f'{self.name} says woof'
class cat(animal):
   def speak(self):
      return f'{self.name} says meaw'
Dog=dog("puppy")
Cat=cat("Pushy")
print(Dog.speak())
print(Cat.speak())

#Polymorphism
#build in poly
s="python"
print(len(s))
#user defined
def add(x,y,z=0):
   return x+y+z
print(add(20,3))
print(add(25,30,4))
# Example of poly
class India():
   def capital(self):
      print("New Delhi is the capital of India")
   def language(self):
      print("Hindi is the most widely spoken language of india")
   def type(self):
      print("India is a developing country")
class USA():
   def capital(self):
      print("Washington is the capital of India")
   def language(self):
      print("English is the primary language of USA")
   def type(self):
      print("USA is a developed country")
obj_ind=India()
obj_usa=USA()
for country in(obj_ind,obj_usa):
 country.capital()
 country.language()
 country.type()


#Encapsulation-Hiding the informayion
class bank:
   def __init__(self,name,bankname,accno,amount):
      #public declaration
      self.name=name
      self.bankname=bankname
      self.acc=accno
      self.amt=amount
   def details(self):
      print(f'My name is {self.name} and having balance is {self.amt}')
b=bank('fathima','SBI',23454321,60000)
b.details()

#will occur error
class bank:
   def __init__(self,name,bankname,accno,amount):
      #public declaration
      self.name=name
      self.bankname=bankname
      self.acc=accno
      #private declaration
      self.__amt=amount
   def details(self):
      print(f'My name is {self.name} and having balance is {self.amt}')
b=bank('fathima','SBI',23454321,60000)
b.details()'''
'''#widraw
class bank:
   def __init__(self,name,bankname,accno,amount,balance):
      #public declaration
      self.name=name
      self.bankname=bankname
      self.acc=accno
      self.amt=amount
      self.bal=balance
   def withdraw(amount, name, balance):
    if amount <= accno[name]["balance"]:
        accno[name]["balance"] -= amount
        print("Withdrawn", amount,"total:",accno[name]["balance"])
    else:
        print("There is no balance")
   def details(self):
      print(f'My name is {self.name} and having balance is {self.amt}')
b=bank('fathima','SBI',23454321,60000)
b.details()

# using subclass
class call():
   def __init__(self,x,y):
      self.x=x
      self.y=y
   def add(self):
      return self.x+self.y
class call1:
   def sub(self):
      return self.x-self.y
class call2(call,call1):
   def mul(sel):
      return self.x*self.y
x=int(input("Enter the number"))
y=int(input("Enter the number"))
c=call2(x,y)
print(issubclass(call2,call1))
print(issubclass(call,call1))
#hybrid inheri
class cal():
   def __init__(self,x,y):
      self.x=x
      self.y=y
   def add(self):
      return self.x+self.y
class call2(cal):
   def sub(self):
      return self.x-self.y
class call3(call2):
   def mul(self):
      return self.x*self.y
class cal4(call3,cal):
   def div(self):
      return self.x/self.y
c4=cal4(50,20)
print('Division',c4.div())
print('Multiplication',c4.mul())
print('Additon',c4.add())
print('Subraction',c4.sub())
#Method Overloading
class Bank:
   def getroi(self):
      return 10
class SBI(Bank):
   def getroi(self):
      return 7
class ICICI(SBI):
   def getroi(self):
      return 5
b1=Bank()
print(b1.getroi())
b2=SBI()
print(b2.getroi())
#count of number of objects created

class sample:
   num=0
   def __init__(self,var):
      sample.num += 1
      self.var = var
      print("The object vaue is=", self.var)
      print("The count of objects created=",sample.num)
S1=sample(15)
S2=sample(35)
S3=sample(45)
#CONSTRUCTOR #DESTRUCTOR
class student:
   def __init__(self,name):
      print("Inside constructor")
      self.name=name
      print("Object initialized")
   def show(self):
      print("hello, My name is",self.name)
   def __del__(self):
      print("Inside Destructor")
      print("object destroyed")
s1=student('fathima')
s1.show()
del s1
s2=student('Mohideen')
s2.show()'''
#Abstaction
#it will hide the information it can be considerd as a blueprint
#for the other class.
#It allows you to create a set of methods the must be within any childclass.
from abc import ABC, abstractmethod
class car(ABC):
   def milage(self):
      pass
class hyundai(car):
   def mileage(self):
    print("It Gives the Mileage of 25 KMPL")
class Tata(car):
   def mileage(self):
    print("It Gives the Mileage of 35 KMPL")
hy=hyundai()
hy.mileage()

