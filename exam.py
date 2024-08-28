'''print([i+j for i in "abc" for j in "def"])

for  i in range(5):
    if i==5:
        break
    else:
        print(i)
class A:
    def one(self):
        return self.two()
    def two(self):
        return 'A'
class B(A):
    def two(self):
        return 'B'
obj1=A()
obj2=B()
print(obj1.two(),obj2.two())'''

li1=['']*3
print(len(li1))

n=['python','list','dict']
print(n[-1][-1])

'''class Test:
    def __int__(self):
        self.x=0
class Derived_test1(Test):
    def __init__(test):
        Test.__init__(self)
        self.y=1
    def main():
        b=Derived_test()
        print(b.x,b.y)
    main()'''
def sum(*args):
    r=0
    for i in args:
        r+=i
    return r
print(sum(1,2,3))
print(sum(1,2,3,4,5))
print('xyyxyyxyxyxxy'.\
        replace('xy','12',100))
a=[0,1,2,3]
for a[-1] in a:
    print(a[-1])

a={5,4}
b={1,2,3,4,5}
a>b

import re
a=re.sub('morning','evening','good morning')
print(a)
a=(lambda x, y: x if x<y else y)
print(a(101*99,102*98))

'''x= 'abcd'
for i in range(len(x)):
    print(i.upper())
True=False
while True:
    print(True)
    break'''
'''print("abcdef".center(7,1))'''
