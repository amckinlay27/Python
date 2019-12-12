#PART 01: Implement UML for each subclass
class Employee:
    def __init__(self, first_name, last_name, SIN, managedBy):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__SIN = SIN
        self.__managedBy = managedBy

    def getFirstName(self):
        return self.__first_name

    def setFirstName(self, first_name):
        self.__first_name = first_name

    def getLastName(self):
        return self.__last_name

    def setLastName(self, last_name):
        self.__last_name = last_name

    def getSIN(self):
        return self.__SIN

    def setSIN(self, SIN):
        self.__SIN = SIN

    def getManager(self):
        return self.__managedBy

    def setManager(self, manager):
        self.__managedBy = manager

    def equals(self, e):
        if(e.getSIN == self.getSIN):
            return true
        else:
            return false

    def __str__(self):
        return "Name: " + self.__last_name + ", " + self.__first_name + "\nSIN: " + str(self.__SIN) + "\n"

class SalariedEmployee(Employee):
    def __init__(self, first, last, SIN, managedBy, salary):
        Employee.__init__(self, first, last, SIN, managedBy)
        self.__salary = salary

    def getSalary(self):
        return self.__salary

    def setSalary(self, salary):
        self.__salary = salary

    def earnings(self):
        return self.__salary

    def __str__(self):
        return "Type: Salaried\n" + Employee.__str__(self) + "Weekly Salary $" +  str(self.__salary) + "\n"

class HourlyEmployee(Employee):
    def __init__(self, first, last, SIN, managedBy, hours, rate):
        Employee.__init__(self, first, last, SIN, managedBy)
        self.__hours = hours
        self.__hourlyRate = rate

    def getHours(self):
        return self.__hours

    def setHours(self, hours):
        self.__hours = hours

    def getRate(self):
        return self.__hourlyRate

    def setRate(self, rate):
        self.__hourlyRate = rate

    def earnings(self):
        if(self.__hours > 40):
            temp = 0
            earnings = 0
            temp = (self.__hours - 40)

            earnings = (40 * self.__hourlyRate) + (temp * (self.__hourlyRate*1.5))
            return earnings
        else:
            return (self.__hours*self.__hourlyRate)

    def __str__(self):
        return "Type: Hourly\n" + Employee.__str__(self) + "Hourly Rate: $" +  str(self.__hourlyRate) + "\nHours Worked: " +  str(self.__hours) + "\n"

class ComissionEmployee(Employee):
    def __init__(self, first, last, SIN, managedBy, rate, sales):
        Employee.__init__(self, first, last, SIN, managedBy)
        self.__commissionRate = rate
        self.__grossSales = sales

    def getCommissionRate(self):
        return self.__commissionRate
        
    def setCommissionRate(self, r):
        self.__commissionRate = r
        
    def getGrossSales(self):
        return self.__grossSales
        
    def setGrossSales(self, s):
        self.__grossSales = s

    def earnings(self):
        return (self.__commissionRate * self.__grossSales)

    def __str__(self):
        return "Type: Commission\n" + Employee.__str__(self) + "Gross Sales: $" +  str(self.__grossSales) + "\nCommission Rate: " +  str(self.__commissionRate) + "\n"

#PART 02 Create main program called payrollTester and display proper output
def payrollTester():
    emp1 = SalariedEmployee("Joe", "Francis", 123456789, None, 2500)
    emp2 = SalariedEmployee("Samamtha", "Hughes", 444555666, emp1, 1400)
    emp3 = HourlyEmployee("Kim", "Adams", 888999000, emp1, 42, 18.50)
    emp4 = ComissionEmployee("Ryan", "Goodall", 111222333, emp2, 0.10, 9000)
    highestPaid = None
    highestPay = 0
    lowestPaid = None
    lowestPay = 10000000
    salEmp = 0
    hourEmp = 0
    commissionEmp = 0
    totalPay = 0
    

    employees = [emp1,emp2,emp3,emp4]

    for emp in employees:
        print(emp,"TOTAL: $",format(emp.earnings(), '.2f'), "\n-------------------------------\n", sep='', end='')

        if(emp.earnings() > highestPay):
            highestPay = emp.earnings()
            highestPaid = emp

        if(emp.earnings() < lowestPay):
            lowestPay = emp.earnings()
            lowestPaid = emp

        if(str(type(emp)) == "<class '__main__.HourlyEmployee'>"):
            hourEmp +=1

        if(str(type(emp)) == "<class '__main__.SalariedEmployee'>"):
            salEmp +=1

        if(str(type(emp)) == "<class '__main__.ComissionEmployee'>"):
            commissionEmp +=1

        totalPay += emp.earnings()

    print("SUMMARY STATISTICS")
    print("Highest Paid Employee:", highestPaid.getLastName(), ",", highestPaid.getFirstName())
    print("Lowest Paid Employee:", lowestPaid.getLastName(), ",", lowestPaid.getFirstName())
    print("Number of salaried employees:",salEmp)
    print("Number of Hourly employees:",hourEmp)
    print("Number of Commission employees:",commissionEmp)
    print("Total for Pay Period: $", format(totalPay, '.2f'), sep='')
    print("-------------------------------")

#PART 03 Implemenet class Workforce
class WorkForce():
    def __init__(self):
        self.__employees = []

    def addEmp(self, emp):
        self.__employees.append(emp)
        
    def delEmp(self, emp):
        self.__employees.remove(emp)

    def findMaxEarner(self):
        maxWage = 0
        maxEmp = None
        for emp in self.__employees:
            if(emp.earnings() > maxWage):
                maxWage = emp.earnings()
                maxEmp = emp
        return maxEmp

    def findMinEarner(self):
        minWage = 1000000
        minEmp = None
        for emp in self.__employees:
            if(emp.earnings() < minWage):
                minWage = emp.earnings()
                minEmp = emp
        return minEmp

    def getNumEmp(self):
        return len(self.__employees)
    
    

def checkWorkForce():
    emp1 = SalariedEmployee("Joe", "Francis", 123456789, None, 2500)
    emp2 = SalariedEmployee("Samamtha", "Hughes", 444555666, emp1, 1400)
    emp3 = HourlyEmployee("Kim", "Adams", 888999000, emp1, 42, 18.50)
    emp4 = ComissionEmployee("Ryan", "Goodall", 111222333, emp2, 0.10, 9000)

    employees = WorkForce()

    employees.addEmp(emp1)
    employees.addEmp(emp2)
    employees.addEmp(emp3)
    employees.addEmp(emp4)

    print(employees.findMaxEarner())
    print(employees.findMinEarner())

    print(str(employees.getNumEmp()))
    employees.delEmp(emp3)
    print(employees.findMinEarner())
    
    print(str(employees.getNumEmp()))

payrollTester()




































        
    
