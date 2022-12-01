import os

path = "/home/nick/Desktop/AoD/adventDay01"
os.chdir(path)


lst = []
with open('elfCalories.txt') as my_file:
     lst = my_file.readlines()

elfs = [item.replace('\r', '').replace('\n', '') for item in lst]
print(elfs)

sum = 0
max = -1




for i in range(len(elfs)):
    if elfs[i] != '':
        sum = sum + int(elfs[i])
        if sum > max:
            max = sum
    else:
        sum = 0

print (max)    


