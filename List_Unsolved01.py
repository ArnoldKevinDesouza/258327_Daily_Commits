# write a program to find the second smallest number in a list

lis=[1, 2, -8, -2, -10, -10]
res = []
for i in lis:
    if i not in res:
        res.append(i)

res.sort()
print(res[1])