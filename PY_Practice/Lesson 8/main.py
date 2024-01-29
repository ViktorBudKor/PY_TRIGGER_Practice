import random
random_num = random.randint(10,30)
inNum = int(input())
while random_num != inNum:
    if inNum > random_num:
        print("Ваше число больше")
    elif inNum < random_num:
        print("Ваше число меньше")
    inNum = int(input())
print("Вы угадали")