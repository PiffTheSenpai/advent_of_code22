

list = []
for line in open('1input.txt','r'):
    list.append(line.strip())

result = [[]]
for i in list:
    if not i:
        result.append([])
    else:
        result[-1].append(int(i))

add = []
for i in range(len(result)):
	sum += result[i]

print(add) 
#print(result.sort())
#print((res[-1]))