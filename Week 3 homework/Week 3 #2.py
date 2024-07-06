#Make a two;dimensional matrix to take in a name and 5 test scores
#Create a function that validates if the users input is correct.
#Create a function that returns the lowest score in the group
#Create a function that returns the highest score in the group
#Create a function that calculates the total score of a student

#Make a two;dimensional matrix to take in a name and 5 test scores
studentInfo = []
studentsInClss = []
scores = []
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
        addStudentInfo(studentInfo, studentsInClss, scores, cont)
    elif menuNumber == 0:
        print('Quitting program')
        quit()
    else:
        print("Invalid menu number")

#Create a function that validates if the users input is correct.
def addStudentInfo(studentInfo, studentsInClss, scores, cont):
    i = 0
    while cont == "yes":
        printList(studentInfo, studentsInClss, scores)
        numOfStudents = int(input("Please enter how many students: "))
        for i in range(numOfStudents):
            newStudent = input("Please enter students name: ")
            for j in range(5):
                newScores = getScores(numOfStudents)
            if newStudent is not None:

                studentInfo = newStudent

                printList(studentInfo, studentsInClss, scores)
        cont = input("Do you want to add another employee? (yes/no): ")
    if cont == "no":
        menu(menuNumber)
    return studentInfo, studentsInClss, scores

def getScores(numOfStudents):
    i = 1
    while True:
        try:
            scores = int(input(f"Please enter students score #{i}: "))
            if scores < 0:
                print("No Negative Numbers")
                continue
            else:
                scores += scores
                i = i + 1
            return scores
        except ValueError:
            print("Invalid input")
            continue
    return

def printList(studentInfo, studentsInClss, scores):
    print("List of employees")
    print("Name" "Scores")
    print(f'Students: {studentInfo} Scores: {scores}')

# Run the program
if __name__ == "__main__":
    menu()