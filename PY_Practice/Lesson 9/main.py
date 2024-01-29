class Car:

    def __init__(self, brand, type,color):
        self.__brand = brand
        self.__type = type
        self.__IsEngineOn = False
        self.__color = color
        self.__IsOpenTrunk = False
        self.__IsLightOn = False
        self.__IsLocked = False

    def StartEngine(self):
        self.__IsEngineOn = True
        self.__IsLightOn = True

    def StopEngine(self):
        self.__IsEngineOn = False
        self.__IsLightOn = False

    def LightOn(self):
        if self.__IsLocked == False:
            if self.__IsLightOn == False:
                self.__IsLightOn = True
                print("Фары включены")
            else:
                print("Фары уже включены")
        else:
            print("Машина закрыта, фары не могут быть включены")

    def LightOFF(self):
        if self.__IsLightOn == True:
            self.__IsLightOn = False
            print("Фары выключены")
        else:
            print("Фары уже выключены")

    def SignalingON(self):
        if self.__IsLocked == True:
            print("Машина уже закрыта")
        else:
            if self.__IsOpenTrunk == True:
                print("Вы забыли закрыть багажник")
            elif self.__IsEngineOn == True:
                print("Вы не заглушили авто, сигнализация не активирована")
            else:
                self.__IsLocked = True
                self.__IsLightOn = False

    def SignalingOFF(self):
        if self.__IsLocked == False:
            print("Машина уже открыта")
        else:
            self.__IsLocked = False
    def GetInfo(self):
        print("*" * 50)
        print(f"Бренд:{self.__brand}", f"Тип авто:{self.__type}",f"Цвет авто:{self.__color}", f"Двигатель заведен:{self.__IsEngineOn}", f"Свет включен:{self.__IsLightOn}",
              f"Багажник открыт:{self.__IsOpenTrunk}", f"Машина на сигнализации:{self.__IsLocked}",sep='\n')
        print("*" * 50)
    def SetColor(self):
        print("В какой цвет вы покрасите ваш авто?")
        self.__color = input()



car1 = Car("Toyota", "Седан", "Красный")
car1.GetInfo()
car1.StartEngine()
car1.SignalingON()
car1.StopEngine()
car1.LightOn()
car1.SignalingON()
car1.SetColor()
car1.GetInfo()