import string

#initialize sums
first_priority_sum=0
second_priority_sum=0

#Read file and append to list "readList"
with open('rucksacks.txt') as my_file:
     readList = my_file.readlines()

#Clean up readList and append to rucksacks
rucksacks = [item.replace('\n', '') for item in readList]

#Corresponging each letter of the alphabet to a value (a-Z, 1-52)
item_priority = dict()
for i, letter in enumerate(string.ascii_letters):
   item_priority[letter] = i + 1

for i in range (len(rucksacks)):
    #Distinguishing first and second compartment 
    first_compartment, second_compartment = rucksacks[i][:len(rucksacks[i])//2], rucksacks[i][len(rucksacks[i])//2:]
    #Find common item
    common_item = ''.join(set(first_compartment).intersection(second_compartment))
    #Adding up sum of item priority
    first_priority_sum += item_priority[common_item]

print("Sum of priority items that appear in both compartments:", first_priority_sum)

for i in range (0,len(rucksacks)-2,3):
    #Find common item
    common_item = ''.join(
    set(rucksacks[i]).intersection(rucksacks[i+1]).intersection(rucksacks[i+2]))
    #Adding up sum of item priority
    second_priority_sum += item_priority[common_item]

print("Sum of priority type for each three-Elf group:",second_priority_sum)



