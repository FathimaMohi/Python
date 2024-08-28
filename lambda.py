'''res=lambda a,b : a+b
print(res(10,20))

res=lambda a,b : a-b
print(res(10,20))

res=lambda a,b : a/b
print(res(10,20))

res=lambda a,b : a*b
print(res(10,20))

res=lambda a,b : a%b
print(res(10,20))

res=lambda a,b : a|b
print(res(10,20))

res=lambda a,b : a<b
print(res(10,20))

res=lambda a,b : a>b
print(res(10,20))

res=lambda a,b,c : max(a,b,c)
print(res(10,20,30))

res=lambda a,b,c : min(a,b,c)
print(res(10,20,30))

res=lambda a,b,c,d,e,f : max(a,b,c,d,e,f)
print(res(10,20,30,40,50,60))

res=lambda a,b :a if a>b else b
print(res(10,20))

res=lambda a: a.isupper()
print(res('fathima'))
res=lambda a: a.islower()
print(res('fathima'))
res=lambda a: a.upper()
print(res('fathima'))
res=lambda a: a.lower()
print(res('FATHIMA'))

x=[11,24,5,6,35,70]
res=list(filter(lambda x_even:(x_even%2==0),x))
print('Even number is',res)

x=[11,24,5,6,35,70]
res=list(filter(lambda x_odd:(x_odd%2==1),x))
print('odd number is',res)

x=[-11,24,-5,6,-35,70]
res=list(filter(lambda x_negative:(x_negative<0)  ,x))
print('Negative number is',res)

x=[-11,+24,-5,+6,-35,+70]
res=list(filter(lambda x_positive:(x_positive>0)  ,x))
print('Positive number is',res)

x=['amma','level','fuhy','radar','jui','madam','hi','ntt']
res=list(filter(lambda x: x==x[::-1],x))
print('palindrom is',res)

x=[11,24,5,6,35,70]
res=set(map(lambda x:(x*2),x))
print(res)

x=[11,24,5,6,35,70]
y=[23,4,5,67,78,89]
res=list(map(lambda x,y:(x*y),x,y))
print(res)

x=[11,24,5,6,35,70]
y=[23,4,5,67,78,89]
res=list(map(lambda x,y:(x+y),x,y))
print(res)

x=[11,24,5,6,35,70]
y=[23,4,5,67,78,89]
res=list(map(lambda x,y:(x-y),x,y))
print(res)

x=[11,24,5,6,35,70]
y=[23,4,5,67,78,89]
res=list(map(lambda x,y:(x/y),x,y))
print(res)

help('functools')

from functools import reduce
x=[23,45,45,65,56]
res=reduce(lambda x1,y1:x1*y1,x)
print(res)

from functools import reduce
x=[23,45,56,45,34,4]
res=reduce(lambda x1,y1:x1-y1,x)
print(res)

from functools import reduce
x=[23,45,45,65,23]
res=reduce(lambda x1,y1:x1/y1,x)
print(res)

import math as m
print('Power value of 2:',m.pow(2,3))

#Angular function
print(m.degrees(90))
print(m.radians(10))

print('Factorial of  is:',m.factorial(6))
print('Remainder  value is:',m.remainder(89,6))
print('Greates common divisor:',m.gcd(24,12))

#trignometric fn
print(m.sin(0))
print(m.cos(0))
print(m.tan(0))

#constant fun
print('pi value:',m.pi)
print('ulaer value:',m.e)
print( 'Tau value:',m.tau)

print(m.nan)#not a number
print(m.inf)#infinity

#Area of circle
r=float(input("Enter the radius:"))
a=m.pi*(r**2)
print("Area of circle:",a)

#calander module
import calendar 
print(calendar.calendar(2024,2))
print(calendar.month(2024,7))
print(calendar.isleap(2024))
print(calendar.isleap(2023))

#datetime
from datetime import date
today=date.today()
print(today)
print(today.year)
print(today.day)
print(today.month)

import datetime
today=datetime.datetime.now()
print(today)

date=datetime.date(2012,12,25)
print(date)

from datetime import datetime
now=datetime.now()
t=now.strftime("%H:%M:%S")
print(t)

from datetime import datetime
now=datetime.now()
t=now.strftime("%M:%D:%Y,%H:%M:%S")
print(t)

from datetime import datetime
now=datetime.now()
t=now.strftime("%m:%B:%y")
print(t)

from datetime import datetime
now=datetime.now()
t=now.strftime("%m:%b:%y")
print(t)
 
from datetime import datetime
now=datetime.now()
t=now.strftime("%m:%c:%y")
print(t)

import calendar
year=int(input("Enter the year"))
value=calendar.isleap(year)
if value == True:
    print("its a leap year",year)
else:
    print("its not a leap year",year)
help('cmath')

import cmath as c
print(c.acos(2+4j))

import cmath as c
print(c.asin(2+4j))

import cmath as c
print(c.atan(2+4j))

import cmath as c
print(c.sqrt(81))

import cmath as c
print(c.sqrt(45))

import cmath as c
print(c.acosh(2+4j))

import cmath as c
print(c.atanh(2+4j))

import cmath as c
print(c.asinh(2+4j))

#Random modules
import random
print(random.randint(0,5))

print(random.random())

print(random.random()*100)

list1=[1,2,3,4,'fathima','aysha']
result=random.choice(list1)
print(result)'''

import random
random.seed(4)
print(random.random())
print(random.randint(1,100))

import random
import math
r=random.random()*100
print(math.floor(r))

import random
import math
r=random.random()*100
print(math.ceil(r))

import random
def passw():
    password=(random.randint(1000,9999))
    return password
print(passw())












