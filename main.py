#!/usr/bin/python

# -------------------------------------------------------------------------------------
# ---------------------------- Libraries ----------------------------------------------
# -------------------------------------------------------------------------------------

import os
import collections
from optparse import OptionParser

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
	new_matrix = []
	#for line in matrix:
	one_position = []
	zero_position = []
	for i in range(len(matrix[0])):
		#print (i,matrix[0][i])
		if matrix[0][i]==1:
			one_position.append(i)
		else:
			zero_position.append(i)
	return one_position ,zero_position

def mascara(matrix):
	mascara = []
	for x in range(len(matrix)):
		elements_in_line=collections.Counter(matrix[x][0:-1])
		if(elements_in_line[1]==1):
			mascara.append(x)
	return mascara

def excluyente(matrix):
	fastidia_columnas = 0
	num_columnas_uno = 0
	mismo_cero = True
	fastidia = False
	mascara = {}
	mascara_add = []
	if len(matrix[0])==1:
		return False
	for x in range(len(matrix)):
		elements_in_line=collections.Counter(matrix[x][0:-1])
		test = list(enumerate(matrix[x][0:-1]))
		test = list(filter(lambda x: x[1] == 1, test))
		#print("-",test)
		if(len(test)==1):
			for t in test:
				if mascara.get(t[0], False):
					mascara[t[0]].append(x)
				else:
					mascara[t[0]] = [x]
		#print(matrix[x][-1])
		if matrix[x][-1]==1:
			mascara_add.append(x)
		# Mismo numero de renglones en 0
		if elements_in_line[0] == len(matrix[x][0:-1]) and matrix[x][-1] == 1:
			mismo_cero = False

	# Fastidia el unico renglon tipico de alguna columna anterior
	#print(mascara,mascara_add)
	for m in mascara:
		#print(m,mascara[m])
		if set(mascara[m]) <= set(mascara_add):
			#print("SI")
			fastidia = True

	#if(num_columnas_uno==fastidia_columnas):
	#	fastidia = True
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
	matrix_order = order_matrix(matrix)

	queue =  [[x] for x in matrix_order[0]]
	matrix_order = matrix_order[0] + matrix_order[1]
	psi_star = []
	column_num = len(matrix[0])
	hits = 0

	while(queue):
	#for x in range(0, 12):
		hits += 1
		queue_aux = queue[:]
		elements = queue.pop(0)
		aux_matrix = sub_matrix(matrix,elements)
		if(testor(aux_matrix) and tipico(aux_matrix)):
			action = "Es Testor y típico"
			psi_star.append(elements)
			aux_hits = len(queue)
			queue = superset_delete(queue,elements)
			aux_hits -= len(queue)
			hits += aux_hits
		elif(excluyente(aux_matrix)):
			action = "Es excluyente"
			aux_hits = len(queue)
			queue = superset_delete(queue,elements)
			aux_hits -= len(queue)
			hits += aux_hits
		else:
			action = "Es candidato"
			new_elements = []
			for x in range(matrix_order.index(elements[-1])+1,column_num):
				new_elements.append(elements+[matrix_order[x]])
			queue = push_queue(queue,new_elements)
		if(print_steps==True):
			print("Paso:",hits,"\nPila inicial:",queue_aux,"\nElemento:",elements)
			print_matrix(sub_matrix(matrix,elements))
			print("Acción:",action,"\nPila final",queue,"\n\n")
	print("\nTestores Típicos:")
	for testor_print in psi_star:
		print(sorted(testor_print))
		#print_matrix(sub_matrix(matrix,testor_print))
	print("Número:",len(psi_star))
	print("Hits:",hits)
	#print_matrix(psi_star)


# -------------------------------------------------------------------------------------
# ---------------------------- Code ---------------------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == '__main__':
	# limpiado de consola
	os.system('clear')

	print("Algoritmo BR")
	matrix = {

	"articulo_br" : [[1,0,0,0,0,0,0,1,0],
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
                      dest='matrix',
                      choices=['articulo_br','identidad_basica','n2', 's'],
                      default='articulo_br',
                      help="Selecciona la matriz a analizar: articulo_br,identidad_basica,n2,s")

	(options, args) = parser.parse_args()

	#excluyente
	"""sub_matrix_ = sub_matrix(matrix_1,[0,7,4])
	print_matrix(sub_matrix_)
	print(excluyente(sub_matrix_))"""

	"""sub_matrix_ = sub_matrix(matrix_1,[0,2,4])
	print_matrix(sub_matrix_)

	print(excluyente(sub_matrix_))"""

	if options.imprimir_pasos=='Y':
		br_algorithm(matrix[options.matrix],True)
	else:
		br_algorithm(matrix[options.matrix])

"""
    Testores tipícos: 14
    	[5,7,8]
    	[4,7,5]
    	[1,7,8]
    	[1,7,4]
    	[0,1,2,6]
    	[0,1,2,3]
    	[0,1,6,7]
    	[0,1,3,7]
    	[0,5,8]
    	[0,4,8]
    	[0,2,5]
    	[0,1,8]
    	[0,1,4]
    	[0,5,7]
	Contador de hits: sacar de la pila -> 92
	tamaño maximo de la lista pila
	cantidad de memoria
"""
