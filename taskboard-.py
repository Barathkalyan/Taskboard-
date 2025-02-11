#Source code for TasksBoard+

import mysql.connector as mysql 

mydb = mysql.connect(host="localhost", user="root", passwd="root") 
mycursor = mydb.cursor() 

try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS Employee") 
    mycursor.execute("USE Employee") 

    # Creating a table for employee details
    mycursor.execute("""CREATE TABLE IF NOT EXISTS emp (
        Emp_ID INT PRIMARY KEY,
        Name VARCHAR(15),
        Age INT,
        Designation VARCHAR(120)
    )""")

    mycursor.execute("""INSERT INTO emp VALUES
        (100, 'ADMIN', 52, 'Admin'),
        (101, 'Bhuvanesh', 34, 'Jr.Tester'),
        (102, 'Harish', 45, 'Sr.Tester'),
        (103, 'Rohit', 60, 'Debugging'),
        (104, 'Tharshan', 23, 'Developer'),
        (105, 'Roshan', 45, 'Product Manager'),
        (106, 'Pranav', 56, 'Project Manager'),
        (107, 'Jagadish', 32, 'HR Manager'),
        (108, 'Adharv', 44, 'Data Analyst'),
        (109, 'Siva', 31, 'Program analyst'),
        (110, 'Barath', 50, 'Full stack developer')
    """)
    mydb.commit()

    # Creating tables for tasks and task completion
    mycursor.execute("""CREATE TABLE IF NOT EXISTS Tasks (
        Emp_ID INT,
        Taskname VARCHAR(50),
        Deadline DATE,
        PRIMARY KEY (Emp_ID, Taskname)
    )""")

    mycursor.execute("""CREATE TABLE IF NOT EXISTS Comptasks (
        Emp_ID INT,
        Taskname VARCHAR(50),
        Comp_status VARCHAR(3),
        PRIMARY KEY (Emp_ID, Taskname)
    )""")
except mysql.Error as e:
    print("Database Error:", e)  

# Function to add a new employee
def New_Employee():
    e_id = int(input("Enter Admin ID: ")) 
    if e_id == 100:
        def Emp():
            eid = int(input("Enter Employee ID: ")) 
            name = input("Enter Employee Name: ") 
            age = int(input("Enter Employee Age: ")) 
            desig = input("Enter Employee Designation: ") 
            return eid, name, age, desig
        
        while True:
            ch = input("Do you want to add new employees? (y/n): ").lower()
            if ch != 'n': 
                num = int(input("Enter the number of employees to add: ")) 
                for _ in range(num):                    
                    try:
                        mycursor.execute("INSERT INTO emp VALUES (%s, %s, %s, %s)", Emp()) 
                        mydb.commit()
                        print("Details added successfully!") 
                    except mysql.Error as e:
                        print("Error:", e) 
            else: 
                break
    else: 
        print("Invalid Admin ID.") 

# Function to add a new task for an employee
def Insert_Tasks(): 
    e_id = int(input("Enter Admin ID: ")) 
    if e_id == 100: 
        def Emp_works():
            eid = int(input("Enter Employee ID: ")) 
            task = input("Enter the task: ") 
            dline = input("Enter the deadline (YYYY-MM-DD): ") 
            return eid, task, dline
        
        while True:
            ch = input("Do you want to add tasks? (y/n): ").lower()
            if ch != 'n':
                n = int(input("Enter the number of employees: ")) 
                for _ in range(n): 
                    try: 
                        mycursor.execute("INSERT INTO Tasks VALUES (%s, %s, %s)", Emp_works()) 
                        mydb.commit() 
                        print("Record added.")
                    except mysql.Error as e:
                        print("Error:", e)
            else: 
                break
    else: 
        print("Invalid Admin ID.") 

# Function to update tasks
def Update_Tasks(): 
    e_id = int(input("Enter Admin ID: ")) 
    if e_id == 100:
        mycursor.execute("SELECT Emp_ID, Taskname FROM Tasks")
        rec = mycursor.fetchall()
        print("Available tasks to update:", rec)

        def update():
            eid = int(input("Enter Employee ID: ")) 
            taskname = input("Enter the task: ") 
            dline = input("Enter new deadline (YYYY-MM-DD): ") 
            return taskname, dline, eid
        
        while True:
            ch = input("Do you want to update tasks? (y/n): ").lower()
            if ch != 'n':
                n = int(input("Enter the number of employees: ")) 
                for _ in range(n):
                    mycursor.execute("UPDATE Tasks SET Taskname=%s, Deadline=%s WHERE Emp_ID=%s", update()) 
                    mydb.commit()
                print("Records updated.") 
            else: 
                break
    else: 
        print("Invalid Admin ID.") 

# Function to delete an employee
def Del_Emp():
    e_id = int(input("Enter Admin ID: ")) 
    if e_id == 100:
        while True:
            ch = input("Do you want to delete employee details? (y/n): ").lower()
            if ch != 'n':
                eid = int(input("Enter Employee ID to delete: ")) 
                try:
                    mycursor.execute("DELETE FROM emp WHERE Emp_ID=%s", (eid,)) 
                    mycursor.execute("DELETE FROM Tasks WHERE Emp_ID=%s", (eid,)) 
                    mycursor.execute("DELETE FROM Comptasks WHERE Emp_ID=%s", (eid,))
                    mydb.commit()
                    print("Employee record deleted.")
                except mysql.Error as e:
                    print("Error:", e)
            else: 
                break
    else: 
        print("Invalid Admin ID.") 

# Function to check task completion
def Task_Comp():
    e_id = int(input("Enter Admin ID: ")) 
    if e_id == 100:
        mycursor.execute("SELECT * FROM Comptasks")
        rec = mycursor.fetchall() 
        print("Completed Tasks:", rec if rec else "No tasks completed.")
    else: 
        print("Invalid Admin ID.") 

# Employee functions
def Emp_Login(): 
    eid = int(input("Enter your Employee ID: "))
    mycursor.execute("SELECT * FROM Tasks WHERE Emp_ID=%s", (eid,))
    rec = mycursor.fetchall()
    print("Your Tasks:", rec if rec else "No tasks assigned.")

def Emp_com():
    while True: 
        ch = input("Do you want to confirm task completion? (y/n): ").lower()
        if ch != 'n':
            eid = int(input("Enter your Employee ID: ")) 
            task = input("Enter your task: ") 
            comp = input("Is the task completed? (YES/NO): ") 
            if comp.upper() == "YES": 
                mycursor.execute("INSERT INTO Comptasks VALUES (%s, %s, %s)", (eid, task, comp))
                mycursor.execute("DELETE FROM Tasks WHERE Emp_ID=%s AND Taskname=%s", (eid, task))
                mydb.commit()
                print("Task marked as completed.") 
        else: 
            break 

# Main Menu
while True:
    print("1. New Employee\n2. Insert Task\n3. Update Task\n4. Delete Employee\n5. View Task Completion\n6. View Tasks\n7. Confirm Task Completion\n8. Exit")
    ch = int(input("Enter choice: ")) 
    if ch == 1: New_Employee()
    elif ch == 2: Insert_Tasks()
    elif ch == 3: Update_Tasks()
    elif ch == 4: Del_Emp()
    elif ch == 5: Task_Comp()
    elif ch == 6: Emp_Login()
    elif ch == 7: Emp_com()
    elif ch == 8: break
    else: print("Invalid option.")

    else:  
        print("Invalid option. Please select a valid option.") 

        print('--------------------------------------------------------------')
