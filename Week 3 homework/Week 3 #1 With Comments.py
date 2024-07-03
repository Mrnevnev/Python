# Create empty lists for employees and salaries
employees = []
salaries = []

# Initialize control variables
menuNumber = 0
cont = "yes"


def menu(menuNumber):
    # Define global variables
    global employees, salaries, cont

    # Show menu and take user's choice
    menuNumber = int(input("Main Menu \n"
                           "Add Employee - 1 \n"
                           "Delete Employee - 2 \n"
                           "Show Employees - 3 \n"
                           "Add Employee at index - 4 \n"
                           "Total Salary - 5 \n"
                           "Search for employee - 6 \n"
                           "Quit - 0 \n"
                           "Enter your menu number "))

    # Perform action based on option chosen
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
        print('Quitting program')
        quit()
    else:
        print("Invalid menu number")


# Function that adds an employee to the list, and their respective salary
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


# Function that adds an employee at a specified index
def addEmployeeAtIndex(employees, salaries, cont):
    while cont == "yes":
        printList(employees, salaries)
        newEmployee = input("Please enter employee name: ")
        newSalary = getSalary()

        if newEmployee and newSalary is not None:
            index = int(input("Please enter the index at which you want to add the employee: "))

            employees[:] = employees[:index] + [newEmployee] + employees[index:]
            salaries[:] = salaries[:index] + [newSalary] + salaries[index:]

            printList(employees, salaries)

        cont = input("Do you want to add another employee? (yes/no): ")

    if cont == "no":
        menu(menuNumber)

    return employees, salaries, cont


# Function that deletes an employee
def deleteEmployee(employees, salaries, cont):
    while cont == "yes":
        printList(employees, salaries)
        employeeToDelete = int(input("Please enter employee to delete: "))

        if 0 <= employeeToDelete < len(employees):
            employees[:] = employees[:employeeToDelete] + employees[employeeToDelete + 1:]
            salaries[:] = salaries[:employeeToDelete] + salaries[employeeToDelete + 1:]
            printList(employees, salaries)
            cont = input("Do you want to delete another employee? (yes/no): ")
        else:
            print("Invalid input. No such employee index.")

    if cont == "no":
        menu(menuNumber)
    return employees, salaries, cont


# Function to get the salary of the employee
def getSalary():
    while True:
        try:
            newSalaries = float(input("Please enter salary: "))
            if newSalaries < 0:
                print("No Negative Numbers")
                continue
            return newSalaries
        except ValueError:
            print("Invalid input")
            continue
    return salaries


# Function to print list of employees and their salaries
def printList(employees, salaries):
    print("List of employees")
    for i in range(len(employees)):
        print(f'{i}. Employee: {employees[i]}, Salary: {salaries[i]}')


# Function to search for an employee
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


# Function to calculate total salary of employees
def totalSalary(salaries):
    totalSalary = 0
    for i in range(len(salaries)):
        totalSalary += salaries[i]
    print(f'Total Salary: {totalSalary}')


# Display the menu to start the program
menu(menuNumber)
