#importing random
import random
#Giving information to the usuer about the scores and the shape
print("1. Rock \n2. Paper \n3. Sissor")
A = 'Rock'
B = 'Paper'
C = 'Sissor'
Lose = 'X'
Draw = 'Y'
Win = 'Z'
print("The scores are as the following:\nRock = 1\nPaper = 2\nSissor = 3\nWin = 6\nDraw = 3\n lose = X\nLose = Y\nWin = Z ")


#Letting the computer choose a word ranging from A-B


#Defining a function
def read_input(input_file):
    result = []
    with open(input_file, "r") as f:  # Use input_file instead of "input_1_cap1.txt"
        for line in f:  # Iterate over each line
            x, y = line.strip().split()  # Split line into x and y
            result.append((x, y)) 
    return result  # Return result after the loop

def calculate_score(result):
    total_score = 0
    for x, y in result:
        x_score = {'A': 1, 'B': 2, 'C': 3, 'D': 4}[x]
        y_score = {'X': 0, 'Y': 3, 'Z': 6}[y]
        total_score += x_score + y_score
    return total_score  # Return total_score instead of result

input_file =  'input_1_cap1.txt'
result = read_input(input_file)
if result:
    total_score = calculate_score(result)
    print("The total score is:", total_score) 