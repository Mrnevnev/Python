"""
Nevill Adeyeye
7/08/2024
"""


def main():
    """
    Main function to get scores from five judges, calculate final score,
    and print final score.
    """
    scores = []
    for i in range(5):
        score = getJudgeScore()  # Get score from a judge
        scores.append(score)  # Append the score to the list of scores
    # Calculate final score by dropping the highest and lowest score, and averaging the rest
    finalScore = calcScore(scores[0], scores[1], scores[2], scores[3], scores[4])
    # Print final score
    print(f"Final score is:, {finalScore:.2f}")


def getJudgeScore():
    """
    Prompts user for judge's score, ensuring it is between 0 and 10.

    Returns:
        score (float): Judge's score if it is a valid input. Continues to prompt otherwise.
    """
    while True:
        try:
            score = float(input("Enter judge's score (0-10): "))
            if 0 <= score <= 10:
                return score
            else:
                print("Score must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def findLowestScore(score1, score2, score3, score4, score5):
    """
    Finds the lowest score from five given scores.

    Args:
        score1 (float): Judge 1's score.
        score2 (float): Judge 2's score.
        score3 (float): Judge 3's score.
        score4 (float): Judge 4's score.
        score5 (float): Judge 5's score.

    Returns:
        lowest (float): The least score of the five.
    """
    lowest = score1
    if score2 < lowest:
        lowest = score2
    if score3 < lowest:
        lowest = score3
    if score4 < lowest:
        lowest = score4
    if score5 < lowest:
        lowest = score5
    return lowest


def findHighestScore(score1, score2, score3, score4, score5):
    """
    Finds the highest score from five given scores.

    Args:
        score1 (float): Judge 1's score.
        score2 (float): Judge 2's score.
        score3 (float): Judge 3's score.
        score4 (float): Judge 4's score.
        score5 (float): Judge 5's score.

    Returns:
        highest (float): The highest score of the five.
    """
    highest = score1
    if score2 > highest:
        highest = score2
    if score3 > highest:
        highest = score3
    if score4 > highest:
        highest = score4
    if score5 > highest:
        highest = score5
    return highest


def calcScore(score1, score2, score3, score4, score5):
    """
    Calculates the final score by dropping the highest and lowest score and averaging the rest.

    Args:
        score1 (float): Judge 1's score.
        score2 (float): Judge 2's score.
        score3 (float): Judge 3's score.
        score4 (float): Judge 4's score.
        score5 (float): Judge 5's score.

    Returns:
        averageScore (float): The average of the middle three scores.
    """
    lowestScore = findLowestScore(score1, score2, score3, score4, score5)
    highestScore = findHighestScore(score1, score2, score3, score4, score5)

    total = score1 + score2 + score3 + score4 + score5
    adjustedTotal = total - lowestScore - highestScore
    averageScore = adjustedTotal / 3

    return averageScore


if __name__ == "__main__":
    main()
