# Task 1 - Read the data from the file and display it in the terminal
# Task 2 - You have to check whether the file exists or not then only display the data from the file to the terminal 
# Task 3 - Take the inputs from the user, save those inputs in the file and then display those inputs in the terminal
import os
def readFile():
    fObject = open("EmpData.txt", 'r')
    data = fObject.read()
    print(data)

def checkfile():
    if not os.path.exists("EmpData.txt"):
        print("File Does Not Exists!")
    else:
        print("Wow..File Exists!")
checkfile()

def userInput():
    empName = input("Enter employee name: ")
    empDepart = input("Enter Department name: ")
    empSalary = int(input("Enter Salary: "))

    return empName,empDepart,empSalary

def writeFile(empName,empDepart,empSalary):
    fObject = open("EmpData.txt",'a')
    data = "\n" + empName + "\t" + empDepart + "\t" + str(empSalary)
    fObject.write(data)

empName,empDepart,empSalary = userInput()
writeFile(empName,empDepart,empSalary)
readFile()

#Search User

def SearchUser(userName):
    fObject = open("EmpData.txt",'r')
    for line in fObject:
        name = line.split("\t")
        if name[0] == userName:
            print(line)
        
# flag = input("Do you want to search employees: ")
# if flag == "y":
#     readFile()
userName = input("Search Employee by Name: ")
SearchUser(userName)
    