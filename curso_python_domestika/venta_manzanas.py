print("Bienvenido a la tienda de manzanas")

print("por favor ingresa tu nombre")
nombre = input()
manzana = 5
disponible = 20

print("Holaa", nombre, "gracias por visitarnos", "actualmente tenemos", disponible, "manzanas disponibles")
print("cada manzana tiene un costo de", manzana, "pesos")
print("Cuantas manzanas desea comprar?")
print("por favor ingresa el numero de manzanas")

man_compra = input()
man_compra = int(man_compra)

print(nombre, "usted desea comprar", man_compra, "manzanas")
print("el total de su compra es de", man_compra * manzana, "pesos")
print("en total quedan", disponible - man_compra, "manzanas disponibles")
