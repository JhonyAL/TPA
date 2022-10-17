from classes.Seller import Seller
from classes.Seller_Product import Seller_Product

class Sale:
    __module: int
    __sellerProduct: list[Seller_Product] = []
    __totalValue: float = 0.00
    __info: str = ""
    __seller: Seller
    __msg: str = ""
    
    def __init__(self, module, sellerProduct, seller):
        self.__module = module
        self.__sellerProduct = sellerProduct
        self.__seller = seller
        self.totalValue(sellerProduct)

    def totalValue(self, sellerProduct):
        for saleProduct in sellerProduct:
            self.__totalValue += saleProduct.getTotalValue()
    
    def getTotalValue(self):
        return self.__totalValue
    
    def showProductsSale(self):
        for saleProduct in self.__sellerProduct:
            self.__msg += saleProduct.info()
        return self.__msg
    
    def actuaQuantity(self):
        for productSeller in self.__sellerProduct:
            productSeller.quantity()
    
    def info(self):
        self.__info = f'Venda número {self.__module} \nRealizada pelo vendedor: {self.__seller.getName()}\n\n ******* Produtos vendidos ***** \n\n{self.showProductsSale()} \nValor total da venda: R$ {self.getTotalValue()}'
        return self.__info