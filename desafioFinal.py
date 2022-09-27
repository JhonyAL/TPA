# List start
historic = []
general_list = []


def productCont():
    contProd = int(input("Informe a quantidade de produtos que deseja cadastrar: "))
    if contProd < 0:
        print("A quantidade não pode ser negativa.")
        return productCont()
    else:
        return historic.append(contProd)

def productName():
    print("\n\n*****Adicionando produto*****\n")
    nameProd = input("Informe o nome do produto: ")
    if len(nameProd) < 2:
        print("O nome deve ser maior do que 2 caracteres.")
        return productName()
    else:
        return historic.append(str(nameProd))

def productQuant():
    quantProd = int(input("Informe a quantidade do produto: "))
    if quantProd < 1:
        print("A quantidade do produto deve ser maior do que 0.")
        return productQuant()
    else:
        return historic.append(quantProd)

def productValor():
    valorProd = float(input("Informe o valor do produto: "))
    if valorProd < 0:
        print("O valor deve ser maior do que 0.")
        return productValor()
    else:
        return historic.append(valorProd)

def clearList():
    historic = []
    return historic

def addListaGeral():
    print("\n\n*****Revisão do produto*****\n")
    print("Nome do produto: "+str(historic[1]))
    print("Quantidade do produto: "+str(historic[2]))
    print("Valor do produto: R$"+str(historic[3]))
    addList = input("Confirmar produto S/N\n").upper()
    if addList == "S":
        return True
    else:
        menu()

def menu():
    openMenu = input(
    '\n******* MENU *******\n'
    'Para adicionar outro produto digite  "add"\n'
    'Acessar cadastro de vendedores digite "CV"\n'
    'Acessar módulo de vendas "MV"\n'
    'digite: '

    ).upper()

    if openMenu == "ADD":
        loop()

    if len(openMenu) <= 0:
        print("Insira um valor")
        menu()

def loop():
    productName()
    productQuant()
    productValor()
    includeProduct()

def includeProduct():
    if addListaGeral() == True:
        general_list.append(historic)
        menu()
    

# Controle de funções
    
productCont()
productName()
productQuant()
productValor()
includeProduct()