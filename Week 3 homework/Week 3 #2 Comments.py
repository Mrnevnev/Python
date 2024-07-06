def mainMenu():
    """Main menu for managing student scores."""
    while True:
        # Display the main menu and prompt user for an option
        try:
            menuNumber = int(input("Main Menu \n"
                                   "Add Student - 1 \n"
                                   "Find Lowest Score - 2 \n"
                                   "Find Highest Score - 3 \n"
                                   "Quit - 0 \n"
                                   "Enter your menu number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if menuNumber == 1:
            # Call the main function to add students
            main()
        elif menuNumber == 2:
            # Find the lowest score for a specific student
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
            # Find the highest score for a specific student
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
            # Quit the program
            print('Quitting program')
            break
        else:
            # Handle invalid menu options
            print("Invalid menu number. Try again.")

def ValidateUserInput(score):
    """
    Validates that the score is between 0 and 100 inclusive.

    Parameters:
    score (int): The score to validate.

    Returns:
    bool: True if the score is valid, False otherwise.
    """
    return 0 <= score <= 100

def getStudentInfo():
    """
    Prompts user for student name and 5 exam scores, validates, and returns them.

    Returns:
    list: A list containing the student's name followed by their scores.
    """
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
    """
    Finds and returns the lowest score from the list.

    Parameters:
    scores (list): A list of scores.

    Returns:
    int: The lowest score.
    """
    lowest = scores[0]
    for score in scores:
        if score < lowest:
            lowest = score
    return lowest

def findHighest(scores):
    """
    Finds and returns the highest score from the list.

    Parameters:
    scores (list): A list of scores.

    Returns:
    int: The highest score.
    """
    highest = scores[0]
    for score in scores:
        if score > highest:
            highest = score
    return highest

def calcScore(scores):
    """
    Calculates the average score after dropping the highest and lowest scores.

    Parameters:
    scores (list): A list of scores.

    Returns:
    float: The average score of the remaining scores.
    """
    lowest = findLowest(scores)
    highest = findHighest(scores)

    # Remove one instance of the lowest and highest score from the list
    scores.remove(lowest)
    scores.remove(highest)

    # Calculate the average of the remaining scores
    average = sum(scores) / len(scores)
    return average

def printStudentInfo(students):
    """
    Prints the student information in a formatted table.

    Parameters:
    students (list): A list of student information.
    """
    print(f"{'Student Name':<16} {'Ex1':<4} {'Ex2':<4} {'Ex3':<4} {'Ex4':<4} {'Ex5':<4}")
    print("-" * 42)
    for student in students:
        name = student[0]
        scores = student[1:]
        scores_str = " ".join(f"{score:<4}" for score in scores)
        print(f"{name:<16} {scores_str}")
    print("-" * 42)

def main():
    """
    Main function to run the program.
    Collects information for multiple students and prints the collected information.
    """
    global students
    students = []

    while True:
        # Get information for a new student
        student_info = getStudentInfo()
        students.append(student_info)

        # Ask if the user wants to add another student
        more_students = input("Do you want to enter another student? (yes/no): ").strip().lower()
        if more_students != 'yes':
            break

    # Print the information for all students
    printStudentInfo(students)

# Run the program
if __name__ == "__main__":
    mainMenu()