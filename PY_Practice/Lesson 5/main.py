i = 100
while i > 0:
    if (i != 55) and (i !=99):
        print(i, end=' ')
        i -= 1
    else:
        i -= 1

lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
min_num = lis[0]
for i in range(len(lis)):
    if min_num > lis[i]:
        min_num = lis[i]
lis.remove(min_num)
if min_num > 0:
    lis.insert(0, min_num)
else:
    lis.append(min_num)
print("\n", lis)