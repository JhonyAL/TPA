class Seller_Product:
    __product: Product
    __seller: Seller
    __quantity: int
    __totalValue: float
    __info: str
    
    def __init__(self, seller, product, quantity):
        self.__seller = seller
        self.__product = product
        self.__quantity = quantity
        self.setTotalValue(product, quantity)
   
    def quantity(self):
        self.__preguicaa = self.__product.getQuantity() - self.__quantity
        self.__product.setQuantity(self.__preguicaa)
    
    def setTotalValue(self, product, quantity):
       self.__totalValue = product.getValue() * quantity
   
    def getNameProduct(self):
       return self.__product.getName()
       
    def getValueProduct(self):
       return self.__product.getValue()
       
    def getQuantity(self):
       return self.__quantity
      
    def getTotalValue(self):
       return self.__totalValue
     
    def getNameSeller(self):
       return self.__seller.getName()

    def info(self):
        self.__info = f'Nome do produto: {self.getNameProduct()} \nPreço unitário: R$ {self.getValueProduct()} \nQuantidade vendida: {self.getQuantity()} \nQuantidade restante: {self.__product.getQuantity()}\n\n'
        return self.__info