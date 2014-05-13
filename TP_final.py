#1er TP de Algoritmos Geneticos

#bloque de definicion de constantes
coef = pow(2, 30) - 1  #mi rango de decimales es [0, 2^30 - 1]
crossoverProb = 0.75
mutationProb = 0.05

#bloque de importacion de modulos
import random


#bloque de definicion de funciones
def funcionObjetivo(cInt):
    return pow(cInt/float(coef), 2)

def funcionFitness(valor, suma):
    fitness = (valor/float(suma))
    return fitness

def promedio(valor):
    return (valor/10.0)

def ruleta(fitness):
    porcentaje = (fitness*100)
    return porcentaje

def crossover(cromosoma1, cromosoma2, corte):
    genes1 = genList[cromosoma1]
    genes2 = genList[cromosoma2]
    
    hijo =  genes1[:corte] + genes2[corte:]
    
    return hijo

#bloque del programa principal

cromosomaList = [] #lista de los valores de c/cromosoma (int)
genList = [] #lista de los genes de c/cromosoma (binario)
objectiveList = [] #resultados de la funcion objetivo evaluada en los cromosomas enteros
fitnessList = [] #resultados de la funcion fitness para c/cromosoma
ruletaList = []
porcentajeList = [] #guardo los porcentajes del fitness de c/cromosoma

sumaList = []
promedioList = []
maximoList = []	
resultadoList = [] #guardo la tabla historica de resultados

indice = 0

for m in range(10):
    cromosoma = random.randint(0, coef)  #genero un int random 
    cromosomaList.append(cromosoma)
  


for i in range(19):
    #tambien puedo usar del list[:], da igual
    genList = []
    objectiveList = []
    fitnessList = []
    ruletaList = [] 
    hijosList = []
    cromosomaListNew = []
    porcentajeList = []
    lista = []
    # zip() creo pares a partir de elementos de una lista
    totalObjetivo = 0
    indice = 0 #para guardar la posicion del cromosoma en la lista
    
    for j in range(10):
            
        cromosoma = int(cromosomaList[j])
        cromosomaBin = bin(cromosoma)[2:].zfill(30) #paso el int a binario
        genList.append(cromosomaBin)
   	
        resultadoObjetivo = funcionObjetivo(cromosoma) #evaluo la funcion en el int
        objectiveList.append(resultadoObjetivo)
   	
   	
    totalObjetivo = sum(objectiveList) #sumo toda la lista de resultados de la funcion
        
    for var in range(10):
            
        resultadoObjetivo = objectiveList[var]
            
        resultadoFitness = funcionFitness(resultadoObjetivo, totalObjetivo)
        fitnessList.append(resultadoFitness)
        
        porcentaje = ruleta(resultadoFitness)#le asigno un valor porcentual en la ruleta
        porcentajeList.append(porcentaje) #lista que guarda porcentajes de fitness p/c cromosoma
        if (porcentaje < 0.5):
            porcentaje = 1
        porcentaje = int(round(porcentaje))	
    
        for k in range(porcentaje): #voy del ultimo valor hasta el porcentaje de este cromosoma
            ruletaList.append(indice) #agrego el mismo cromosoma hasta que termine el for
 			
        indice = indice + 1 #cuando terminan las 10 iteraciones la ruleta queda cargada
    
    for l in range(5):#hago 5 loops porque son 5 pares
        azarRuleta1 = random.randint(0, 99)
        cromosomaAzar1 = ruletaList[azarRuleta1] #elijo el primer valor del par
    
        azarRuleta2 = random.randint(0, 99)
        cromosomaAzar2 = ruletaList[azarRuleta2] #elijo el 2do valor del par
    
        crossoverRandom = random.random() #tiro un random para ver el crossover
    
        if crossoverRandom<=crossoverProb: #si el crossover da si:
            corteRandom = random.randint(0, 29)
    
   	    hijo1 = crossover(cromosomaAzar1, cromosomaAzar2, corteRandom) #pongo los genes hasta el corteRandom
   	    hijo2 = crossover(cromosomaAzar2, cromosomaAzar1, corteRandom)
    
        else:
            hijo1 = genList[cromosomaAzar1]
            hijo2 = genList[cromosomaAzar2]
    
        mutationRandom1 = random.random
        mutationRandom2 = random.random
    
        if mutationRandom1 <= mutationProb:  #pruebo si muta y cambio el valor
            genChange = random.randint(0, 29)
    
       	    if (hijo1[genChange] == 0):
                hijo1[genChange] = 1
       	    else:
       	        hijo1[genChange] = 0
       	else:
       	    hijo1 = int(genList[cromosomaAzar1])
            
        if mutationRandom2 <= mutationProb:
            genChange = random.randint(0, 29)
    
   	    if (hijo2[genChange] == 0):
                hijo2[genChange] = 1
   	    else:
   	        hijo2[genChange] = 0
   	else:
   	    hijo2 =  int(genList[cromosomaAzar2])
    
        cromosomaListNew.append(hijo1) #guardo los cromosomas nuevos en otra lista
        cromosomaListNew.append(hijo2)
   	
    
    cromosomaList = cromosomaListNew #reemplazo la lista original con los hijos
        
    
    promedioObjetivo = promedio(totalObjetivo)
    maximoObjetivo =  max(objectiveList)
    maximoFitness =  max(fitnessList)
    sumaObjetivo = totalObjetivo
   	
    
    lista = ['SUMA Objetivo: ' + str(sumaObjetivo), 'SUMA Fitness: 1', 'PROMEDIO Objetivo: ' + str(promedioObjetivo), 'PROMEDIO Fitness: 0.25', 'MAXIMO Objetivo: ' + str(maximoObjetivo), 'MAXIMO Fitness: ' + str(maximoFitness)]
    
    resultadoList.append(lista)
        
print resultadoList
