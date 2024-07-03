# Nevill Adeyeye Week 2 Program 3
name = ""  # Holds the user's name
serviceType = ""  # Holds the type of service chosen by the user
accountNumber = ""  # Holds the user's account number
nightMin = 0  # Holds the number of night minutes used for Premium Service
dayMin = 0  # Holds the number of day minutes used for Premium Service
minUsed = 0  # Holds the total minutes used
regularService = 10  # Fixed cost for Regular Service
premiumService = 25  # Fixed cost for Premium Service
bill = 0  # Holds the total bill amount
cont = "yes"  # Control variable to continue or stop the loop

# Loop to repeatedly ask for user input and calculate the bill until the user decides to stop
while cont == "yes":
    # Prompt user to enter their name
    name = input("Enter your name: ")

    # Prompt user to select a service type (Regular or Premium)
    serviceType = input(
        f"Hi {name}. Please pick a Service Type (R for Regular Service or P for Premium Service):  ").lower().strip()

    # Check if the user selected Regular Service
    if serviceType == "r":
        try:
            # Prompt user to enter their account number
            accountNumber = input("Enter your account number: ")
            # Prompt user to enter the number of minutes used
            minUsed = int(input("Enter your min used: "))
            # Check for negative input
            if minUsed < 0:
                print("No Negative Numbers")
                continue
            # Set service type to Regular Service
            serviceType = "Regular Service"
            # Calculate the bill based on minutes used
            if minUsed > 50:
                bill = regularService + ((minUsed - 50) * .20)  # Additional charges for minutes over 50
            else:
                bill = regularService  # Base charge for Regular Service
        except ValueError:
            # Handle invalid input for minutes used
            print("Invalid input")
            continue

    # Check if the user selected Premium Service
    elif serviceType == "p":
        try:
            # Prompt user to enter the number of night and day minutes used
            nightMin = int(input("Enter your night min: "))
            dayMin = int(input("Enter your day min: "))
            # Check for negative input
            if nightMin < 0 or dayMin < 0:
                print("No Negative Numbers")
                continue

            # Set service type to Premium Service
            serviceType = "Premium Service"
            # Calculate total minutes used
            minUsed = nightMin + dayMin

            # Calculate additional charges for night minutes over 100
            if nightMin > 100:
                bill += (nightMin - 100) * .05
            # Calculate additional charges for day minutes over 75
            if dayMin > 75:
                bill += (dayMin - 75) * .10

            # Add base charge for Premium Service
            bill += premiumService
        except ValueError:
            # Handle invalid input for night and day minutes
            print("Invalid input")
            continue
    else:
        # Handle invalid input for service type
        print("Invalid Input")
        continue
    finalBill = float(round(bill, 2))

    # Display the billing information to the user
    print(f"Name: {name}")
    print(f"Service Type: {serviceType}")
    print(f"Account Number: {accountNumber}")
    print(f"Minutes Used this month: {minUsed}")
    print(f"Bill for this month: {finalBill}")

    # Prompt user to decide if they want to continue or stop
    cont = input("Type YES to continue or Press Enter to stop: ").lower().strip()