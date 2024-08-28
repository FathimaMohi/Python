students=[]
def add():
    st_name=input("Enter the student name")
    st_id=input("Enter the student Id")
    st_gr=float(input("Enter the CGPA"))
    print("Student details Added successfully")
def remove(st_name,st_id):
    students=[student for student in students if student["id"]!=id]
def update(st_name,st_id):
     for student in students:
         if student["st_name"] == st_name or student["st_id"] == st_id:
             break
def display():
    for student in students:
       print("Student Name:",st_name,"ID:",st_id)
def search():
    for student in students:
     if st_name == st_name or st_id == st_id:
        print("Student Name:",st_name,"ID:",st_id)
     else:
        print("no search found")
while True:
    print("--------------- Student Management System ----------------")
    print("1. Add student")
    print("2. Remove student")
    print("3. Update student")
    print("4. Search student Details ")
    print("5.Display")
    print("6. Exit")
    ch = input("Choose an option: ")
    if ch == "1":
         st_name=input("Enter the student name")
         st_id=input("Enter the student Id")
         st_gr=float(input("Enter the CGPA"))
         print("Student details Added successfully")
         add()
    elif ch == "2":
        st_id=input("Enter student id to remove:")
        remove(st_id)
        print("ID removed")
    elif ch == "3":
        st_name=input("Enter the name to update")
        st_id=input("Enter the new id")
        update(st_name,st_id)
        print("updated successfully")
    elif ch == "4":
        st_name_or_st_id=input("Enter the student name or id to search")
        search(st_name,st_id)
    elif ch == "5":
        display()
    elif ch == "6":
       break
    else:
        print("invalid entry")
