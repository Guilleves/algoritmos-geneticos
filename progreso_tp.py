#!/bin/env python3.0

#1er TP de Algoritmos Geneticos
#
#
#bloque de definicion de constantes
coef = pow(2, 30) - 1  #mi rango de decimales es [0, 2^30 - 1]
crossoverProb = 0.75
mutationProb = 0.05
#
#
#bloque de importacion de modulos
import random
#
#
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

def crossover(cromosoma1, cromosoma2, corte):
	hijo = genList[cromosma1][:corte] + genList[cromosoma2][corte:]
	return hijo

#bloque del programa principal

cromosomaList = [] #lista de los valores de c/cromosoma (int)
genList = [] #lista de los genes de c/cromosoma (binario)
objectiveList = [] #resultados de la funcion objetivo evaluada en los cromosomas enteros
fitnessList = [] #resultados de la funcion fitness para c/cromosoma
ruletaList = []

sumaList = []
promedioList = []
maximoList = []	

indice = 0

for i in xrange(20):

	cromosomaList = [] #tambien puedo usar del list[:], da igual
	genList = []
	objectiveList = []
	fitnessList = []
	ruletaList = [] 
	# zip() creo pares a partir de elementos de una lista
	totalObjetivo = 0
	indice = 0


	for j in xrange(10):
		cromosoma = random.randint(0, coef)  #genero un int random 
		cromosomaList.append(cromosoma)

		cromosomaBin = bin(cromosoma)[2:] #paso el int a binario
		genList.append(cromosomaBin)

		resultadoObjetivo = funcionObjetivo(cromosoma) #evaluo la funcion en el int
		objectiveList.append(resultadoObjetivo)

	totalObjetivo = sum(objectiveList) #sumo toda la lista de resultados de la funcion

	for objective in objectiveList:
		resultadoFitness = funcionFitness(objective, totalObjetivo)
		fitnessList.append(resultadoFitness)
		porcentaje = ruleta(resultadoFitness)#le asigno un valor porcentual en la ruleta
		porcentajeList.append(porcentaje)
			
			for k in xrange(porcentaje):#voy cargando valores en un array de 100
				ruletaList.append(indice)
		indice++ #cuando terminan las 10 iteraciones la ruleta queda cargada

	for l in xrange(5):
		azarRuleta1 = random.randint(0, 99)
		cromosomaAzar1 = cromosomaBin[azarRuleta1] #elijo el primer valor del par

		azarRuleta2 = random.randint(0, 99)
		cromosomaAzar2 = cromosomaBin[azarRuleta2] #elijo el 2do valor del par

		crossoverRandom = random.random() #tiro un random para ver el crossover

		if crossoverRandom<=crossoverProb: #si el crossover da si:
			corteRandom = random.randint(0, 29)

			hijo1 = crossover(cromosomaAzar1, cromosomaAzar2, corteRandom) #pongo los genes hasta el corteRandom
			hijo2 = crossover(cromosomaAzar2, cromosomaAzar1, corteRandom)

			hijosList.append(hijo1) #creo una lista con elementos hijos de los cromosomas
			hijosList.append(hijo2)
		else:
			hijo1 = cromosomaAzar1
			hijo2 = cromosomaAzar2

GITHU      	mutationRandom2 = random.random

		if mutationRandom1 <= mutationProb:  #pruebo si muta y cambio el valor
			genChange = random.randit(0, 29)

			if hijo1[genChange] = 0:
				hijo1[genChange] = 1
			else:
				hijo1[genChange] = 0
        
        if mutationRandom2 <= mutationProb:
			genChange = random.randit(0, 29)

			if hijo2[genChange] = 0:
				hijo2[genChange] = 1
			else:
				hijo2[genChange] = 0


