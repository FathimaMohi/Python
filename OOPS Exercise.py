#1
class vehicle:
    def __init__(self,car,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    def show(self):
      print("the car", car, "has the milage" ,mileage, "and speed" ,max_speed)
car = input("Enter the car ")
max_speed = input("Enter the max_speed ")
mileage = input("Enter the mileage ")
obj=vehicle(car,max_speed,mileage)
obj.show()
#2
class addition:
   def __init__(self,no1,no2):
      self.no1 = no1
      self.no2 = no2
   def show(self):
      print('Addition',no1+no2)
no1=int(input("Enter the no1"))
no2=int(input("Enter the no2"))
obj=addition(no1,no2)
obj.show()
#3
class vehicle:
    def __init__(self,color,max_speed,mileage):
        self.color=color
        self.max_speed=max_speed
        self.mileage=mileage
class bus(vehicle):
    pass
Bus=bus("Blue",100,50000)
print(Bus.color)
print(Bus.max_speed)
print(Bus.mileage)
#4
class vehicle:
    def __init__(self,color,max_speed,mileage,seating_capacity):
        self.color=color
        self.max_speed=max_speed
        self.mileage=mileage
        self.seating_capacity=seating_capacity
class bus(vehicle):
    pass
Bus=bus("Blue",100,50000,50)
print(Bus.color)
print(Bus.max_speed)
print(Bus.mileage)
print(Bus.seating_capacity)
#5
class myname:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=myname("fathima",20)
print(obj.__dict__)
#6
class student:
    pass
class mark:
    pass
student1=student()
mark1=mark()
print(isinstance(student1,student))
print(isinstance(mark1,mark))
print(issubclass(student,object))
print(issubclass(mark,object))
#8
class IntegerToRoman:
    def __init__(self,integer):
        self.integer=integer
    def convert(self):
        val=[1000,900,500,400,100,90,50,40,10,9,5,4]
        syb=['M','CM','D','CD','C','XC','L','XL','IX','V','IV','I']
        roman=''
        i=0
        while self.integer>0:
            for i in range(self.integer//val[i]):
                roman+=syb[i]
                self.integer-=val[i]
            i+=1
        return roman
r=IntegerToRoman(2010)
print(r.convert())
#9
class uniqe:
    def __init__(self,integer):
        self.integer=integer
    def subset(self):
        subsets=[[]]
        for i in self.integer:
            subsets+=[sub + [i]for sub in subsets]
            return subsets
os=uniqe([4, 5, 6])
print(os.subset())
#10
class power:
    def __init__(self,x,n):
        self.x=x
        self.n=n
    def calculate(self):
        return self.x**self.n
power=power(12,3)
print(power.calculate())
