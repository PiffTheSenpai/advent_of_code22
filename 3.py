#The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.
from string import ascii_letters

with open('3input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

total = 0
for rucksack in data:
    half = len(rucksack)//2 #rozdeleni rucksaku na polovinu
    
    left = set(rucksack[:half]) #leva cast = od zacatku do poloviny 
    right = set(rucksack[half:]) #prava cast = od poloviny do konce
    
    for priority, char in enumerate(ascii_letters): #ascii znaky jsou namapovane na cisla+1
        if char in left and char in right:
            total += priority + 1

print("Answer to part1 is:", total)

# === part2 ===
total2 = 0

j = 3
for i in range(0, len(data), 3): #pro i v rozsahu od 0 do celkoveho poctu dat, jdi po trech krocich
    rucksack = data[i:j] #rucksack je i az j(j = 3 na zacatku a pak zvetsujeme o 3)
    j += 3

    for priority, char in enumerate(ascii_letters): 
        if char in rucksack[0] and char in rucksack[1] and char in rucksack[2]: #jestli je znak v batohu 1,2,3 pricti jejich prioritu(ciselnou reprezentaci), kterou ziskavame z ascii mapovani a + 1, protoze zacina v 0
            total2 += priority + 1

print("Answer to part2 is:", total2)
