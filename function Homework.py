'''#1
def num(x,y,z):
    if (x>y):
        print('x is greater than y')
    elif(y>z):
        print('y is greater than z')
    else:
        print('x is less than z')
x=int(input("Enter the number"))
y=int(input("Enter the number"))
z=int(input("Enter the number"))
num(x,y,z)
#2
x=[2,3,4,5,6]
def let(x):
   print(sum(x))
let(x)
               
#3
s=input('Enter the charater')
def let(s):
 upper_count=0
 lower_count=0
 for i in s: 
  if i.isupper():
    upper_count+=1
    print('upper count',upper_count)
  else:
    lower_count+=1
    print('lower count',lower_count)  
let(s)
#4
x=int(input('enter a number'))
y=1
def num(x,y):
  for i in range(1,x+1):
   y=y*i
   print('Factorial of number is',y)
num(x,y)

#5
x=int(input('enter a number'))
def num(x):
 if (x%2)==1:
  print('its an prime number')
 else:
  print('its not an prime number')
num(x)
#6
def reverse(num):
    rev=0
    while(num>0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    print(rev)
num=int(input('Enter the number'))
reverse(num)
#6
x=input('Enter the string')
def rs(x):
 print( x[::-1])
rs(x)
#10
def rv(s):
    v = ['a','e','i','o','u','A','E','I','O','U']
    for i in s:
        if (i not in v):
         print(i,end="")
s=input("Enter the string")
rv(s)
#11
x=['apple','banana','orange']
def st(x):
    li=[]
    for i in x:
      if(len(i)==5):
        li.append(i)
        print('given string has 5 char',i)
st(x)
#8
x=input('Enter a string')
def vowel(x):
  char='aeiouAEIOU'
  count=0
  for i in x:
    if i in char:
      count+=1
  print('The vowel count is',count)
vowel(x)'''
#9
num=[1,2,3,4,5,6,7]
def fait(num):
   sum=0
   if (num%2==0):
      return sum(num)
fait(num)

