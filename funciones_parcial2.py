def llenarMatriz():
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

#verificacion para los caracteres ingresados
def caracter_mat(chain):
    for i in range (len(chain)):
        if chain[i] != "a" and chain[i] != "c" and chain[i] != "g" and chain[i] !="t": 
            return False
    return True  

#verificacion de largo de la lista
def large_mat(chain):
    if (len(chain)!=6):
        return False
    else:
        return True  

                

# verificacion horizontal
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
            if (coincidencesH == 3):
                mutant = mutant +1
            else:
                pass    
    
    #verificacion vertical    
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
            if (coincidences == 3):
                mutant = mutant +1
            else:
                pass
    

    mutante = ["aaaa", "cccc", "gggg", "tttt"]
    #verificacion diagonal desde la esquina superior izquierda a inferior derecha
    for i in range (6):
        for j in range (6):
            if (dna[i][j] == mutante and dna[i+1][j+1] == mutante and dna[i+2][j+2] == mutante and dna[i+3][j+3] == mutante):
                mutant = mutant+1
    
    #verificacion diagonal desde la esquina superior derecha a inferior izquierda
    for i in range (6):
        for j in range (6):
            if (dna[i][j] == mutante and dna[i-1][j+1] == mutante and dna[i-2][j+2] == mutante and dna[i-3][j+3] == mutante):
                mutant = mutant+1

    if mutant>1:
        return True
    else:
        return False
