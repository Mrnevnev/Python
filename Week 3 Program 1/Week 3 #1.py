#menu with a list of things to do
#add employee to list with salary DONE
#show list of employees
#insert new employee at certain index
#delete employee at certain index Done
#search for employee in list
#find total salary of employees in list
#quit if sentinal value is true DONE

employees = []
salaries = []
menuNumber = 1
cont = "yes"

def menu(menuNumber):
    global cont
    menuNumber = int(input("Main Menu \n"
                           "Add Employee - 1 \n"
                           "Delete Employee - 2 \n"
                           "Show Employees - 3 \n"
                           "Quit - 0 \n"
                           "Enter your menu number "))
    if cont == "no":
        menu(menuNumber)
    elif menuNumber == 1:
        addEmployee(employees, salaries, cont)
    elif menuNumber == 2:
        deleteEmployee(employees, salaries, cont)
    elif menuNumber == 3:
        showEmployees(employees, salaries, cont)



    else:
        print("invalid menu number")

    menuNumber = int(input("Main Menu \n"
                           "Add Employee - 1 \n"
                           "Delete Employee - 2 \n"
                           "Show Employees - 3 \n"
                           "Quit - 0 \n"
                           "Enter your menu number "))



#Adds employee to the list and takes the salary function adds it next to the employee
def addEmployee(employees, salaries, cont):


    while cont == "yes":
        printList(employees, salaries)
        newEmployees = input("Please enter employee name: ")
        newSalaries = getSalary()

        if newEmployees and newSalaries is not None:
            employees += [newEmployees]
            salaries += [newSalaries]
            printList(employees, salaries)

        cont = input("Do you want to add another employee? (yes/no): ")


    if cont == "no":
        menu(menuNumber)


    return employees, salaries, cont

#delete employee at certain index without using pop()
def deleteEmployee(employees, salaries, cont):

    while cont == "yes":
        printList(employees, salaries)
        employeeToDelete = int(input("Please enter employee to delete: "))

        # Check if input is a valid index within the list range
        if 0 <= employeeToDelete < len(employees):
            # Remove the employee and his corresponding salary
            employees = employees[:employeeToDelete] =+ employees[employeeToDelete + 1:]
            salaries = salaries[:employeeToDelete] =+ salaries[employeeToDelete + 1:]
            printList(employees, salaries)
            cont = input("Do you want to add another employee? (yes/no): ")
        else:
            print("Invalid input. No such employee index.")

    if cont == "no":
        menu(menuNumber)
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
    return salaries

#show list of employees
def showEmployees(employees, salaries, cont):
    printList(employees, salaries)
    menu(menuNumber)

#Print the list of employees and salaries.
def printList(employees, salarries):
    print("List of employees")
    for i in range(len(employees)):

        print(f'{i}. Employee: {employees[i]}, Salary: {salaries[i]}')

menu(menuNumber)

employees, salaries, cont = addEmployee(employees, salaries, cont)

addEmployee(employees, salaries, cont)

deleteEmployee(employees, salaries, cont)

printList(employees, salaries)






