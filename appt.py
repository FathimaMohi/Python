def missing(l):
    s=sum(l)
    n=len(l)+1
    actualsum=(n*(n+1))//2
    result=actualsum-s
    return result
l=[4,3,1,5,6]
print(missing(l))

x=[1,2,3,4]
x.reverse()
print(x)
