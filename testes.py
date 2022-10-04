from classes.Product import Product

prod = []

p1 = Product("Banana", 13, 2)
p2 = Product("Feijão", 10, 4)
prod.append(p1)
prod.append(p2)

for prods in prod:
    if prods.getQuantity() > 3:
        pp = prods
        pp.setName("Arroz")

print(prod[1].getName())

print(p1.getName())
p1.setName("Arroz")
print(p1.getName())