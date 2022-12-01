
#Initialize variables
sum = 0                  
solution2=0
caloryElfs = []
readList = []

#Read file and append to list "readList"
with open('elfCalories.txt') as my_file:
     readList = my_file.readlines()

#Clean up readList and append to elfs
elfs = [item.replace('\n', '') for item in readList]

#Create new list caloryElfs with the sums of Calories from each elf
for i in range(len(elfs)):
    if elfs[i] != '':
        sum = sum + int(elfs[i])
    else:
        caloryElfs.append(sum)
        sum = 0

#Sort list caloryElfs from high to low
caloryElfs.sort(reverse=True)

#Sum up the top 3 elfs from sorted caloryElf list. This is for the second part of the challenge
for i in range (0,3):
    solution2 = solution2 + caloryElfs[i]

#First index of sorted caloryElfs list is our solution for the first part of the challenge
solution1 = caloryElfs[0]
print("Highest calory elf:", solution1)
print("Sum of top 3 calory elfs:", solution2)

