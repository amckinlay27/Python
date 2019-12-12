#Adam McKinlay - c0656685
#Date: 2019-12-04
#Chapter 10: Q7 - Main

from Employee import Employee
import pickle

def main():
    #Read in data
    inputFile = open('employees.dat', 'rb')
    endOfFile = False
    
    while not endOfFile:
        try:
            roster = pickle.load(inputFile)
        except EOFError:
            endOfFile = True
    inputFile.close()
    #End of read in data
    
    outputFile = open('employees.dat', 'wb')

    falg = 0
    while falg != 5:
        #Display Prompt
        prompt()
        
        #Get customers options
        choice = int(validateNum("\nWhat would you to do? (1-5)", "Option", 1 ,5))
        falg = choice

        #Option 1
        if(choice == 1):
            employeeID = int(validateNum("\nEnter employee ID to search for. (40000-49999)", "ID", 40000, 49999))
            result = roster.get(employeeID, 'Employee not found')
            if(result == 'Employee not found'):
                print(result)
            else:
                print("Employee Info\n..................")
                print(result)

        #Option 2
        elif(choice == 2):
            employeeName = input("Enter employee name: ")
            employeeID = int(validateNum("Enter new employee id. (40000-49999)", "ID", 40000, 49999))
            department = input("Enter department: ")
            role = input("Enter role: ")

            newEmployee = Employee(employeeName, employeeID, department, role)
            roster[employeeID] = newEmployee
            print("Employee added.")

        #Option 3
        elif(choice == 3):
            employeeID = int(validateNum("Enter employee id to change. (40000-49999)", "ID", 40000, 49999))
            employeeName = input("Enter employee name: ")
            department = input("Enter department: ")
            role = input("Enter role: ")

            employee = roster.get(employeeID, 'Employee not found')
            employee.setName(employeeName)
            employee.setDept(department)
            employee.setJob(role)
            
            roster[employeeID] = employee
            print("Employee updated.")
            
        #Option 4
        elif(choice == 4):
            employeeID = int(validateNum("Enter employee id to delete. (40000-49999)", "ID", 40000, 49999))
            if employeeID in roster:
                del roster[employeeID]
                print("Employee Deleted")
            else:
                print("Employee does not exist")
    pickle.dump(roster, outputFile)
    outputFile.close()

#Displays user prompt
def prompt():
    print("\nAvialabe Options...")
    print("1. Lookup Employee")
    print("2. Add New Employee")
    print("3. Change existing employee")
    print("4. Delete Employee")
    print("5. Exit")

#Prevents value casting error and ensures input within range
def validateNum(phrase, focus, lower, upper):
    try:
        num = int(input(phrase))
        while num < lower or num > upper:
            print("Error: You must enter ", lower, " to ", upper, ". Please try again", sep='')
            num = int(input(phrase))
        return num

    #Handle String Input -> rec
    except ValueError:
        print("ERROR:", focus, "must be an integer. Plase try agian")
        return validateNum(phrase, focus, lower, upper)


#Call Main      
main()
