#initialize solution
total_score1=0
total_score2=0

# Read file and append to list "readList"
with open('strategyGuide.txt') as my_file:
     readList = my_file.readlines()

#Clean up readList and append to strategyList
strategyList = [item.replace('\n', '') for item in readList]

#Mapping pairs to points for each challenge
score1 = {
    'A X': 4, 'A Y': 8, 'A Z': 3,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 7, 'C Y': 2, 'C Z': 6
        }
score2= {
    'A X': 3, 'A Y': 4, 'A Z': 8,
    'B X': 1, 'B Y': 5, 'B Z': 9,
    'C X': 2, 'C Y': 6, 'C Z': 7
}

#Adding points of each round for both total scores
for i in range (len(strategyList)):
    total_score1 += score1[strategyList[i]]
    total_score2 += score2[strategyList[i]]
    
#Printing out the total score for each challenge
print("First score:", total_score1)
print("Second score:", total_score2)