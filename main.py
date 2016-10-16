#!/usr/bin/python

#Algoritmo BR
#Desarrollador por: Silva Peña Guillermo
#Descripcion: Implementación en Python del algoritmo BR

# -------------------------------------------------------------------------------------
# ---------------------------- Libraries ----------------------------------------------
# -------------------------------------------------------------------------------------

import os
import collections
from optparse import OptionParser
import json

# -------------------------------------------------------------------------------------
# ---------------------------- Functions ----------------------------------------------
# -------------------------------------------------------------------------------------

def testor(matrix):
	for x in range(len(matrix)):
		elements_in_line = collections.Counter(matrix[x])
		if elements_in_line[1] == 0:
			return False
	return True

def tipico(matrix):
	one_position = []
	for line in matrix:
		line_one = [x for x,y in enumerate(line) if y==1]
		if len(line_one)==1 and line_one[0] not in one_position:
				one_position.append(line_one[0])
	if(len(one_position)!=len(matrix[0])):
		return False
	return True

def order_matrix(matrix):
	matrix_aux = []
	x = [0,len(matrix[0])]
	for line_pos in range(len(matrix)):
		line_one = len(list(filter(lambda one:one==1,matrix[line_pos])))
		if(x[1] > line_one):
			x = [line_pos,line_one]
	matrix_aux = matrix.pop(x[0])
	matrix.insert(0,matrix_aux)
	return matrix

def getKey(element):
	return element[1]

def ones_and_zeros(matrix):
	one_position = []
	zero_position = []
	for i in range(len(matrix[0])):
		if matrix[0][i]==1:
			one_position.append(i)
		else:
			zero_position.append(i)
	return one_position ,zero_position

def excluyente(matrix):
	mismo_cero = True
	fastidia = False
	mascara = {}
	mascara_add = []
	if len(matrix[0])==1:
		return False
	for x in range(len(matrix)):
		elements_in_line=collections.Counter(matrix[x][0:-1])
		if elements_in_line[1]== 1:
			pos_one = matrix[x][0:-1].index(1)
			if mascara.get(pos_one, False):
				mascara[pos_one].append(x)
			else:
				mascara[pos_one] = [x]
		if matrix[x][-1]==1:
			mascara_add.append(x)
		# Mismo numero de renglones en 0
		if elements_in_line[0] == len(matrix[x][0:-1]) and matrix[x][-1] == 1:
			mismo_cero = False
	# Fastidia el unico renglon tipico de alguna columna anterior
	for m in mascara:
		if set(mascara[m]) <= set(mascara_add):
			fastidia = True
	return fastidia or mismo_cero

def print_matrix(matrix):
	for line in matrix:
		print ("\t",line)

def sub_matrix(matrix,list_columns):
	sub_matrix = []
	for line in matrix:
		aux = []
		for x in list_columns:
			aux.append(line[x])
		sub_matrix.append(aux)
	return sub_matrix

def push_queue(queue,new_elements):
	queue_aux = (list(enumerate(queue)))
	#print (queue_aux)
	queue_aux = list(filter(lambda x: len(x[1]) == 1, queue_aux))
	#print (queue_aux)
	if(queue_aux):
		position = queue_aux[0][0]
		return queue[:position] + new_elements + queue[position:]
	else:
		return queue + new_elements

def superset_delete(queue,element):
	return [x for x in queue if not set(x)>=set(element)]

def br_algorithm(matrix,print_steps=False):
	print("Matriz de entrada:")
	print_matrix(matrix)
	matrix = order_matrix(matrix)
	matrix_order = ones_and_zeros(matrix)
	queue =  [[x] for x in matrix_order[0]]
	matrix_order = matrix_order[0] + matrix_order[1]
	psi_star = []
	column_num = len(matrix[0])
	hits = 0
	steps = 0
	while(queue):
		steps += 1
		hits += 1
		queue_aux = queue[:]
		elements = queue.pop(0)
		aux_matrix = sub_matrix(matrix,elements)
		if(testor(aux_matrix) and tipico(aux_matrix)):
			action = "Es Testor y típico"
			psi_star.append(elements)
			queue = superset_delete(queue,elements)
			hits += len(queue_aux) - len(queue) -1
		elif(excluyente(aux_matrix)):
			action = "Es excluyente"
			queue = superset_delete(queue,elements)
			hits += len(queue_aux) - len(queue) -1
		else:
			action = "Es candidato"
			new_elements = []
			for x in range(matrix_order.index(elements[-1])+1,column_num):
				new_elements.append(elements+[matrix_order[x]])
			queue = push_queue(queue,new_elements)
		if(print_steps==True):
			print("Paso:",steps,"\nPila inicial:",queue_aux,"\nElemento:",elements)
			print_matrix(sub_matrix(matrix,elements))
			print("Acción:",action,"\nPila final",queue,"\n\n")
	print("\nTestores Típicos:")
	for testor_print in psi_star:
		print(sorted(testor_print))
		if(print_steps==True):
			print_matrix(sub_matrix(matrix,testor_print))
	print("Número:",len(psi_star))
	print("Hits:",hits)
	return


# -------------------------------------------------------------------------------------
# ---------------------------- Code ---------------------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == '__main__':
	# limpiado de consola
	os.system('clear')

	print("Algoritmo BR")
	matrix = {

	"articulo_br" : [
				[1,0,0,0,0,0,0,1,0],
				[0,1,0,0,0,1,0,0,0],
				[0,0,0,1,1,1,1,0,1],
				[0,0,1,0,1,0,0,1,1],
				[1,0,0,0,1,0,0,0,1]],
	# hits: 92

	"n2" : [[1,1,1,0,0],
				[1,1,0,0,1],
				[1,0,1,1,0],
				[1,0,1,0,1]],
	# hits: 9

	"s" : [[1,0,0,0,1,0],
				[1,1,0,0,0,1],
				[0,0,1,0,0,1],
				[1,0,0,1,0,1]],

	# hits: 21

	# cavvadias y stravopolous pagina: trasnversales minimales 1-0 | 0-*

	"identidad_basica" : [[0,0,0,1],
				[1,0,0,0],
				[0,0,1,0],
				[0,1,0,0]]
	}

	parser = OptionParser(usage="usage: %prog [options] arg1")
	parser.add_option("-i", "--imprimir_pasos",
                      type='choice',
                      action='store',
                      dest='imprimir_pasos',
                      choices=['Y', 'N'],
                      default='N',
                      help="Muestra los pasos del Algoritmo BR: Y(si), N(no)")

	parser.add_option("-m", "--matriz",
                      type='choice',
                      action='store',
                      dest='matriz',
                      choices=['articulo_br','identidad_basica','n2', 's'],
                      default='articulo_br',
                      help="Selecciona la matriz a analizar: articulo_br,identidad_basica,n2,s")

	parser.add_option("-f", "--file",
                      dest='archivo_matriz',
					  default = False,
                      help="Inserta una matriz desde un archivo")

	(options, args) = parser.parse_args()

	if(options.archivo_matriz):
		with open(options.archivo_matriz,'r') as json_file:
			archivo_matriz = json.load(json_file)
		matriz_seleccionada = archivo_matriz["matrix"]
	else:
		matriz_seleccionada = matrix[options.matriz]

	if options.imprimir_pasos=='Y':
		br_algorithm(matriz_seleccionada,True)
	else:
		br_algorithm(matriz_seleccionada)
