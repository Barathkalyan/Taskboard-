#Source code for TasksBoard+

import mysql.connector as mysql 
mydb=mysql.connect(host="localhost",user="root",passwd="root") 
#mydb=mysql.connect(host="localhost",user="root",passwd="root",database="Employee") 
mycursor=mydb.cursor() 
                        
try:
    mycursor.execute("Create database Employee") 
    mycursor.execute("Use employee") 
    #Creating a table for employee's details: 
    mycursor.execute("create table emp(Emp_ID int(3) primary key,Name varchar(15),age integer,Designation varchar(120))")
    mycursor.execute("insert into emp values(100,'ADMIN',52,'Admin'),\ (101,'Bhuvanesh',34,'Jr.Tester'),(102,'Harish',45,'Sr.Tester'),\
(103,'Rohit',60,'Debugging'),(104,'Tharshan',23,'Developer'),(105,'Roshan',45,'Product Manager'),(106,'Pranav',56,'Project Manager'),\
(107,'Jagadish',32,'HR Manager'),(108,'Adharv',44,'Data Analyst'),(109,'Siva',31,'Program analyst'),\
(110,'Barath',50,'Full stack developer')")
    mydb.commit() 

    #Creating table to store employee's tasks:
    mycursor.execute("Create table Tasks(Emp_Id integer primary key,Taskname varchar(20),Deadline date)") 
    #Creating table to enter the status of the employee's tasks: 
    mycursor.execute("Create table Comptasks(Emp_ID integer primary  key,Comp_status varchar(3))")
except:
    print()  

#Function to add a new Employee: 
def New_Employee(): 

    e_id=int(input("Enter Admin ID:")) 
    if e_id==100:
        def Emp(): 
            eid=int(input("Enter Employee's ID:")) 
            name=input("Enter Employee's name:") 
            age=int(input("Enter Employee's age:")) 
            desig=str(input("Enter Employee's designation:")) 
            return eid,name,age,desig
        while True:
            print("Do you want to add new Employees?") 
            ch=input("Enter your option (y/n)?") 
            if ch.lower()!='n' 
                num=int(input("Enter the number of Employees to be added:")) 
                for i in range(num):                    
                    try:
                        mycursor.execute("Insert into emp values(%s,%s,%s,%s)",Emp()) 
                        mydb.commit() 
                        print("Details added successfully!") 
                    except:
                        print("Given ID is already in use. Please enter a valid ID.") 
            else: 
                break
    else: 
        print("Invalid Admin ID.") 
#Function to add a new task for an employee:       
def Insert_Tasks(): 
    e_id=int(input("Enter Admin ID:")) 
    if e_id==100: 
        def Emp_works():
            
            eid=int(input("Enter Employee ID:")) 
            task=str(input("Enter the task:")) 
            dline=str(input("Enter the deadline:")) 
            return eid,task,dline
        
        while True:
            
            print("Do u want to add tasks?") 
            ch=input("Enter the option (y/n)?") 
            if ch.lower()!='n':
                
                n=int(input("Enter the number of employees:")) 
                for i in range(n): 

                    try: 

                        mycursor.execute("Insert into Tasks values(%s,%s,%s)",Emp_works()) 
                        mydb.commit() 
                        print("Record added.")
                        
                    except: 

                        print("Given ID already has a task.")
                        
            else: 
                break
            
    else: 
        print("Invalid Admin ID.") 

#Function to update/revamp a task for an employee:
        
def Update_Tasks(): 

    e_id=int(input("Enter Admin ID:")) 
    if e_id==100:
        
        mycursor.execute("Select Emp_ID from tasks")
        rec=mycursor.fetchall() 
        print("The ID's available to update are:") 
        l=[]
        for i in rec: 

            l.append(list(i))
            
        for i in l: 

            print(i,end=' ')
            
        print() 

        def update(): 

            eid=int(input("Enter ID:")) 
            tname=str(input("Enter the task:")) 
            dline=str(input("Enter Date of submission:")) 
            adata=[tname,dline,eid]     
            return adata
        
        while True:
            
            print("Do u want to update the tasks?") 
            ch=input("Enter the option (y/n)?") 
            if ch.lower()!='n':
                
                n=int(input("Enter the number of employees:")) 
                for i in range(n):
                    
                    mycursor.execute("Update tasks set taskname=%s,Deadline=%s where Emp_ID=%s",update()) 
                    mydb.commit()
                print("Records updated.") 

            else: 
                break
            
    else: 
        print("Invalid Admin ID.") 

#Function to delete the details of an employee:
        
