import funciones_parcial2
#Creamos y llamamos a la funcion (llenarMatriz) para llenar la matriz con los valores validos 
while True:
    dna = funciones_parcial2.llenarMatriz()
    print (dna)
    if funciones_parcial2.is_mutant(dna):
        print("Usted es mutante")
    else:
        print("Usted es humano")
#Aca le preguntamos al usuario si quiere seguir jugando
    op = int(input("Si desea continuar presione 1, de lo contrario 2: "))
    if op == 1:
        continue
    else:
        break
#Nos despedimos del usuario
print("Gracias por jugar. Hasta luego")
