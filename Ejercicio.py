# Ejercicio:una pelota se deja caer de desde un altura H
#  y en cada revote sube el 10% menos de la anterior hacer el diagrama flujo y
#  el programa en python, que lea H y que calcule e imprima en cual
#  revote la pelota no alcanza a subir la quinta parte de la altura inicial.

print ("-----------------------")
print ("----------Revote-------")
print ("-----------------------")

h = int(input("Ingrese la altura de la pelota: "))

rebotes = 0
quinta = (h / 5)

while h >= quinta:
    h = h - (h * 0.10)
    rebotes += 1
    print("La altura " + str(round(h, 1)) + " se alcanza en el rebote " + str(rebotes))
  
print("El número de rebotes necesarios para que la altura sea menor que la quinta parte de la altura es de " + str(rebotes) + " rebotes.")