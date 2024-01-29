try:
    file = open('example.txt', 'x')
    file.close()
except FileExistsError:
    print("Файл не обнаружен")