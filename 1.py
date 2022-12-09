#nacteni dat a vytvoreni listu
with open('1input.in') as file:
    data = [i for i in file.read().strip().split("\n")]

#secteni jednotlivych batohu, prevedeni do int a nalezeni nejvetsiho batohu
max = 0
max2 = 0
max3 = 0
count = 0
for i in data:
    if i == '':
        count = 0
    else:
        num = int(i)
        count += num

    if count > max:
        max3 = max2
        max2 = max
        max = count
    elif count > max2:
        max3 = max2
        max2 = count
    elif count > max3:
        max3 = count
        

print("Answer to part 1 is:", max)
print("Answer to part 2 is:", max+max2+max3)