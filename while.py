'''#while loop
i=0
while(i<=5):
    print(i)
    i+=1
#1
i=0
while(i<=20):
    print(i)
    i+=1
#2
i=-10
while(i<=-5):
    print(i)
    i+=1
#3
i=-10
while(i<=-1):
    print(i)
    i+=1
#name
x='fathima'
i=0
while(i<len(x)):
    print(x[i])
    i+=1
i=0
while (i<=20):
    i+=1
    if (i%2)==1:
      print(i)
      
i=0
while (i<=20):
    i+=1
    if (i%2)==0:
      print(i)
x=int(input('Enter the number'))
y=1
while x>=1:
  y*=x
  x-=1
  print('Factorial of number is',y)
#break
for i in range(11):
  if i==7:
    break
  print(i)
#while break
i=0
while(i<=11):
  i+=1
  if i==7:
    break
  print(i)
#continue
for i in range(11):
  if i==7:
    continue
  print(i)
#pass
for i in range(11):
  if i==7:
    pass
  print(i)
#while continue
i=0
while(i<=11):
  i+=1
  if i==7:
    continue
  print(i)
#print 1st 4 letters of ur name(for loop)
x='Fathima'
for i in x:
  if i=='i':
    break
  print(i)
#skip 5th char from ur name(for loop)
x='Fathima'
for i in x:
  if i=='i':
    continue
  print(i)'''
x='jubliee'
for i in x:
  if i=='e':
   break
  print(i)
      
