# Imports classes
from classes.Sale import Sale
from classes.Product import Product
from classes.Seller import Seller
from classes.Data import Data
from classes.Seller_Product import Seller_Product

# Creat and add product
def creatProduct(data):
    print("\nIniciando cadastro de produto...\n")
    while True:
        name = input("Nome: ")
        if name.upper() == "FIM":
            return
        if len(name) > 3:
            validation = data.verificationNameProduct(name)
            if not validation:
                break
            mensage = input("O produto já está cadastrado.\nDeseja aumentar a quantidade em estoque? [s/n] ").upper()
            if mensage == "S":
                try:
                    quantity = int(input("Quantidade à ser adicionada: "))
                except:
                    print("O valor inserido deve ser um número!")
                else:
                    validation.addQuantity(quantity)
                return
        print("O nome do produto deve ter mais que 3 caracteres! Informe novamente.")
    while True:
        try:
            value = float(input("Valor: R$ "))
        except:
            print("O Valor informado precisa ser um valor numérico!")
        else:
            if value > 0:
                 break
            print("O valor não pode ser nulo ou negativo! Informe novamente.")
    while True:
        try:
            quantity = int(input("Quantidade: "))
        except:
            print("A quantidade deve ser um valor inteiro!")
        else:
            if quantity > 0:
                break
            print("A quantidade deve ser superior a 0! Informe novamente.")
    mensage = "\nDeseja cadastrar esse produto? [s/n] "
    if input(mensage).upper() == "S":
        product = Product(name, value, quantity)
        data.addProduct(product)
        mensage = ("\nProduto cadastrado com sucesso.\nDeseja iniciar o cadastro de um novo produto? [s/n] ")
        if input(mensage).upper() == "S":
            return creatProduct(data)
        return product
    else:
        mensage = "\nDados descartados. Deseja iniciar o cadastro de um outro produto? [s/n] "
        if input(mensage).upper() == "S":
            return creatProduct(data)
        return False
 

# Creat and add seller
def creatSeller(data):
    print("\nIniciando cadastro de vendedor...\n")
    while True:
        name = input("Nome: ")
        if name.upper() == "FIM":
            return
        if len(name) > 3:
            validation = data.verificationNameSeller(name)
            if not validation:
                break
            mensage = input("O vendedor já está cadastrado.\nDeseja cadastrar um novo? [s/n] ").upper()
            if mensage == "FIM":
                return
            if mensage == "S":
                return creatSeller(data)
        print("O nome do vendedor deve ter mais que 3 caracteres! Informe novamente.")
    while True:
        try:
            salary = float(input("Salário: R$ "))
        except:
            print("O salário deve ser informado em números!")
        else:
            if salary >= 1000:
                 break
            print("O salário do vendedor deve ser maior que R$ 1000.00! Informe novamente.")
    mensage = "\nDeseja cadastrar esse vendedor? [s/n] "
    if input(mensage).upper() == "S":
        seller = Seller(name, salary)
        data.addSeller(seller)
        mensage = ("\nVendedor cadastrado com sucesso.\nDeseja iniciar o cadastro de um novo vendedor? [s/n] ")
        if input(mensage).upper() == "S":
            return creatSeller(data)
        return seller
    else:
        mensage = "\nDados descartados. Deseja iniciar o cadastro de um outro vendedor? [s/n] "
        if input(mensage).upper() == "S":
            return creatSeller(data)
        return False
    

# Start a sale
def startSale(data, sellerSale):
         global module
         sellerProduct = []
         print("\nIniciando a venda...\n")
         print(f'Venda número: {module}')
         if sellerSale:
             while True:
                 name = input("Nome do vendedor: ")
                 seller = data.verificationNameSeller(name)
                 if name.upper() == "FIM":
                     return
                 if not seller:
                     print("O vendedor infromado não existe!\nTente novamente.")
                 else:
                     break
         teste = True
         while teste:
             while True:
                 name = input("Nome do produto: ")
                 product = data.verificationNameProduct(name)
                 if name.upper() == "FIM":
                     return
                 if not product:
                     print("O produto informado não existe!\nTente novamente.")
                 else:
                     sellerSale = False
                     break
             while True:
                 try:
                    quantity = int(input("Quantidade à ser vendida: "))
                 except:
                    print("A quantidade deve ser um valor inteiro!")
                 else:
                    if product.getQuantity() > quantity:
                        sellerProduct.append(Seller_Product(seller, product, quantity))
                        mensage = input("Deseja acrescentar outro produto a está venda? [s/n] ").upper()
                        if not mensage == "S":
                            teste = False
                        break
                    else:
                        print("A quantidade deve ser inferior à que està em estoque! \nInforme novamente.")
         sale = Sale(module, sellerProduct, seller)
         print(f'Valor total da venda: R$ {sale.getTotalValue()}')
         mensage = input("Deseja efetuar esta venda? [s/n] ").upper()
         if mensage == "S":
             sellerSale = True
             sale.actuaQuantity()
             data.addSale(sale)
             seller.setComission(sale.getTotalValue())
             print(f'Venda {module} realizada!')
             module += 1
             mensage = input("\nDeseja realizar uma nova venda? [s/n] ").upper()
             if mensage == "S":
                 return startSale(data, sellerSale)
         else:
            mensage = "\nDados descartados. Deseja iniciar o uma outra venda? [s/n] "
            if input(mensage).upper() == "S":
                return startSale(data, sellerSale)
         return False
         
         
# Variables
generalData = Data()
module = 1
while True:
    mensage = input("\n[1] Cadastro de produtos \n[2] Cadastro de vendedores \n[3] Módulo de vendas \n[4] Produtos em estoque \n[5] Vendedores cadastrados \n[6] Histórico de vendas \n[7] Finalizar o sistema \nDigite: ")
    print('\n[OBS: Caso desejar voltar para o menu, digite "fim" em qualquer campo que pede um nome.]')
    if mensage == "1":
        creatProduct(generalData)
    elif mensage == "2":
        creatSeller(generalData)
    elif mensage == "3":
        if generalData.getSellers():
            if generalData.getProducts():
                sellerSale = True
                startSale(generalData, sellerSale)
            else:
                print("\nNão há nenhum produto cadastrado.\nCadastre um antes de acessar o modulo de vendas.")
                creatProduct(generalData)
        else:
            print("\nNão há nenhum vendedor cadastrado.\nCadastre um antes de acessar o modulo de vendas.")
            creatSeller(generalData)
    elif mensage == "4":
        generalData.showProductStock()
    elif mensage == "5":
        generalData.showSellers()
    elif mensage == "6":
        generalData.showSales()
    elif mensage == "7":
         print("\nFinalizando o sistema...")
         break
    else: 
        print("\nInforme um dos valores mostrados!")