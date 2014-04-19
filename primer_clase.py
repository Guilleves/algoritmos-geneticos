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
import numpy
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

#bloque del programa principal

cromosomaList = [] #lista de los valores de c/cromosoma (int)
genList = [] #lista de los genes de c/cromosoma (binario)
objectiveList = [] #resultados de la funcion objetivo evaluada en los cromosomas enteros
fitnessList = [] #resultados de la funcion fitness para c/cromosoma

sumaList = []
promedioList = []
maximoList = []	

for i in range(20):

	cromosomaList = [] #tambien puedo usar del list[:], da igual
	genList = []
	objectiveList = []
	fitnessList = []
	# zip() creo pares a partir de elementos de una lista
	totalInt = 0

	for j in range(10):
		cromosoma = random.randint(0, coef)  #genero un int random 
		cromosomaList.append(cromosoma)

		cromosomaBin = bin(cromosoma)[2:] #paso el int a binario
		genList.append(cromosomaBin)

		resultadoObjetivo = funcionObjetivo(cromosoma) #evaluo la funcion en el int
		objectiveList.append(resultadoObjetivo)

	totalInt = sum(objectiveList) #sumo toda la lista de resultados de la funcion

	for objective in objectiveList:
		resultadoFitness = funcionFitness(objective, totalInt)
		fitnessList.append(resultadoFitness)

