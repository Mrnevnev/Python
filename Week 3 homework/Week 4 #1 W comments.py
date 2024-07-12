"""
Nevill Adeyeye
7/08/2024
Week 4 Assignment 1
"""
def main():
    """
    Main function to start the program. Asks if the patient was an in-patient or out-patient 
    and calls the appropriate function to calculate charges. 
    Continues to ask for new patients until the user decides to quit.
    """
    while True:
        # Get the patient's name
        patientName = input("Enter patient name: ")
        
        # Get the type of patient (in-patient or out-patient) and validate the input
        patientType = input(f"Was {patientName} an in-patient or out-patient? (Enter 'in' or 'out') ").lower()

        if patientType == 'in':
            # Process charges for in-patient
            inPatientCharges(patientName)
        elif patientType == 'out':
            # Process charges for out-patient
            outPatientCharges(patientName)
        else:
            # Invalid input handling
            print("Invalid input. Must be 'in' or 'out'.")
            continue
        
        # Ask if the user wants to charge another patient
        another_patient = input("Charge another patient? (Enter 'yes' to continue or 'no' to quit): ").lower()
        if another_patient != 'yes':
            # Exit the loop if the user doesn't want to continue
            print("Exiting the program.")
            break


def inPatientCharges(patientName):
    """
    Function for computing inpatient charges.
    
    Args:
        patientName (str): The name of the patient.
    
    This function prompts the user for the number of days spent in the hospital, 
    the daily rate, service charges, and medication costs. It then calculates the 
    total charges using the calculateInPatientCharges function and displays the result.
    """
    print(f"{patientName} was an in-patient")

    # Get and validate input for number of days spent in the hospital
    days = validateInput("How many days was the in-patient visit? ")
    
    # Get and validate input for the daily rate
    rate = validateInput(f"Please enter {patientName}'s daily in-patient rate: ")
    
    # Get and validate input for service charges
    serviceRates = validateInput(f"Please enter {patientName}'s service charges: ")
    
    # Get and validate input for medication costs
    medicationCost = validateInput(f"Please enter {patientName}'s medication cost: ")

    # Calculate total charges
    totalCost = calculateInPatientCharges(days, rate, serviceRates, medicationCost)

    # Display the total cost
    print(f"The total cost for {patientName}'s stay is: ${totalCost:.2f}")


def outPatientCharges(patientName):
    """
    Function for computing outpatient charges.
    
    Args:
        patientName (str): The name of the patient.
    
    This function prompts the user for service charges and medication costs. 
    It then calculates the total charges using the calculateOutPatientCharges function 
    and displays the result.
    """
    print(f"{patientName} was an out-patient")

    # Get and validate input for service charges
    serviceRates = validateInput(f"Please enter {patientName}'s service charges: ")
    
    # Get and validate input for medication costs
    medicationCost = validateInput(f"Please enter {patientName}'s medication cost: ")

    # Calculate total charges
    totalCost = calculateOutPatientCharges(serviceRates, medicationCost)

    # Display the total cost
    print(f"The total cost for {patientName}'s visit is: ${totalCost:.2f}")


def validateInput(prompt):
    """
    Function to validate the user input. Ensures the input is a non-negative number.
    
    Args:
        prompt (str): The prompt to display to the user.
    
    Returns:
        float: The validated input value.
    
    This function continually prompts the user until a valid non-negative number is entered.
    """
    while True:
        try:
            # Try to convert input to a float
            value = float(input(prompt))
            
            # Check if the input value is non-negative
            if value < 0:
                print("Invalid input. Value cannot be negative.")
                continue
            return value
        except ValueError:
            # Handle invalid number input
            print("Invalid input. Please enter a valid number.")


def calculateInPatientCharges(days, daily_rate, service_charges, medication_charges):
    """
    Function to calculate inpatient charges.
    
    Args:
        days (float): Number of days the patient stayed.
        daily_rate (float): Daily rate for the stay.
        service_charges (float): Service charges for the patient.
        medication_charges (float): Charges for any medications.
    
    Returns:
        float: The total inpatient charges.
    
    This function calculates the total cost for in-patient by summing 
    the product of days and daily rate with the service charges and medication charges.
    """
    total_charges = (days * daily_rate) + service_charges + medication_charges
    return total_charges


def calculateOutPatientCharges(service_charges, medication_charges):
    """
    Function to calculate outpatient charges.
    
    Args:
        service_charges (float): Service charges for the patient.
        medication_charges (float): Charges for any medications.
    
    Returns:
        float: The total outpatient charges.
    
    This function calculates the total cost for out-patient by summing 
    the service charges and medication charges.
    """
    total_charges = service_charges + medication_charges
    return total_charges


# Run the main function if this script is run directly
if __name__ == "__main__":
    main()