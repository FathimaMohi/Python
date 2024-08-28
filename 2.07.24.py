#fibonaci(Recursive function)
x=int(input("Enter the  fibonaci series"))
n1=0
n2=1
for i in range(2,x+1):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
#recursive fun
def fib(num):
    if num==0 or num==1:
        return num
    else:
        return fib(num-2)+fib(num-1)
print(fib(6))
 
#list comprehension
res=[i for i in range(1,11)]
print(res)

res=[i for i in range(1,21) if i%2==0]
print(res)

res=[i for i in range(1,21) if i%2==1]
print(res)

res=[i**2 for i in range(1,5)]
print(res)

x=[10,5,21,25,60,20,53]
res=[i for i in x if i%2==0]
print(res)

x=[10,5,21,25,60,20,53]
res=[i for i in x if i%2==1]
print(res)

char=['apple','orange','kiwi','lime','berry']
res=[i for i in char if len(i)<5]
print(res)

x=input("Enter the word")
w=x.split()#to print a continues word
res=[i.upper() for i in w]
print(res)

x=['level','map','madam','one']
res=[i for i in x if (i==i[::-1])]
print(res)

x=input("Enter the word")
v = ['a','e','i','o','u','A','E','I','O','U']
res=[i for i in x if (i in v)]
print(res)

matrix=[1,2,3,
       4,5,6,
       7,8,9]
li=[]
for i in matrix:
        li.append(i)
print(li)

res=[i for i in matrix if i%2==1]
print(res)
res=[i for i in matrix if i%2==0]
print(res)

x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[1,2,3],
   [4,5,6],
   [7,8,9]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        result [i][j]=x[i][j]+y[i][j]
    for r in result:
            print(r)
x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[1,2,3,],
   [4,5,6],
   [7,8,9]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
      for k in range(len(y)):
        result [i][j] += x[i][k]*y[k][j]
    for r in result:
            print(r)

x=[1,2,3,
   4,5,6,
   7,8,9]
y=[1,2,3,
   4,5,6,
   7,8,9]
li1=[]
li2=[]
for i in x:
        li1.append(i)
        li2.append(i)
print(li1,li2)
add=[li1+li2 for i in x if len(x[0])]

