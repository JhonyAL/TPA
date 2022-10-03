from classes.Product import Product

# Variable
cont = 0
products = []

def setName(products, cont):
    name = input("Digite o nome do produto: ")
    prod = Product()
    prod.setName(name)
    products.append(prod)

def quantityFunction(cont, products):
    quantity = int(input("Digite a quantidade de produtos à serem cadastrados: "))
    if quantity < 0:
        print("A quantidade solicitada não pode ser negativa!")
        return quantityFunction()
    else:
        while quantity > cont:
            setName(products, cont)
            cont += 1

        for product in products:
            print(product.setName())

quantityFunction(cont, products)