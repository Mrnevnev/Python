def main():
    scores = []
    for i in range(5):
        score = getJudgeScore()
        scores.append(score)
    finalScore = calcScore(scores[0], scores[1], scores[2], scores[3], scores[4])
    print(f"Final score is:, {finalScore:.2f}")

def getJudgeScore():
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
    lowestScore = findLowestScore(score1, score2, score3, score4, score5)
    highestScore = findHighestScore(score1, score2, score3, score4, score5)

    total = score1 + score2 + score3 + score4 + score5
    adjustedTotal = total - lowestScore - highestScore
    averageScore = adjustedTotal / 3

    return averageScore

if __name__ == "__main__":
    main()