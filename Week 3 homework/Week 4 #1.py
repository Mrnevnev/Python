def main ():
    while True:
            patientName = input("Enter patient name: ")
            patientType = input(f"Was {patientName} an in-patient or out-patient? (Enter 'in' or 'out') ").lower()
            if patientType == 'in':
                inPatientCharges(patientName)
            elif patientType == 'out':
                outPatientCharges(patientName)
            else:
                print("Invalid input. Must be in or out.")
                continue
def inPatientCharges(patientName):
    print(f"{patientName} was an in-patient")
    days = validateInput("How many days was the in-patient visit? ")
    rate = validateInput(f"Please enter {patientName}'s daily in-patient rate: ")
    serviceRates = validateInput(f"Please enter {patientName}'s service rates: ")
    medicationCost = validateInput(f"Please enter {patientName}'s medication cost: ")
    totalCost = calculateInPatientCharges(days, rate, serviceRates, medicationCost)
    print(f"The total cost for {patientName}'s stay is: ${totalCost:.2f}")
    chargePatient()
def outPatientCharges(patientName):
    print(f"{patientName} was an out-patient")
    serviceRates = validateInput(f"Please enter {patientName}'s service rates: ")
    medicationCost = validateInput(f"Please enter {patientName}'s medication cost: ")
    totalCost = calculateOutPatientCharges(serviceRates, medicationCost)
    print(f"The total cost for {patientName}'s visit is: ${totalCost:.2f}")
    chargePatient()
def validateInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Invalid input. Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def calculateInPatientCharges(days, daily_rate, service_charges, medication_charges):
    total_charges = (days * daily_rate) + service_charges + medication_charges
    return total_charges
def calculateOutPatientCharges(service_charges, medication_charges):
    total_charges = service_charges + medication_charges
    return total_charges
def chargePatient():
    start = input("Charge another patient? (Enter 'yes' to continue  or 'no'): ").lower()
    if start == 'yes':
        main()
    else:
        quit()
# Run the program
if __name__ == "__main__":
    main()
