#A for Rock, B for Paper, and C for Scissors
#response: X for Rock, Y for Paper, and Z for Scissors.
#The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
#['A Z', 'A Z', 'C Y']
# part2 X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

# nacteni dat
with open('2input.txt') as file:
    rounds = [i for i in file.read().strip().split("\n")]

'''
score = 0
for a in data:
    for i in a:
        if i == "X":
            score += 1
        elif i == "Y":
            score += 2    
        elif i == "Z":
            score += 3
'''
#part1
outcomes = {                    #vytvoreni slovniku bodu
    "A X":4, "A Y":8, "A Z":3,
    "B X":1, "B Y":5, "B Z":9,
    "C X":7, "C Y":2, "C Z":6
}

points_p1 = 0
for round in rounds:
    points_p1 += outcomes[round]

#part2
outcomes2 = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7
}

points_p2 = 0
for round in rounds:
    points_p2 += outcomes2[round]

print("Answer to part1 is:", points_p1)
print("Answer to part2 is:", points_p2)