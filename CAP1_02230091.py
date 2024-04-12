################################
# Ugyen Namgay Phuntsho
# Electrical Engineering, Year 1
# 02230091
################################
# SOLUTION
# Solution Score:
# 50029
################################


#Defining a function
#Refered to Lotfinejad, M. (2023, March 6). Tutorial: How to easily read files in Python (Text, CSV, JSON). Dataquest.
#https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content

def read_input(input_file):
    result = []
    with open(input_file, "r") as f:  # Using the open and with to read the assigned text.
        for line in f:  # Iterating over each line
            x, y = line.strip().split()  # It helps in spiiting x and y where x is the opponents choice and y is the outcome
            result.append((x, y)) #adding x and y in the list.
    return result  # Return result after the loop

#Refered Python Tutorial. (n.d.). 
#https://www.w3schools.com/python/
def calculate_score(result):#defining calculate_score() and setting result as the parameter
    total_score = 0 #initial score point
    for x, y in result: #iteration 
        x_score = {'A': 1, 'B': 2, 'C': 3, 'D': 4}[x] #settings value for each key to operate the sum later which is for opponents choice
        y_score = {'X': 0, 'Y': 3, 'Z': 6}[y] #Giving values for the keys for outcome
        total_score += x_score + y_score #suming the outcomes and opponents choice 
    return total_score  # Return total_score instead of result

input_file =  'input_1_cap1.txt' #giving values to the variables
result = read_input(input_file) #assigning the result values from the assigned text.
if result:#condition
    total_score = calculate_score(result) #calling the function to run the code
    print("The total score is:", total_score) #Printing out the total score