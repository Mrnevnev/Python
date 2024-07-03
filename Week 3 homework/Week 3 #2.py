#Make a two;dimensional matrix to take in a name and 5 test scores
#Create a function that validates if the users input is correct.
#Create a function that returns the lowest score in the group
#Create a function that returns the highest score in the group
#Create a function that calculates the total score of a student

#Make a two;dimensional matrix to take in a name and 5 test scores
studentInfo = ["name", 1, 2, 3, 4, 5]
studentsInClss = [studentInfo]
menuNumber = 0
cont = "yes"
#Menu
def menu(menuNumber):
    # Define global variables
    global studentInfo, studentsInClss, cont

    # Show menu and take user's choice
    menuNumber = int(input("Main Menu \n"
                           "Add Student - 1 \n"
                           "Quit - 0 \n"
                           "Enter your menu number "))

    # Perform action based on option chosen
    if menuNumber == 1:
        addStudentInfo(studentInfo, studentsInClss, cont)
    elif menuNumber == 0:
        print('Quitting program')
        quit()
    else:
        print("Invalid menu number")

#Create a function that validates if the users input is correct.
def addStudentInfo(studentInfo, studentsInClss, cont):
    i = 0
    while cont == "yes":
        printList(studentInfo, studentsInClss)
        newStudent = input("Please enter students name and 5 test scores: ")

        while i != len(studentInfo):
            newStudent = input("Please enter students name and 5 test scores: ")
            if newStudent is not None:
                studentInfo += [newStudent]
                studentsInClss += [studentInfo]
                printList(studentInfo, studentsInClss)
        cont = input("Do you want to add another employee? (yes/no): ")

    if cont == "no":
        menu(menuNumber)
    return studentInfo, studentsInClss

def printList(studentInfo, studentsInClss):
    print("List of employees")
    for i in range(len(studentInfo)):
        print(f'{i}. Students: {studentInfo[i]}')


menu(menuNumber)