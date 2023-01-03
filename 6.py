with open('6input.txt') as file:
    data = file.read()

#pro kazde i v rozsahu 4 az maximum: s je set z data v rozsahu po i a 4 jeho predchudce, pokud je set s dlouhy 4 znaky, vypis odpoved. (sety nepovoluji duplikaty, takze jakmile najdu set s delkou 4, nalezl jsem marker)
#==========part1=========================
for i in range(4, len(data)):
    s = set(data[(i-4):i])
    if len(s) == 4:
        print("Answer to part1 is:", i)
        break

#==========part2=========================
for i in range(14, len(data)):
    s = set(data[(i-14):i])
    if len(s) == 14:
        print("Answer to part2 is:", i)
        break
