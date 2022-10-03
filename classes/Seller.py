class Seller:
    def __init__(self, name, wage, comission):
        self.__name = name
        self.__wage = wage
        self.__comission = comission
    
    def setName(self, name):
        self.__name = name

    def setWage(self, wage):
        self.__wage = wage

    def setName(self, comission):
        self.__comission = comission

    def getName(self):
        return self.__name

    def getWage(self):
        return self.__wage

    def getComission(self):
        return self.__comission