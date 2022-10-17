from classes.Sale import Sale
from classes.Product import Product
from classes.Seller import Seller

class Data:
        # Atributes
        __products: list[Product] = []
        __sellers: list[Seller] = []
        __sales: list[Sale] = []
        
        def getProducts(self):
            return self.__products
        
        def getSellers(self):
            return self.__sellers
        
        # Append product in product list
        def addProduct(self, product: Product):
            self.__products.append(product)
         
        def showProductStock(self):
            print("\n**** Estoque de produtos *****\n")
            for product in self.__products:
                print(product)
                print("\n")
                
        # Append product in product list
        def addSeller(self, seller: Seller):
            self.__sellers.append(seller)
         
        def showSellers(self):
            print("\n**** Vendedores cadastrados *****\n")
            for seller in self.__sellers:
                print(seller)
                print("\n")
                
        def addSale(self, sale: Sale):
                self.__sales.append(sale)
                
        def showSales(self):
            print("\n**** Histórico de vendas *****\n")
            for sale in self.__sales:
                print(sale.info())
                print("\n")
            
        def verificationNameSeller(self, name):
            for seller in self.__sellers:
                if seller.getName() == name:
                    return seller
            return False
                
        def verificationNameProduct(self, name):
           for product in self.__products:
               if product.getName() == name:
                   return product
           return False