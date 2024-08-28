def wish():
    print("Happy Birth Day dear")
wish()
def add():
    a=10
    b=9
    print("Addition",a+b)
add()
def wish1():
   print("hello world")
for i in range(10):
 wish1()
#positioning arg
def num(x):
 print(x)
num(100)
def num(x,y):
 print(x)
 print(y)
num(100,30)
#Keyword arg
def num(x,y):
 print(x)
 print(y)
 print(x+y)
num(y=100,x=30)
a=input("Enter your name")
def name(x):
  print( "hello",x)
name(a)
#default arg
def num(x,y=20):
    print(x)
    print(y)
num(10)
#variable length arg
def num(x,*y):
    print(x)
    print(y)
num(25,35,45,50,60)

def num(x,*y):
    t=x
    for i in y:
     t=t+i
    print(t)
num(25,35,45,50,60)

#factorial
x=int(input('enter a number'))
y=1
def num(x,y):
  for i in range(1,x+1):
   y=y*i
   print('Factorial of number is',y)
num(x,y)
#Return keyword
x=int(input("Enter the number"))
y=int(input("Enter the number"))
def large(x,y):
          if(x>y):
              return x
          else:
              return y
print("the Largest of numbers",large(x,y))
