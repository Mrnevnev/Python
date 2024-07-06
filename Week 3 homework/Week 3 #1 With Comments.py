# Create empty lists for employees and salaries
employees = []
salaries = []

# Initialize control variables
menuNumber = 0
cont = "yes"

def menu():
    """
    Displays the main menu and performs actions based on the user's choice.
    """
    global employees, salaries, cont

    # Show menu and take user's choice
    menuNumber = int(input("Main Menu \n"
                           "Add Employee - 1 \n"
                           "Delete Employee - 2 \n"
                           "Show Employees - 3 \n"
                           "Add Employee at index - 4 \n"
                           "Total Salary - 5 \n"
                           "Search for employee - 6 \n"
                           "Sort Salaries - 7 \n"
                           "Quit - 0 \n"
                           "Enter your menu number: "))

    # Perform action based on option chosen
    if menuNumber == 1:
        addEmployee(employees, salaries, cont)
    elif menuNumber == 2:
        deleteEmployee(employees, salaries, cont)
    elif menuNumber == 3:
        showList(employees, salaries)
    elif menuNumber == 4:
        addEmployeeAtIndex(employees, salaries, cont)
    elif menuNumber == 5:
        totalSalary(salaries)
    elif menuNumber == 6:
        searchEmployee(employees)
    elif menuNumber == 7:
        sortSalaries(employees, salaries)
    elif menuNumber == 0:
        print('Quitting program')
        quit()
    else:
        print("Invalid menu number")


def addEmployee(employees, salaries, cont):
    """
    Adds a new employee and their salary to the lists.

    Args:
        employees (list): List of employee names.
        salaries (list): List of employee salaries.
        cont (str): Control variable for continuing or stopping the loop.

    Returns:
        tuple: Updated employees, salaries, and cont.
    """
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
        menu()
    return employees, salaries, cont


def addEmployeeAtIndex(employees, salaries, cont):
    """
    Adds a new employee and their salary at a specified index in the lists.

    Args:
        employees (list): List of employee names.
        salaries (list): List of employee salaries.
        cont (str): Control variable for continuing or stopping the loop.

    Returns:
        tuple: Updated employees, salaries, and cont.
    """
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
        menu()

    return employees, salaries, cont


def deleteEmployee(employees, salaries, cont):
    """
    Deletes an employee and their salary from the lists.

    Args:
        employees (list): List of employee names.
        salaries (list): List of employee salaries.
        cont (str): Control variable for continuing or stopping the loop.

    Returns:
        tuple: Updated employees, salaries, and cont.
    """
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
        menu()
    return employees, salaries, cont


def getSalary():
    """
    Prompts the user to enter a valid salary and returns it.

    Returns:
        float: The entered salary.
    """
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


def printList(employees, salaries):
    """
    Prints the list of employees and their salaries.

    Args:
        employees (list): List of employee names.
        salaries (list): List of employee salaries.
    """
    print("List of employees")
    for i in range(len(employees)):
        print(f'{i}. Employee: {employees[i]}, Salary: ${salaries[i]}')

def showList(employees, salaries):
    """
    Prints the list of employees and their salaries.

    Args:
        employees (list): List of employee names.
        salaries (list): List of employee salaries.
    """
    print("List of employees")
    for i in range(len(employees)):
        print(f'{i}. Employee: {employees[i]}, Salary: ${salaries[i]}')
    menu()

def searchEmployee(employees):
    """
    Searches for an employee by name and prints their details if found.

    Args:
        employees (list): List of employee names.
    """
    employeeName = input("Please enter the name of the employee to search: ")
    if employeeName in employees:
        index = employees.index(employeeName)
        salary = salaries[index]
        print(f"{employeeName} is in the list of employees.")
        print(f"At Index: {index}")
        print(f"With a salary of: {salary}")
    else:
        print(f"{employeeName} is not in the list of employees.")
    menu()


def totalSalary(salaries):
    """
    Calculates and prints the total salary of all employees.

    Args:
        salaries (list): List of employee salaries.
    """
    totalSalary = 0
    for i in range(len(salaries)):
        totalSalary += salaries[i]
    print(f'Total Salary: {totalSalary}')
    menu()

def sortSalaries(employees, salaries):
    """
    Sorts the salaries and corresponding employee names using selection sort in descending order.

    Args:
        employees (list): List of employee names.
        salaries (list): List of employee salaries.
    """
    for i in range(len(salaries)):
        max_index = i
        for j in range(i + 1, len(salaries)):
            if salaries[j] > salaries[max_index]:  # Change comparison to '>' for descending order
                max_index = j
        # Swap salaries
        temp_salary = salaries[i]
        salaries[i] = salaries[max_index]
        salaries[max_index] = temp_salary
        # Swap employees to match sorted salaries
        temp_employee = employees[i]
        employees[i] = employees[max_index]
        employees[max_index] = temp_employee
    print("Salaries sorted successfully in descending order.")
    printList(employees, salaries)
    menu()


# Display the menu to start the program
if __name__ == "__main__":
    menu()