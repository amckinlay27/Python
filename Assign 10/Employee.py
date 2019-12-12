#Adam McKinlay - c0656685
#Date: 2019-12-04
#Chapter 10: Q7 - Employee

#Employee class
class Employee:

    #Constructs an employee object
    def __init__(self, name, id_num, department, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__department = department
        self.__job_title = job_title

    #Returns the name of the employee
    def getName(self):
        return self.__name

    #Returns the id number of an employee
    def getIdNum(self):
        return self.__id_num

    #Returns employee's department
    def getDept(self):
        return self.__department

    #Returns employee job title
    def getJobTitle(self):
        return self.__job_title

    #Sets employee name
    def setName(self, name):
        self.__name = name

    #Sets employee id number
    def setIdNum(self, id_num):
        self.__id_num = id_num

    #Sets employee's department
    def setDept(self, dept):
        self.__department = dept

    #Sets employee job title
    def setJob(self, job):
        self.__job_title = job

    def __str__(self):
        return "Employee Name: " + self.__name + \
               "\nEmployee ID: " + str(self.__id_num) + \
               "\nDepartment: " + self.__department + \
               "\nRole: " + self.__job_title
