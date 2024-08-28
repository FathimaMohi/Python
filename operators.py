#operators
#arithmetic

m=int(input('Enter First Number'))
n=int(input('Enter second Number'))
o=m+n
print('output is',o)

m=int(input('Enter First Number'))
n=int(input('Enter second Number'))
o=m-n
print('output is',o)

m=int(input('Enter First Number'))
n=int(input('Enter second Number'))
o=m*n
print('output is',o)

m=int(input('Enter First Number'))
n=int(input('Enter second Number'))
o=m/n
print('output is',o)

m=int(input('Enter First Number'))
n=int(input('Enter second Number'))
o=m%n
print('output is',o)

m=int(input('Enter First Number'))
n=int(input('Enter second Number'))
o=m//n
print('output is',o)

m=int(input('Enter First Number'))
n=int(input('Enter second Number'))
o=m**n
print('output is',o)

#membership
x=[1,2.2,'True',3,4,5]
print(2.2 in x)
print('True' not in x)

#identity operator
x={1,2,3,4}
y={1,2,3,4}
print(x in y)
print(id(x))
print(id(y))
x=y
print(x is y)

#logical operator(Binary)
print(bin(8))
print(int('1000',2))

#lo(And,or,not)
print(bin(80))
print(int('1000',2))
print(int('1010000',2))
a=50
print(a>100 and a<75)
print(a>100 or a<75)
print(not(a>100 and a<75))

#assignment
x=5
x+=5
x=x+5
print('sum of no',x)
