#loop
'''for i in range(0,11):
    print(i)
for i in range(1,6):
    print(i)
for i in range(-10,-1):
    print(i)
for i in range(-10,-6):
    print(i)
#name in loop
x=('f','a','t','h','i','m','a')
for i in x:
   print(i)
#one value
for i in range(1):
    print(i)
#to add
x=[10,20,30,40,50]
y=0
for i in x:
    y+=i
    print(y)
#to multilpy
x=[10,20,30,40,50]
y=0
for i in x:
    y*=i
    print(y)
#to print even
for i in range(1,21):
     if(i%2)==0:
      print('Even number',i)
    
#to print even in list
x=[12,61,4,38,35,63,70]
for i in range(12,71):
 if(i%2)==0:
    print('Even number',i)
#count upper&lower case
y=0
x=('PyTHoNlaNguAGE')
for i in x:
    if(i.isupper()):
     y+=i.count(i)
print('the count is',y)
y=0
x=('PyTHoNlaNguAGE')
for i in x:
    if(i.islower()):
     y+=i.count(i)
print('the count is',y)'''
#factorial
x=int(input('enter a number'))
y=1
for i in range(1,x+1):
 y=y*i
 print('Factorial of number is',y)

#prime number
x=int(input('enter a number'))
for i in range(1,x+1):
 if (i%2)==1:
  print(i,'its an prime number')



