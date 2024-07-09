"""
 Mhave the user re-enter the input if it is invalid.
"""


def main ():
    while True:
            patientName = input("Enter patient name: ")
            paitentType = input(f"Was {patientName} an in-patient or out-patient? (Enter 'in' or 'out') ").lower()
            if paitentType == 'in':
                inPatientCharges(patientName)
            elif paitentType == 'out':
                outPatientCharges(patientName)
            else:
                print("Invalid input. Must be in or out.")
                continue

def inPatientCharges(patientName):
    print(f"{patientName} was an in-patient")
    days = validateInput(input("How many days was the in-patient visit? "))
    rate = validateInput(input(f"Please enter {patientName}'s daily in-patient rate: "))
    serviceRates = validateInput(input(f"Please enter {patientName}'s service rates: "))
    medicationCost = validateInput(input(f"Please enter {patientName}'s medication cost: "))
    totalCost = calculateInPatientCharges(days, rate, serviceRates, medicationCost)
    print(f"The total cost for {patientName}'s stay is: ${totalCost:.2f}")
    chargePatient()
def outPatientCharges(patientName):
    print(f"{patientName} was an out-patient")
    serviceRates = validateInput(input(f"Please enter {patientName}'s service rates: "))
    medicationCost = validateInput(input(f"Please enter {patientName}'s medication cost: "))
    totalCost = calculateOutPatientCharges(serviceRates, medicationCost)
    print(f"The total cost for {patientName}'s stay is: ${totalCost:.2f}")
    chargePatient()
def validateInput(input_str):
    # Check if string can be converted to a float
    try:
        val = float(input_str)
    except ValueError:
        print(f"Invalid input. Please enter a number.")
        return None
    return val

def calculateInPatientCharges(days, daily_rate, service_charges, medication_charges):
    total_charges = (days * daily_rate) + service_charges + medication_charges
    return total_charges
def calculateOutPatientCharges(service_charges, medication_charges):
    total_charges = service_charges + medication_charges
    return total_charges
def chargePatient():
    start = input("Charge patient? (Enter 'yes' or 'no'): ").lower()
    if start == 'yes':
        main()
    else:
        quit()
# Run the program
if __name__ == "__main__":
    chargePatient()