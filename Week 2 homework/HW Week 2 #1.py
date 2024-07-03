# Nevill Adeyeye Week 2 Homework 1

# Prompt user to enter the number of employees
numofemployees = input("Number of employees? ")

# Convert the number of employees from string to integer
intnumemployees = int(numofemployees)

# Iterate through the number of employees to gather details and calculate taxes
for i in range(intnumemployees):
    # Prompt user to enter their name
    name = input("What is your name? ")

    # Prompt user to enter their salary and convert it to an integer
    salary = int(input("How much is your salary? "))

    # Initialize federal tax variable
    fedTax = 0

    # Define the federal tax limit
    fedLimit = 100000

    # Calculate federal tax based on the salary
    if salary > fedLimit:
        # If salary is greater than the federal limit, apply 20% federal tax
        fedTax = salary * .20
    else:
        # If salary is less than or equal to the federal limit, apply 15% federal tax
        fedTax = salary * .15

    # Prompt user to enter the state they worked in and convert it to lowercase
    stateOfWork = input("What state did you work in? ").strip().lower()

    # Calculate state tax based on the state of work
    if stateOfWork == "ca" or stateOfWork == "nv" or stateOfWork == "az" or stateOfWork == "tz":
        # If state is CA, NV, AZ, or TZ, apply 10% state tax
        stateTax = salary * .10
    else:
        # For all other states, apply 12% state tax
        stateTax = salary * .12

    # Calculate the total taxes paid by summing federal and state taxes
    taxesPaided = (float(round(fedTax, 2)) + float(round(stateTax, 2)))

    # Calculate the gross salary after deducting taxes
    gross = float(round(salary, 2)) - float(round(taxesPaided, 2))

    # Print the employee's name
    print(f"Name: {name}")

    # Print the total taxes paid
    print(f"Taxes Paid:{taxesPaided}")

    # Print the gross salary
    print(f"Gross Salary: {gross}")

    # Print the state of work in uppercase
    print(f"State of Work: {stateOfWork.upper()}")