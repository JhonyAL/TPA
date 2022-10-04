from classes.Product import Product
from classes.Seller import Seller

# Variable
cont = 0
products = []
sellers = []


# Inform name seller for sales module
def setNameSellerModule(sellers):
    nameSeller = input("Nome do vendeddor: ")
    for sellerUnity in sellers:
        if sellerUnity.getName() == nameSeller:
            return sellerUnity
    print("O vendedor informado não existe!")
    return setNameSellerModule(sellers)


# Inform name product for sales module
def setNameProductModule(products):
    nameProduct = input("Nome do produto: ")
    for productUnity in products:
        if nameProduct == productUnity.getName():
            return productUnity
    print("O produto informado não existe!")
    return setNameProductModule(products)


# Inform quantity product for sales module
def setQuantityProductModule(product):
    quantityProduct = int(input("Quantidade para venda: "))
    quantity = product.getQuantity()
    if quantityProduct > quantity:
        print(
            "A quantidade informada não pode ultrapassar a quantidade em estoque!")
        return setQuantityProductModule(product)
    product.setQuantity(quantity - quantityProduct)
    return quantityProduct


# Total value of the sale
def valueSalesModule(product, quantity):
    valueProduct = product.getValue()
    return valueProduct * quantity


# Set comission for seller
def setValueSalesSeller(seller, valueTot):
    comission = seller.getComission()
    comission += (valueTot * 10) / 100
    seller.setComission(comission)


# Sales module start
def salesModule(products, sellers, cont):
    cont = 1
    if len(products):
        if len(sellers):
            print("Venda número " + str(cont))
            seller = setNameSellerModule(sellers)
            product = setNameProductModule(products)
            quantityProduct = setQuantityProductModule(product)
            valueTot = valueSalesModule(product, quantityProduct)
            setValueSalesSeller(seller, valueTot)
            print(product.getName() + " | " + product.getQuantity + " unidades em estoque.")
            print("Venda " + str(cont) + " realizada pelo vendedor " seller.getName() + " no valor total de R$ " + )
        else:
            print("Não há nenhum vendedor cadastrado! Cadastre no minímo um vendedor para acessar o modulo de vendas.")
            return quantityProductFunction(cont, products, sellers)
    else:
        print("Não há nenhum produto cadastrado! Cadastre no minímo um produto para acessar o modulo de vendas.")
        return quantityProductFunction(cont, products, sellers)


# Seller setters in atributes
def setSellerName():
    name = input("Digite o nome do vendedor: ")
    if len(name) > 3:
        return name
    else:
        print("O nome vendedor deve possuir mais de 3 caracteres!")
        return setName()


def setWage():
    wage = float(input("Salário: R$ "))
    if wage < 1000:
        print("O salário deve ser superior à R$ 1000,00!")
        return setWage()
    else:
        return wage


def setComission():
    comission = 0.00
    return comission


# Menu
def menu(text, twoText):
    print("\n ************* MENU ************"
          "\n\nPara iniciar o cadastro de um novo " + text + ", digite 'add';\n"
          "Para abrir o cadastro de " + twoText + ", digite 'cdv';\n"
          "Para abrir o modulo de vendas, digite 'mdv'."
          )
    menu = input("Digite: ").upper()
    return menu


# Seller sign up start
def quantitySellerFunction(sellers):
    print("\nIniciando cadastro de vendedores...\n")
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

            print("\n ***** VENDEDOR ****** \n\nNome: " + seller.getName() + "\nSalário: " +
                  str(seller.getWage()) + "\nComissão: " + str(seller.getComission()))
            validationSeller = input(
                "\nDeseja cadastrar esse vendedor?[s/n] ").upper()
            if validationSeller == "S" or validationSeller == "SIM":
                sellers.append(seller)
                cont += 1
                if cont < quantity:
                    if menu("vendedor", "produtos") == "CDV":
                        return quantitySellerFunction(sellers)
                else:
                    print(
                        "\n******** A QUANTIDADE DE VENDEDORES A SEREM CADASTRADOS FOI PREENCHIDA ******\n")
                    return salesModule(products, sellers, cont)
            else:
                print("Então cadastre outro produto.")
                return salesModule(products, sellers, cont)


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
            print("\n ***** PRODUTO ****** \n\nNome: " + prod.getName() + "\nValor: " +
                  str(prod.getValue()) + "\nQuantidade: " + str(prod.getQuantity()))
            validationProduct = input(
                "\nDeseja cadastrar esse produto?[s/n]").upper()
            if validationProduct == "S" or validationProduct == "SIM":
                products.append(prod)
                cont += 1
                if cont < quantity:
                    if menu("produto", "vendedores") == "CDV":
                        return quantitySellerFunction(sellers)
                else:
                    print(
                        "\n******** A QUANTIDADE DE PRODUTOS A SEREM CADASTRADOS FOI PREENCHIDA ******\n")
                    quantitySellerFunction(sellers)
            else:
                print("Então cadastre outro produto.")
                return quantityProductFunction(cont, products, sellers)


# Start system
quantityProductFunction(cont, products, sellers)
