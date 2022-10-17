class Product:
    # Atributes
    __name: str
    __value: float
    __quantity: int
    __info: str
    
    #Construct method
    def __init__(self, name, value, quantity):
        self.__name = name
        self.__value = value
        self.__quantity = quantity
     
     #Magic methods
    def __str__(self):
        self.__info = f'Nome do produto: {self.__name} \nValor unitário: R$ {self.__value} \nQuantidade em estoque: {self.__quantity}'
        return self.__info
        
     # Setters methods
    def setName(self, name):
        self.__name = name
     
    def setValue(self, value):
         self.__value = value
      
    def setQuantity(self, quantity):
          self.__quantity = quantity
     
     #Getters methods
    def getName(self):
        return self.__name
        
    def getValue(self):
        return self.__value
                  
    def getQuantity(self):
        return self.__quantity
     
    def addQuantity(self, quantity):
        self.__quantity += quantity  