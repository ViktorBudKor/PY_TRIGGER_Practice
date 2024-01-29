num_1 = int(input())
num_2 = int(input())
sign = input()
if sign =="+":
    print(num_1 + num_2)
elif sign == "-":
    print(num_1 - num_2)
elif sign == "/" and num_2!=num_1!=0:
    print(num_1 / num_2)
elif sign == "*":
    print(num_1 * num_2)