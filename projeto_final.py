cont = 0

def quantFunc():
    quant = int(input("Informe a quantidade de produtos desejados para serem inseriodos: "))
    if quant < 0:
        print("O número informado não pode ser negativo!")
        return quantFunc()
    else:
        return quant

def nameInsert():
    nameProduct = input("Nome do produto: ")
    return len(nameProduct)

def quantInsert():
    quantProduct = int(input("Quantidade: "))
    return quantProduct

def valueInsert():
    valueProduct = float(input("Valor: "))
    return valueProduct

def validationValue():
    if valueInsert() > 0:
        return
    else:
        print("O valor inserido deve ser maior que 0!")
        return validationValue()

def validationQuant():
    if quantInsert() > 0:
        validationValue()
    else:
        print("A quantidade inserida deve ser maior que 0!")
        return validationQuant()

def validationName():
    if nameInsert() > 2:
        validationQuant()
    else:
        print("O nome do produto deve ser superior à 2 caracteres!")
        return validationName()

def signUpProduct():
    validationName()
    menu = (input("\n*************       Menu:       ***************** \n\n Cadastrar um novo produto: Digite c; \n Cadastro de vendedores: Digite v; \n Módulo de vendas: mv \n\n")).upper()
    if menu == "C":
        return signUpProduct()
    elif menu == "V":
        return signUpSeller()
    else:
        return moduleSales()

while cont < quantFunc():
    cont += 1
    signUpProduct()