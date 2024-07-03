#Nevill Adeyeye Week 2 Homework 2

# Prompt the user to input their name and store it in the variable 'name'
name = input("What is your name? ")

# Prompt the user to input three scores, convert them to float, and store them in the variables 'score1', 'score2', and 'score3'
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))

# Calculate the average of the three scores and round it to the nearest integer
averageScore = round((score1 + score2 + score3) / 3)

# Initialize the variable 'letterScore' with a default value of "A"
letterScore = "A"

# Determine the letter grade based on the average score using a series of conditional statements
if averageScore >= 98:
    # If the average score is 98 or higher, assign "A+" to the variable 'letter'
    letter = "A+"
elif averageScore >= 95:
    # If the average score is between 95 and 97, assign "A" to the variable 'letter'
    letter = "A"
elif averageScore >= 91:
    # If the average score is between 91 and 94, assign "A-" to the variable 'letter'
    letter = "A-"
elif averageScore >= 88:
    # If the average score is between 88 and 90, assign "B+" to the variable 'letter'
    letter = "B+"
elif averageScore >= 84:
    # If the average score is between 84 and 87, assign "B" to the variable 'letter'
    letter = "B"
elif averageScore >= 80:
    # If the average score is between 80 and 83, assign "B-" to the variable 'letter'
    letter = "B-"
elif averageScore >= 75:
    # If the average score is between 75 and 79, assign "C+" to the variable 'letter'
    letter = "C+"
elif averageScore >= 70:
    # If the average score is between 70 and 74, assign "C" to the variable 'letter'
    letter = "C"
elif averageScore < 70 and averageScore > 60:
    # If the average score is between 61 and 69, assign "D" to the variable 'letter'
    letter = "D"
elif averageScore <= 60:
    # If the average score is 60 or below, assign "NC" to the variable 'letter'
    letter = "NC"

# Assign the determined letter grade to the variable 'letterScore'
letterScore = letter

# Print the user's name, average score, and letter grade
print(f"Name: {name}")
print(f"Average Score: {averageScore}")
print(f"Letter Score: {letterScore}")