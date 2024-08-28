#1
#2       
a='venki$321.'
print(a[::-1])
#3
i=[3,4,6,2,1,9,0]
i.sort(reverse=True)
print(i)
#4
dic={'no':80,'no1':55,'no2':34}
a=list(dic.values())
a.sort()
print(a)
#5
import re
x=[{'name':'Fathima','age':25},{'name':'Mohi','age':26}]
x.sort(key=lambda d:d["age"])
print(x)
#7
import re
def valid_gmail(email):
    formate=r'^[a-z0-9+@gmail\.com$]'
    if re.match(formate,email):
        return True
    else:
        return False
x=input("Enter the gmail address:")
if valid_gmail(x):
    print('is valid')
else:
    print('invalid')
#9
x=[12,34,67,5,6,4,3,6,67]
res=list(filter(lambda x:x>5,x))
print(res)
#10
numbers={}
letters={}
comb={}
numbers[1]=56
numbers[3]=7
letters[4]='B'
comb['Numbers']=numbers
comb['Letters']=letters
print(comb)
#11
li=[1,3,4,2,3]
count={}
for i in li:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
#print remove duplicate value
x=list(count.keys())
print(x)

#13
inputdict={"input_data":{"K1":"V1","V2":"K2","K3":"V3","V4":"K4","K5":"V5"}}
keys=list(inputdict["input_data"].keys())
values=list(inputdict["input_data"].values())
output=[",".join(keys),",".join(values)]
print(output)
#15
def pair(ls,k):
    pairs=[]
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i]+ls[j]==k:
                pairs.append((ls[i],ls[j]))
    return pairs

ls=[1,5,3,7,9]
k=12
print(pair(ls,k))
#16
import re
def validate_password(password):
    if len(password) < 8 or len(password) > 16:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[^a-zA-Z0-9]', password):
        return False
    return True
password = input("Enter the valid Password:")
if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
