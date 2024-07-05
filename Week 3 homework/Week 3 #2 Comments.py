def mainMenu():
    """Main menu for managing employees and student scores."""
    while True:
        menuNumber = int(input("Main Menu \n"
                               "Add Student - 1 \n"
                               "Find Lowest Score - 2 \n"
                               "Find Highest Score - 3 \n"
                               "Quit - 0 \n"
                               "Enter your menu number: "))
        if menuNumber == 1:
            main()
        elif menuNumber == 2:
            if 'students' in globals() and students:
                student_name = input("Enter the student's name to find the lowest score: ")
                student = next((s for s in students if s[0] == student_name), None)
                if student:
                    lowest_score = findLowest(student[1:])
                    print(f"Lowest score for {student_name} is: {lowest_score}")
                else:
                    print(f"Student {student_name} not found.")
            else:
                print("No students available. Add students first.")
        elif menuNumber == 3:
            if 'students' in globals() and students:
                student_name = input("Enter the student's name to find the highest score: ")
                student = next((s for s in students if s[0] == student_name), None)
                if student:
                    highest_score = findHighest(student[1:])
                    print(f"Highest score for {student_name} is: {highest_score}")
                else:
                    print(f"Student {student_name} not found.")
            else:
                print("No students available. Add students first.")
        elif menuNumber == 0:
            print('Quitting program')
            break
        else:
            print("Invalid menu number. Try again.")

def ValidateUserInput(score):
    """Validates that the score is between 0 and 100 inclusive."""
    return 0 <= score <= 100

def getStudentInfo():
    """Prompts user for student name and 5 exam scores, validates, and returns them."""
    student_info = []
    student_name = input("Enter the student's name: ")
    scores = []

    for i in range(1, 6):
        while True:
            try:
                score = int(input(f"Enter score for exam {i}: "))
                if ValidateUserInput(score):
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    student_info.append(student_name)
    student_info.extend(scores)
    return student_info

def findLowest(scores):
    """Finds and returns the lowest score from the list."""
    lowest = scores[0]
    for score in scores:
        if score < lowest:
            lowest = score
    return lowest

def findHighest(scores):
    """Finds and returns the highest score from the list."""
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest

def calcScore(scores):
    """Calculates the average score after dropping the highest and lowest scores."""
    lowest = findLowest(scores)
    highest = findHighest(scores)

    # Remove one instance of the lowest and highest score from the list
    scores.remove(lowest)
    scores.remove(highest)

    # Calculate the average of the remaining scores
    average = sum(scores) / len(scores)
    return average

def printStudentInfo(students):
    """Prints the student information in a formatted table."""
    print(f"{'Student Name':<16} {'Ex1':<4} {'Ex2':<4} {'Ex3':<4} {'Ex4':<4} {'Ex5':<4}")
    print("-" * 42)
    for student in students:
        name = student[0]
        scores = student[1:]
        scores_str = " ".join(f"{score:<4}" for score in scores)
        print(f"{name:<16} {scores_str}")
    print("-" * 42)

def main():
    """Main function to run the program."""
    global students
    students = []

    while True:
        student_info = getStudentInfo()
        students.append(student_info)

        more_students = input("Do you want to enter another student? (yes/no): ").strip().lower()
        if more_students != 'yes':
            break
    printStudentInfo(students)

# Run the program
if __name__ == "__main__":
    mainMenu()