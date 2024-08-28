import sqlite3
'''conn=sqlite3.connect('E:\\python pro\\data.sqlite')
con=conn.cursor()
print('Opened Database Successfully')
con.close()
#sql is not a case sensitive language
conn=sqlite3.connect('E:\\python pro\\data.sqlite')
con=conn.cursor()'''
#con.execute('''create table student
            #(ID int primary key not null,
            #name text not null,
            #age int not null,
            #address char(50)not null,
            #marks int);''')
#con.close()

'''conn=sqlite3.connect('E:\\python pro\\data.sqlite')
con=conn.cursor()
con.execute("INSERT INTO student VALUES(101,'harani',24,'20,9th Street,Tenkasi',87)");
con.execute("INSERT INTO student VALUES(102,'ani',22,'67,kovilstreet,Tenkasi',89)");
con.execute("INSERT INTO student VALUES(103,'dhanu',26,'10,8th Street,madurai',87)");
con.execute("INSERT INTO student VALUES(104,'fathi',23,'45,kalindhasan,chennai',89)");
con.execute("INSERT INTO student VALUES(105,'fathi',25,'45,palayamkottai,Tirunelveli',66)");
conn.commit()
con.close()
conn = sqlite3.connect('E:\\python pro\\data.sqlite')
cursor = conn.cursor()
for row in cursor.execute("select*from student"):
    print(row)
conn.commit()
conn.close()

import sqlite3
conn = sqlite3.connect('E:\\python pro\\data.sqlite')
cursor = conn.cursor()
for row in cursor.execute("SELECT ID, NAME,ADDRESS,marks from student"):
    print("ID = ", row[0])
    print("NAME = ",row[1])
    print("ADDRESS = ",row[2])
    print("MARKS = ",row[3], "\n")
conn.commit()
conn.close()

conn = sqlite3.connect('E:\\python pro\\data.sqlite')
cursor = conn.cursor()
conn.execute('update student set marks=70 where ID=101')
conn.commit()
for row in cursor.execute("select* from student"):
    print(row)
conn.commit()
conn.close()

conn = sqlite3.connect('E:\\python pro\\data.sqlite')
cursor = conn.cursor()
conn.execute('UPDATE STUDENT set NAME="grtty" where ID=103')
conn.commit()
for row in cursor.execute("SELECT ID,NAME,ADDRESS,marks from student"):
    print("ID = ",row[0])
    print("NAME = ",row[1])
    print("marks = ",row[2])
    print("ADDRESS = ",row[3],"\n")
conn.commit()
conn.close()

conn = sqlite3.connect('E:\\python pro\\data.sqlite')
cursor = conn.cursor()
conn.execute('DELETE from student where ID=103')
conn.commit()
for row in cursor.execute("SELECT ID,NAME,ADDRESS,marks from student"):
    print("ID = ",row[0])
    print("NAME = ",row[1])
    print("marks = ",row[2])
    print("ADDRESS = ",row[3],"\n")
conn.commit()
conn.close()'''

conn = sqlite3.connect('E:\\python pro\\data.sqlite')
print('Enter Student ID:')
r=input()
print('Enter Student Name:')
sn=input()
print('Enter Student Address:')
sad=input()
print('Enter Student Marks:')
sm=input()
query="insert into student (ID,NAME,ADDRESS,marks) values ("',' + r + "','" + sn + "','" + sad + "','" + sm + "')"
conn.execute(query)
conn.commit()
conn.close()
print('Data Saved')

'''conn = sqlite3.connect('E:\\python pro\\data.sqlite')
print('Enter Student Roll Number,which you want to Update:')
r=input()
print('Enter Student Address, which you want to Update:')
ad=input()
query="update student set ADDRESS='" + ad + "' where ID=" + r
conn.execute(query)
conn.commit()
conn.close()
print('Data Saved')

import sqlite3
conn = sqlite3.connect('E:\\python pro\\data.sqlite')
cursor = conn.cursor()
query = "select *from student"
cursor.execute(query)
data=cursor.fetchall()
print("Type of data is:",type(data))
print('\n')
print(data)
conn.close()'''
