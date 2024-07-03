CustDrink1, CustDrink2, CustDrink3 = 0, 0, 0
CustFood1, CustFood2, CustFood3 = 0, 0, 0

#Customer 1 Information
CustName1 = input("Enter Customers Name: ")
CustDrink1 = input("Enter Drink Total: ")
CustFood1 = input("Enter Food Total: ")


#Customer 2 Information
CustName2 = input("Enter Customers Name: ")
CustDrink2 = input("Enter Drink Total: ")
CustFood2 = input("Enter Food Total: ")


#Customer 3 Information
CustName3 = input("Enter Customers Name: ")
CustDrink3 = input("Enter Drink Total: ")
CustFood3 = input("Enter Food Total: ")


# Calculate totals including a 15% tip on food
Cust1Total = float(CustDrink1) + float(CustFood1) + (float(CustFood1) * 0.15)
Cust2Total = float(CustDrink2) + float(CustFood2) + (float(CustFood2) * 0.15)
Cust3Total = float(CustDrink3) + float(CustFood3) + (float(CustFood3) * 0.15)



print(
    CustName1, "Total is: ", Cust1Total, '\n',
    CustName2, "Total is: ", Cust2Total, '\n',
    CustName3, "Total is: ", Cust3Total )