print("Bienvenido al conversor de millas a kilometros")

print("escribe un numero de millas")
millas = input()

print("Tipo de dato de millas", type(millas))
# COnvertir str a numero
millas = float(millas)

print("Tipo de dato de millas", type(millas))


# 1 milla = 1.60934 km
kilometros = millas * 1.609


print("millas ingresadas:", millas)
print("kilometros:", kilometros)