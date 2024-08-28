import re
s='Hello Good Morning'
res=re.findall(r'^He',s)#r-raw data
print(res)

#Exp for r
print('hello \n new')
print(r'hello \n new')

s='Hello Good Morning'
res=re.match(r'He',s)
print(res)

import re
s='Hello Good Morning'
res=re.search(r'Good',s)
if res:
    print(res,'\nParticular String is Available')
else:
    print('not available')

import re
s='Hello Good Morning'
res=re.search(r'good',s)
if res:
    print(res,'\nParticular String is Available')
else:
    print('not available')

#A Python program to create a regular expression to search at the ending a string by ignoring the case.
import re
word='Python Program'
result=re.search(r'program',word,re.IGNORECASE)
print(result)

#python program tocreate a regex to retrieve marks & names from a given string
w='Suba got 80.5 marks, Manju got 75 marks, whreas Venki got 82.'
marks=re.findall(r'\d{2}',w)
print(marks)
names=re.findall(r'[A-Z][a-z]*',w)
print(names)

import re
tx="The rain in tenkasi"
x=re.findall("[a-m]",tx)
print(x)

import re
tx="The value is 23"
x=re.findall("\d",tx)
print(x)

import re
tx="The rain 56 in tenkasi"
x=re.findall("te....i",tx)
print(x)

import re
tx="Th"
x=re.findall("Th.*",tx)
print(x)

import re
tx="Th"
x=re.findall("Th.+",tx)
print(x)

import re
tx="The rain in tenkasi"
x=re.findall("fath|ima",tx)
print(x)
if x:
    print("yes,there is at least one match")
else:
    print("No match")


#program to create a regex that reads email form
import re
f=open('D:\Excel&Python\\mail.txt','r')
for line in f:
    res=re.search(r'\S+@\S.+',line)
    print(res)
f.close()

import re
m=re.match(r'(\w+)@(\w+)\.(\w+)','fathima2004@gmail.com')
print(m.group())


l=[1,2,3,4,5,6]
square=tuple(map(lambda x:x**2,l))
print(square)

l=[1,2,3,4,5,6,3]
square=set(map(lambda x:x**2,l))
print(square)
print(l.count(3))

def func(x, l=[]):
    for i in range(x):
        l.append(i)
    print(l)
func(2)
func(3, [3, 2, 1])
func(3)

import re
s='kumbhmela will be conducted at Ahmedabad in India'
res=re.sub(r'Ahmedabad','Allahabad',s)
print(res)

import re
pattern = re.compile(r"\d")
sentence = "I went to the store and bought 5 apples, 4 oranges, and 15 plums."
print(pattern.findall(sentence))
pattern = re.compile(r"\D")
print(pattern.findall(sentence))

import re
pattern = re.compile("flower")
match = pattern.search("a red flower in the field")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

import re
pattern = re.compile("flower")
print(type(pattern))
print(pattern.search("candy"))
match = pattern.search("a red flower in the field flower")
print(type(match))
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

from datetime import date
birthday = date(2004, 7, 13)
print(birthday)
print(type(birthday))
moon_landing = date(year = 2004, month = 7, day = 13)
print(moon_landing)
print(birthday.year)
print(birthday.month)
print(birthday.day)
today = date.today()
print(today)
print(type(today))
