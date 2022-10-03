class Product:
    def __init__(self, name, value, quantity):
        self.__name = name
        self.__value = value
        self.__quantity = quantity

    def setName(self, name):
        self.__name = name

    def setValue(self, value):
        self.__value = value

    def setName(self, quantity):
        self.__quantity = quantity

    def getName(self):
        return self.__name

    def getValue(self):
        return self.__value

    def getQuantity(self):
        return self.__quantity