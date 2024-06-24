#given char alphabet or digir or spl char
x=input('Enter the charater')
if x.isalpha():
      print('this is alphabet')
elif x.isdigit():
     print('this is digit')
else:
    print('this is spl character')
#armstrong
x=int(input('Enter the number'))
if is_armstrong_number(x):
 print('its an armstrong number')
else:
 print('its not an armstrong number')
#century
yr=int(input("Enter the year"))
if(yr%100)==0:
       print('its an century year')
else:
    print('its not an century year')
#condition
x=int(input('Enter a Number'))
if x==0:
    print('no is 0')
elif x>0:
    print('no is >0')
else:
    print('no is negative')
#vowel
x=input('Enter a letter')
print(x)
y=['a','e','i','o','u','A','E','I','O','U']
if x in y:
    print('vowel')
else:
    print('not a vowel')
#days
x=int(input('enter a number'))
if x==1:
      print('monday')
elif x==2:
      print('tuesday')
elif x==3:
      print('Wednesday')
elif x==4:
      print('thursday')
elif x==5:
      print('friday')
elif x==6:
      print('saturday')
elif x==7:
      print('sunday')
else:
    print('nothing')
#divisible
x=int(input("enter a number"))
if (x%2)==0:
      print('divisible by 2')
elif (x%3)==0:
      print('divisible by 3')
elif (x%2&3)==1:
      print('non divisible by 2 and 3')
elif (x%2&3)==0:
      print(' divisible by 2 and 3')
else:
      print('nothing')
      
x=int(input("enter a number"))
if (x%3)&(x%5)==0:
      print('divisible by 3 and 5')
else:
      print('non divisible')
#large shot
ls=[0,1,2,3,4,55,66,77,88]
print('Maximum',max(ls))
print('Minimum',min(ls))
#leapyear
yr=int(input("Enter the year"))
if(yr%4)==0:
       print('its an leap year')
else:
    print('its not an leap year')

#nested if
x=int(input('Enter a number'))
y=int(input('Enter a number'))
z=int(input('Enter a number'))
if x>y:
      if x>z:
       print('x is greater than z')
      else:
       print('z is greater than x')
else:
    print('y is grater than x')

x=int(input('Enter a Number'))
if x==0:
    print('no is 0')
elif x>0:
    print('no is >0')
else:
    print('no is negative')
#odd or even
x=int(input("Enter a number"))
print(x)
if (x%2)==0:
    print('the no is even')
else:
    print('the no is odd')
#calculation
print('select operation')
print('1.Addition operation')
print('2.Subraction operation')
print('3.multiplication operation')
print('4.division operation')
ch=int(input('Enter a choice'))
if ch in (1,2,3,4):
  a=int(input('enter a 1 number '))
  b=int(input('enter a 2 number '))
  if ch==1:
    print (a+b)
  elif ch==2:
    print (a-b)
  elif ch==3:
    print (a*b)
  elif ch==4:
    print (a%b)
  else:
    print('nothing')
else:
    print('nothing')
#palindrom
x=input('enter a word :')
if (x==x[::-1]):
    print("its a palindrom")
else:
    print("its not a palindrom")

x='malayalam'
y='malayalam'
if(x==y):
  print('malayalm is a palindrom' )
else:
  print('malayalam is not a palindrom')
    
#prime numbers
x=int(input('enter a number'))
if (x%2)==1:
 print('its an prime number')
else:
 print('its not an prime number')
#vowel or consonant
x=input('Enter a letter')
print(x)
y=['a','e','i','o','u','A','E','I','O','U']
if x in y:
    print('it is vowel')
else:
    print('it is an consonant')



       