def Del_Emp():
    
    e_id=int(input("Enter Admin ID:")) 
    mycursor.execute("Select Emp_ID from emp") 
    rec=mycursor.fetchall() 
    print("The ID's available to delete are:") 
    l=[] 
    for i in rec: 

        if i[0]==100: 

            continue 

        l.append(list(i))
        
    for i in l: 

        print(i,end=' ') 

    print() 

    if e_id==100: 

        while True:
            
            print("Do you want to delete details of an employee?") 
            ch=input("Enter the option (y/n)?") 
            if ch.lower()!='n':
                
                n=int(input("Enter the number of employees to be deleted:")) 
                for i in range(n): 

                    eid=int(input("Enter ID to delete data:")) 
                    l=[eid] 
                    mycursor.execute("Delete from emp where Emp_ID=%s",l) 
                    mycursor.execute("Delete from tasks where Emp_ID=%s",l) 
                    mydb.commit()
                    
                print("Records deleted.") 

            else: 
                break
            
    else: 

        print("Invalid Admin ID.") 

#Function to view the Completion of tasks:
        
def Task_Comp(): 

    EID=int(input("Enter Admin ID:")) 
    if EID==100:
        
        mycursor.execute("select * from comptasks") 
        rec=mycursor.fetchall() 
        if rec==[]: 

            print("Tasks not completed yet.") 
        else: 
            print(rec) 

    else: 
        print("Invalid Admin ID.") 

#Function to view the tasks:
        
def Emp_Login(): 

    def Works():
        
        e_id=int(input("Enter your ID:"))
        l=[e_id] 
        return l
    
    while True:
        
        print("Do u want to view the tasks?") 
        ch=input("Enter the option (y/n):") 
        if ch.lower()!='n':
        
            n=int(input("Enter the no. of employees to view their works:")) 
            for i in range(n): 

                mycursor.execute("Select * from tasks where Emp_ID=%s",Works()) 
                rec=mycursor.fetchall() 
                flag=False 
                for x in rec:
                    
                    print(x) 
                    flag=True 

                if flag==False:
                    
                    print("No tasks") 

        else: 

            break 

#Function to check whether task is completed or not 

def Emp_com():
    
    while True: 

        print("Do you want to confirm the submission of your task?") 
        ch=input("Enter the choice(y/n):") 
        if ch!='n':
            
            eid=int(input("Enter your ID:")) 
            task=str(input("Please enter your task:")) 
            comp=str(input("Is the task completed?(YES/NO):")) 
            a=[eid,task] 
            l=[eid,comp]
            
            try:
                
                if comp=='YES': 

                    mycursor.execute("Insert into comptasks values(%s,%s)",l) 
                    mycursor.execute("Delete from tasks where Emp_ID=%s and Taskname=%s",a)
                    mydb.commit()
                    
                else:
                    
                    print("Complete the task soon and update.") 

            except:
                
                print("Task Completion already confirmed.") 

        else: 

            break 

#Menu to use the aforementioned functions: 


print("_________"*8) 

print("\t\t\t\t - Welcome to Tasksboard+ - ") 

print("_________"*8) 

print("============================") 

print("\t    Admin Mode:") 

print("============================") 

print() 

print("->1. New Enrollment") 

print("->2. Inserting tasks") 

print("->3. Updating tasks") 

print("->4. Disenrollment") 

print("->5. Check Completion Of Tasks") 

print() 

print("============================") 

print("\tEmployee Mode:") 

print("============================") 

print() 

print("->6. Viewing Tasks") 

print("->7. Confirmation of completion of Tasks") 

print("->8. Exit") 

print() 

print('-------------------------------------------------------') 

  

while True:
    
    ch=int(input("Enter your choice of operation (1-8) :")) 
    print('-------------------------------------------------------') 
    if ch==1:
        
        print("Enrollment of New Employee......") 

        print('-------------------------------------------------------') 

        New_Employee() 

        print('-------------------------------------------------------') 

    elif ch==2:
        
        print("Inserting Task For Employee......") 

        print('-------------------------------------------------------') 

        Insert_Tasks() 

        print('-------------------------------------------------------')
        
    elif ch==3: 

        print("Updating Task Of Employee......") 

        print('-------------------------------------------------------') 

        Update_Tasks() 

        print('-------------------------------------------------------') 

    elif ch==4:
        
        print("Disenrollment Of Employee......") 

        print('-------------------------------------------------------') 

        Del_Emp() 

        print('-------------------------------------------------------') 

    elif ch==5:
        
        print("Viewing The Completion Of Tasks......") 

        print('-------------------------------------------------------') 

        Task_Comp() 

        print('-------------------------------------------------------') 

  

    elif ch==6:
        
        print("Viewing The Tasks Of Employees......") 

        print('-------------------------------------------------------') 

        Emp_Login() 

        print('-------------------------------------------------------') 

    elif ch==7:
        
        print("Confirming The Completion Of Tasks......") 

        print('-------------------------------------------------------') 

        Emp_com() 

        print('-------------------------------------------------------') 

    elif ch==8:
        
        mycursor.execute("Delete from comptasks") 

        mydb.commit() 

        print("_________"*4) 

        print("\t\t\t\t\t   Thank You") 

        print("_________"*4) 

        break 

    else:  
        print("Invalid option. Please select a valid option.") 

        print('--------------------------------------------------------------')
