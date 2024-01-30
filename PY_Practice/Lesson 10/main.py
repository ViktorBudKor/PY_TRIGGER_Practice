class Car:
    __weight =0
    __color = ""
    __power = 0
    _wheels = 4

    def __init__(self, brand, power, weight, color):
        self.__brand = brand
        self.__power = power
        self.__weight = weight
        self.__color = color




    def GetInfo(self):
        print("*" * 50)
        print(f"Бренд:{self.__brand}", f"Цвет:{self.__color}",f"Вес:{self.__weight}",f"Мощность:{self.__power}", f"Количество колес:{self._wheels}", sep='\n')
        print("*" * 50)
    def SetColor(self):
        print("В какой цвет вы покрасите?")
        self.__color = input()

class Motorcycle(Car):
    _wheels = 2


moto = Motorcycle("Kawasaki",100,1000,"Red")
print(moto.GetInfo())
moto.SetColor()
print(moto.GetInfo())
car1 = Car("Toyota", 144,1670,"White")
car1.GetInfo()