#1
def arithmetic():
  print("***Arithmetic Operation***")
  print("1.Addition")
  print("2.Subraction")
  print("3.Multiplication")
  print("4.Division")
  ch=int(input("Enter the number:"))  
  a=int(input("Enter the number 1:"))
  b=int(input("Enter the number 2:"))
  if ch==1:
    print("Addition:",a+b)
  elif ch==2:
    print("Subraction:",a-b)
  elif ch==3:
    print("Multiplication:",a*b)
  elif ch==4:
    print("Division:",a/b)
arithmetic()
#2
a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
if a>b:
  print("a is greater than b")
elif a<b:
  print("a less than b")
elif a==b:
  print("a is equal to b")
elif a!=b:
  print("a is not equal to b")
#3
class log1():
  def __init__(self,a,b):
    print("And Operation:",a>0 and b>0)
class log2(log1):
  def __init__(self,a,b):
    x=log1(a,b)
    print("Or Operation:",a>0 or b>0)
class log3(log2):
  def __init__(self,a,b):
    y=log2(a,b)
    print("Not Operation:",not(a>0 and b>0))
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
log3(a,b)
#4
a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
if a==b:
    print("A is equal to b")
else:
    print("A is not equal to B")
#5
li=[1,2,3,4,5]
li=li[:-2]
print(li)
#6
tu=(1,2,3,4,5,6)
print(tu[2])
print(tu[-3])
#7
tu=(1,2,2,3,4,4,4,5)
tu=tu[::-1]
print(tu)
print(tu.count(4))
#8
tuple1=(1,2,2,3,"tuple")
list1=[1,2,2,3,"list"]
print(tuple1)
print(list1)
#9
for i in range(10,0,-2):
        print(i)
#10
a="Hello World"
b=5
c=10
print(a,"\n sum:",b+c)
#11
import math
num=int(input("Enter the number:"))
print("Square Root:",math.sqrt(num))
#12
base=10
height=15
area=0.5*base*height
print("Area:",area)
#13
import math
a=1
b=-5
c=6
dis=b**2-4*a*c
if dis>=0:
    r1=(-b+math.sqrt(dis))/(2*a)
    r2=(-b-math.sqrt(dis))/(2*a)
    print("Roots:",r1,r2)
else:
    print("no roots")
#14
a=5
b=10
a,b=b,a
print("a=",a)
print("b=",b)
#15
a=int(input("Enter the number:"))
if a>0:
    print("Positive")
elif a<0:
    print("Negative")
else:
    print("Zero")
#16
a=int(input("Enter the number:"))
if a%2==0:
    print("Even number")
else:
    print("Odd number")
#17
yr=int(input("Enter the year:"))
if yr%4==0 and yr%400==0 :
    print("Leap year")
else:
    print("Not Leap year")
#18
a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
c=int(input("Enter the number 3:"))
if a>=b and a>=c:
    print("Largest number is:",a)
elif b>=a and b>=c:
    print("Largest number is:",b)
else:
    print("Largest number is:",c)
#19
n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
#20
a={'age':12,'age2':13,'age3':14,'age4':15}
b={k:v for k, v in a.items() if v%2==0}
print(b)
