class Seller:
    # Atributes
    __name: str
    __salary: float
    __comission: float = 0.00
    __info: str
    
    #Construct method
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
     
     #Magic methods
    def __str__(self):
        self.__info = f'Nome do vendedor: {self.getName()} \nSalário: R$ {self.getSalary()} \nComissão: R$ {self.getComission()} \nSalário total: R$ {self.getTotalSalary()}'
        return self.__info
        
     # Setters methods
    def setName(self, name):
        self.__name = name
     
    def setSalary(self, salary):
         self.__salary = salary
      
    def setComission(self, value):
          self.__comission += (value * 0.1)
     
     #Getters methods
    def getName(self):
        return self.__name
        
    def getSalary(self):
        return self.__salary
     
    def getComission(self):
        return self.__comission
                  
    def getTotalSalary(self):
        return self.__salary + self.__comission