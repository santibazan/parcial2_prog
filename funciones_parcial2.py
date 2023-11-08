#Creamos la matriz 
def fillMatriz():
    dna = []
    counter = 0
    while  counter < 6:
        chain = input(f"Ingrese el adn: ").lower()
        if caracter_mat(chain):
            if large_mat(chain):
                dna.append(chain)
                counter = counter + 1
            else:
                print(F"Largo invalido, recuerda que tiene que ser de 6 espacios")

        else:
            print (F"Caracteres invalidos, recuerda que solo se utilizan las letras a, c, g, t")
    return dna        

# Aqui hacemos la verificacion para que los caracteres ingresados sean validos
def caracter_mat(chain):
    for i in range (len(chain)):
        if chain[i] != "a" and chain[i] != "c" and chain[i] != "g" and chain[i] !="t": 
            return False
    return True  

#Aqui hacemos la verificacion para que el largo de la lista sea correcto
def large_mat(chain):
    if (len(chain)!=6):
        return False
    else:
        return True  

                

# En esta parte estamos verificando si en las filas hay alguna secuencia mutante
def is_mutant(dna):
    mutant = 0
    for i in range(6):
        for j in range (3):
            coincidencesH = 0
            aux = j
            for k in range (3):
                if (dna[i][aux + 1 ]== dna[i][aux]):
                    coincidencesH += 1
                else:
                    pass
                aux += 1
#hacemos las respectivas validaciones y si el codigo encuentra una combinacion, se sumara a la variable mutant
            if (coincidencesH == 3):
                mutant = mutant +1
            else:
                pass    
    
    # Y en esta otra parte estamos verificando si en las columnas hay alguna secuencia mutante
    for i in range(6):
        for j in range (3):
            coincidences = 0
            aux = j
            for k in range (3):
                if (dna[aux +1][i]== dna [aux][i]):
                    coincidences = coincidences + 1
                else:
                    pass
                aux = aux + 1
#hacemos las respectivas validaciones y si el codigo encuentra una combinacion, se sumara a la variable mutant
            if (coincidences == 3):
                mutant = mutant +1
            else:
                pass
    

    mutante = ["aaaa", "cccc", "gggg", "tttt"]
    #Aca hacemos la verificacion para saber si hay alguna secuencia mutante en las diagonales desde la esquina superior izquierda a inferior derecha
    for i in range (6):
        for j in range (6):
            if (dna[i][j] == mutante and dna[i+1][j+1] == mutante and dna[i+2][j+2] == mutante and dna[i+3][j+3] == mutante):
                mutant = mutant+1
    
    #Aca hacemos la verificacion para saber si hay alguna secuencia mutante en las diagonales desde la esquina superior derecha a inferior izquierda
    for i in range (6):
        for j in range (6):
            if (dna[i][j] == mutante and dna[i-1][j+1] == mutante and dna[i-2][j+2] == mutante and dna[i-3][j+3] == mutante):
                mutant = mutant+1
#En este ultimo paso lo que hcaemos es retornar el valor mutant, si este llega a ser mas de 1, la secuencia es mutante, de lo contrario es humano
    if mutant>1:
        return True
    else:
        return False
