print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print("°°°°°°Bienvenido a la tienda°°°°°°°°°°°")
print("°°°°°°°°°°°de  mascotas!°°°°°°°°°°°°°°°")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")


num_perros = 10
num_gatos = 8
num_pajaros = 25
animales_total = num_perros + num_gatos + num_pajaros

print("por favor ingresa tu nombre")
nombre = input()
print("por favor ingresa tu apellido")
apellido = input()

# concatenación
nombre_completo = nombre + " " + apellido
print("gracias por visitarnos,", nombre_completo)


print("actualmente contamos con:")
print("perros:", num_perros, "pajaros:", num_pajaros, "gatos:", num_gatos)
print("En total tenemos", animales_total, "animales")


