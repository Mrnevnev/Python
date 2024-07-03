GrossWage = 0
LastName = input('Enter Last Name') # Takes in the users last name.
print("Last name is: ", LastName) #Echos users last name.
FirstName = input('Enter First Name') # Takes in users first name.
print("First name is: ", FirstName) # Echos users first name.
HoursWorked = float(input('Enter Number of Hours Worked')) # Takes in number of hours worked. Converted to a float.
print("Your Hours Worked: ", HoursWorked) # Echos users hours worked.
HourlyWage = int(input('Enter you Hourly Wage')) # Takes in hourly wage. Converted to a int.
print("Your Hours Worked: ", HourlyWage) # Echos users hourly wage.
GrossWage = HoursWorked * HourlyWage # calculates the gross wage for the user.

print ("Hello", FirstName, LastName,". " "Your Gross Wage is: ", GrossWage)