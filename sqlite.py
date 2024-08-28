import sqlite3
conn=sqlite3.connect("D:\\new db\\aruvi.sqlite3")
con=conn.cursor()
print('opened Database successfully')
con.close()

conn=sqlite3.connect("D:\\new db\\aruvi.sqlite3")
con=conn.cursor()
con.execute('''create table student
            (ID int PRIMARY KEY NOT NULL,
             Name text NOT NULL,
             Age int NOT NULL,
             Address char(100) NOT NULL
             mark int);''')
cursor.close() 
conn=sqlite3.connect("D:\\new db\\aruvi.sqlite3")
con=conn.cursor()
con.execute("INSERT INTO student VALUES(101,'fathima',20,'1/67,veerasumdrum',56)");
con.execute("INSERT INTO student VALUES(102,'mohi',20,'1/67,veerasumdrum',67)");
con.execute("INSERT INTO student VALUES(103,'basi',20,'1/67,veerasumdrum',45)");
cursor.close() 
