def function(num, limit=20, division_num=3):
    lis = []
    for i in range(num, limit + 1):
        if division_num != 0:
            lis.append(round((i / division_num), 2))
    return lis

print(function(-20))