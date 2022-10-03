from classes.Product import Product
from classes.Seller import Seller

# Variable
cont = 0
products = []
sellers = []


# Product setters in atributes

def setName():
    name = input("Digite o nome do produto: ")
    if len(name) > 2:
        return name
    else:
        print("O nome do produto deve possuir mais de 2 caracteres!")
        return setName()


def setValue():
    value = float(input("Valor: "))
    if value > 0:
        return value
    else:
        print("O valor deve ser superior à zero!")
        return setValue()


def setQuantity():
    quantity = int(input("Quantidade: "))
    if quantity > 0:
        return quantity
    else:
        print("A quantidade deve ser superior a zero!")
        return setQuantity()


# Seller setters in atributes

def setSellerName():
    name = input("Digite o nome do vendedor: ")
    if len(name) > 3:
        return name
    else:
        print("O nome vendedor deve possuir mais de 3 caracteres!")
        return setName()


def setWage():
    wage = float("Salário: R$ ")
    if wage < 1000:
        print("O salário deve ser superior à R$ 1000,00!")
        return setWage()
    else:
        return wage


def setComission():
    comission = 0.00


# Menu
def menu():
    menu = input("\n ************* MENU ************"
                 "\n\nPara iniciar o cadastro de um novo produto, digite 'add';\n"
                 "Para abrir o cadastro de vendedores, digite 'cdv';\n"
                 "Para abrir o modulo de vendas, digite 'mdv'.\n\n"
                 ).upper()
    return menu

# Seller sign up start
def quantitySellerFunction(sellers):
    cont = 0
    quantity = int(
        input("Digite a quantidade de vendedores à serem cadastrados: "))
    if quantity < 0:
        print("A quantidade informada não pode ser negativa!")
        return quantitySellerFunction()
    else:
        while quantity > cont:
            nameSeller = setSellerName()
            wageSeller = setWage()
            comissionSeller = setComission()
            seller = Seller(nameSeller, wageSeller, comissionSeller)
            sellers.append(seller)
            if cont < quantity:
                menu()
            cont += 1


# Product sign up start
def quantityProductFunction(cont, products, sellers):
    quantity = int(
        input("Digite a quantidade de produtos à serem cadastrados: "))
    if quantity < 0:
        print("A quantidade solicitada não pode ser negativa!")
        return quantityProductFunction()
    else:
        while quantity > cont:
            nameProduct = setName()
            valueProduct = setValue()
            quantityProduct = setQuantity()
            prod = Product(nameProduct, valueProduct, quantityProduct)
            validationProduct = input("\n ***** PRODUTO ******" +
                        "Nome do produto: " + prod.getName()
                        + "\nValor do produto: " + prod.getValue()
                        + "\nQuantidade do produto: " + prod.getQuantity()
                        + "\nDeseja cadastrar esse produto?[s/n] "
            ).upper()
            if validationProduct == "SIM":
                products.append(prod)
                cont += 1
                if cont < quantity:
                    menu = menu()
                    if menu == "CDV":
                        return quantitySellerFunction(sellers)
                else:
                    quantitySellerFunction(sellers)
            else:
                print("Então cadastre outro produto.")
                return quantityProductFunction(cont, products, sellers)


quantityProductFunction(cont, products, sellers)