import pandas as pd

list = []
for line in open('1input.txt','r'):
    list.append(line.strip())

result = [[]]
for i in list:
    if not i:
        result.append([])
    else:
        result[-1].append(i)


#res.sort()
#print((res[-1]))
print(result)