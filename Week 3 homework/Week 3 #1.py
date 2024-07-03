#menu with a list of things to do. Done
#add employee to list with salary DONE
#show list of employees Done
#insert new employee at certain index Done
#delete employee at certain index Done
#search for employee in list Done
#find total salary of employees in list Done
#quit if sentinel value is true DONE

employees = []
salaries = []
menuNumber = 0
cont = "yes"


def menu(menuNumber):
    global employees, salaries, cont
    menuNumber = int(input("Main Menu \n"
                           "Add Employee - 1 \n"
                           "Delete Employee - 2 \n"
                           "Show Employees - 3 \n"
                           "Add Employee at index - 4 \n"
                           "Total Salary - 5 \n"
                           "Search for employee - 6 \n"
                           "Quit - 0 \n"
                           "Enter your menu number "))
    if menuNumber == 1:
        addEmployee(employees, salaries, cont)
    elif menuNumber == 2:
        deleteEmployee(employees, salaries, cont)
    elif menuNumber == 3:
        printList(employees, salaries)
    elif menuNumber == 4:
        addEmployeeAtIndex(employees, salaries, cont)
    elif menuNumber == 5:
        totalSalary(salaries)
    elif menuNumber == 6:
        searchEmployee(employees)
    elif menuNumber == 0:
        quit()
        print('Quitting program')


    else:
        print("Invalid menu number")

    menuNumber = int(input("Main Menu \n"
                           "Add Employee - 1 \n"
                           "Delete Employee - 2 \n"
                           "Show Employees - 3 \n"
                           "Add Employee at index - 4 \n"
                           "Total Salary - 5 \n"
                           "Search for employee - 6 \n"
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

#insert new employee at certain index
def addEmployeeAtIndex(employees, salaries, cont):
    while cont == "yes":
        printList(employees, salaries)
        newEmployee = input("Please enter employee name: ")
        newSalary = getSalary()

        if newEmployee and newSalary is not None:
            index = int(input("Please enter the index at which you want to add the employee: "))

            # Add the new employee and salary at the specified index using slicing
            employees[:] = employees[:index] + [newEmployee] + employees[index:]
            salaries[:] = salaries[:index] + [newSalary] + salaries[index:]

            printList(employees, salaries)

        cont = input("Do you want to add another employee? (yes/no): ")

    if cont == "no":
        menu(menuNumber)  # Assuming menuNumber is 1 for example

    return employees, salaries, cont

#delete employee at certain index without using pop()
def deleteEmployee(employees, salaries, cont):

    while cont == "yes":
        printList(employees, salaries)
        employeeToDelete = int(input("Please enter employee to delete: "))

        # Check if input is a valid index within the list range
        if 0 <= employeeToDelete < len(employees):
            # Remove the employee and his corresponding salary
            employees[:] = employees[:employeeToDelete] + employees[employeeToDelete + 1:]
            salaries[:] = salaries[:employeeToDelete] + salaries[employeeToDelete + 1:]
            printList(employees, salaries)
            cont = input("Do you want to delete another employee? (yes/no): ")
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

#Print the list of employees and salaries.
def printList(employees, salaries):
    print("List of employees")
    for i in range(len(employees)):
        print(f'{i}. Employee: {employees[i]}, Salary: {salaries[i]}')

def searchEmployee(employees):
    employeeName = input("Please enter the name of the employee to search: ")
    if employeeName in employees:
        index = employees.index(employeeName)
        salary = salaries[index]
        print(f"{employeeName} is in the list of employees.")
        print(f"At Index: {index}")
        print(f"With a salary of: {salary}")
    else:
        print(f"{employeeName} is not in the list of employees.")
    menu(menuNumber)

def totalSalary(salaries):
    total = 0
    totalSalary = 0
    for i in range(len(salaries)):

        totalSalary += salaries[i]


    print(f'Total Salary: {totalSalary}')

menu(menuNumber)
