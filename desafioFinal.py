# Create lists
historic = []
generalList = []
sellers = []
amountProduct = []
product = []

# Function for add name in product


def productName():
    cont = 0
    cont += 1
    print("\n*****Adicionando produto*****\n")
    nameProd = input("Informe o nome do produto: ")
    if len(nameProd) < 2:
        print("O nome do produto deve ser possuir mais que 2 caracteres.")
        return productName()
    else:
        return historic.append(nameProd)

# Function for add amount in product


def productQuant():
    quantProd = int(input("Informe a quantidade do produto: "))
    if quantProd < 1:
        print("A quantidade do produto deve ser maior do que 0.")
        return productQuant()
    else:
        return historic.append(quantProd)

# Function for add values in product


def productInsertValue():
    valueProduct = float(input("Informe o valor do produto: "))
    if valueProduct <= 0:
        print("O valor deve ser maior do que 0.")
        return productInsertValue()
    else:
        return historic.append(valueProduct)

# Comission function


def sellerInsertComission():
    comission = 0
    return historic.append(comission)

# Function for add seller name


def sellerInsertName():
    nameSeller = str(input("Digite o nome do vendedor: "))
    if len(nameSeller) < 4:
        print("O nome do vendedor deve possuir mais que de 3 caracteres!")
        return sellerInsertName()
    else:
        return historic.append(nameSeller)

# Function for add seller wage


def sellerInsertWage():
    sellerWage = float(input("Digite o salário do vendedor: "))
    if sellerWage <= 1000:
        print("O salário do vendedor deve possuir maior que R$ 1.000!")
        return sellerInsertWage()
    else:
        sellerInsertComission()
        return historic.append(sellerWage)

# Funtion for end program


def endProgram():
    print("Programa finalizado...")
    exit()

# Function for clear historic


def clearHistoric():
    global historic
    historic = historic * 0

# Function for add product in general list


def addGeneralList():
    print("\n*****Revisão do produto*****")
    print("Nome do produto: "+str(historic[0]))
    print("Quantidade do produto: "+str(historic[1]))
    print("Valor do produto: R$"+str(historic[2]))
    addList = input("Confirmar produto S/N: \n").upper()
    if addList == "S":
        generalList.append(historic)
        return True
    else:
        clearHistoric()
        menu()

# função de contagem de produtos


def cont_products():
    global amountProduct
    global product
    strProduct = str(amountProduct)
    if len(strProduct) >= 1:
        amountProduct = amountProduct[0] - 1
        return product.append(amountProduct)


# função de menu
def menu():
    print('******* MENU *******\n'
          'Para adicionar outro produto digite  "add"\n'
          'Acessar cadastro de sellers digite "CV"\n'
          'Acessar módulo de vendas "MV"\n'
          'Para finalizar o programa "exit"')
    openMenu = input('digite: ').upper()

    if openMenu == "ADD":
        clearHistoric()
        loop()

    if openMenu == "CV":
        clearHistoric()
        sellerInsertName()
        sellerInsertWage()
        print(historic)
        exit()

    if len(openMenu) <= 0:
        print("Insira um valor")
        menu()

    if openMenu == "EXIT":
        endProgram()

# função de loop


def loop():
    productName()
    productQuant()
    productInsertValue()
    includeProduct()

# função de incluir produtos


def includeProduct():
    if addGeneralList() == True:
        generalList.append(historic)
        # print(generalList)
        menu()


def includeVendedor():
    if sellerInsertName():
        print("Histórico sellers: "+str(historic))

# Function start


def start():
    starting = input(
        '*****DESAFIO FINAL*****\n'
        'Para continuar o cadastro de produto "continuar"\n'
        'Para ir ao menu interativo "menu"\n'
        'Digite: '
    ).upper()

    if starting == "CONTINUAR":
        productCont()
    elif starting == "MENU":
        menu()
    else:
        print("Insira um dos dois valores anteriores!\n\n")
        return start()

# Function for add values in variables


def productCont():
    contProd = int(
        input("Informe a quantidade de produtos que deseja cadastrar: "))
    if contProd < 1:
        print("A quantidade não pode ser negativa ou nula!\n")
        productCont()
    else:
        amountProduct.append(contProd)
        loop()

# Controle de funções


start()
