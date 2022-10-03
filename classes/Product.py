class Product:
    def __init__(self, name, value, quantity):
        self.__name = name
        self.__value = value
        self.__quantity = quantity

    def __init__(self):
        self.__name = ""
        self.__value = 0.00
        self.__quantity = 0

    def getName(self):
        return self.__name

    def getValue(self):
        return self.__value

    def getQuantity(self):
        return self.__quantity