#menu with a list of things to do
#add employee to list with salary DONE
#show list of employees
#insert new employee at certain index
#delete employee at certain index
#search for employee in list
#find total salary of employees in list
#quit if sentinal value is true DONE



employees = []
salaries = []
menuNumber = 1
cont = "yes"

def menu(menuNumber):

    menuNumber = int(input("Main Menu \n"
                           "Add Employee - 1 \n"
                           "Enter your menu number "))


    while True:
        if menuNumber == 1:
            addEmployee(employees, salaries, cont)
        else:
            print("invalid menu number")

        menuNumber = int(input("Main Menu \n"
                               "Add Employee - 1 \n"
                               "Enter your menu number "))



#Adds employee to the list and takes the salary function adds it next to the employee
def addEmployee(employees, salaries, cont=None):
    while cont == "yes":

        newEmployees = input("Please enter employee name: ")
        newSalaries = getSalary()

        if newEmployees and newSalaries is not None:
            employees = employees =+ [newEmployees]
            salaries = salaries =+ [newSalaries]
            printList(employees, salaries)

        cont = input("Do you want to add another employee? (yes/no): ")

    return employees, salaries, cont

#ask the user to enter the salary of the employee
def getSalary():
    while True:
        try:
            newSalaries = float(input("Please enter salary: "))
            if newSalaries < 0:
                print("No Negative Numbers")
                continue
            return newSalaries
        except ValueError:
            # Handle invalid input for minutes used
            print("Invalid input")
            continue


#Print the list of employees and salaries.
def printList(employees, salaries):
    for i in range(len(employees)):
        print(f'{i + 1}. Employee: {employees[i]}, Salary: {salaries[i]}')

menu(menuNumber)

employees, salaries, cont = addEmployee(employees, salaries, cont)

addEmployee(employees, salaries, cont)

printList(employees, salaries)
