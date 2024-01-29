import random
random_num = random.randint(10,30)

while True:
    try:
        inNum = int(input())
        break
    except ValueError:
        print("Введите число!")

while random_num != inNum:
    if inNum > random_num:
        print("Ваше число больше")
    elif inNum < random_num:
        print("Ваше число меньше")
    while True:
        try:
            inNum = int(input())
            break
        except ValueError:
            print("Введите число!")
print("Вы угадали")