#!/usr/bin/python

# -------------------------------------------------------------------------------------
# ---------------------------- Libraries ----------------------------------------------
# -------------------------------------------------------------------------------------

import os
import collections

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
	mask = matrix[0]
	for x in range(len(matrix)-1):
		mask = [x + y for x, y in zip(mask, matrix[x+1])]
	#print (mask)
	if collections.Counter(mask)[0] != 0:
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

def excluyente(matrix):
	fastidia = False
	if len(matrix[0])==1:
		return False
	for x in range(len(matrix)):
		elements_in_line=collections.Counter(matrix[x][0:-1])
		# Mismo numero de renglones en 0	
		if elements_in_line[0] == len(matrix[x][0:-1]) and matrix[x][-1] == 1:
			return False
		# Fastidia el unico renglon tipico de alguna columna anterior
		if elements_in_line[1] == 1 and matrix[x][-1] == 1:
			fastidia = True
	if not fastidia:
		return False
	return True

def print_matrix(matrix):
	for line in matrix:
		print (line)
	print("\n")

def sub_matrix(matrix,list_columns):
	sub_matrix = []
	for line in matrix:
		sub_matrix.append([y for x,y in enumerate(line) if x in list_columns]) 
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

def br_algorithm(matrix):
	print("Matriz de entrada:")	
	print_matrix(matrix)
	matrix_order = order_matrix(matrix)

	queue =  [[x] for x in matrix_order[0]]
	matrix_order = matrix_order[0] + matrix_order[1]
	psi_star = []

	while(queue):
		elements = queue.pop(0)
		aux_matrix = sub_matrix(matrix,elements)
		#print_matrix(aux_matrix)
		if(testor(aux_matrix) and tipico(aux_matrix)):
			psi_star.append(elements)
			queue = superset_delete(queue,elements)
		elif(excluyente(aux_matrix)):
			queue = superset_delete(queue,elements)
		else:
			new_elements = []
			for x in range(len(matrix[0])):
				if(x not in elements):
					new_elements.append(elements+[x])
			queue = push_queue(queue,new_elements)
			#print(queue)
	print("Testores Típics:")	
	print_matrix(psi_star)


# -------------------------------------------------------------------------------------
# ---------------------------- Code ---------------------------------------------------
# -------------------------------------------------------------------------------------

if __name__ == '__main__':
	# limpiado de consola
	os.system('clear')
	print("Algoritmo BR")

	matrix_1 = [[1,0,0,0,0,0,0,1,0],
				[0,1,0,0,0,1,0,0,0],
				[0,0,0,1,1,1,1,0,1],
				[0,0,1,0,1,0,0,1,1],
				[1,0,1,0,1,0,0,0,1]]

	matrix_2 = [[0,0,0,1],
				[1,0,0,0],
				[0,0,1,0],
				[0,1,0,0]]

	br_algorithm(matrix_2)
	

