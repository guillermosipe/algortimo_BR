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
	print (mask)
	if collections.Counter(mask)[0] != 0:
		return False
	return True

def order_matrix(matrix):
	new_matrix = []
	#for line in matrix:
	one_position = []
	for i in range(len(matrix[0])):
		#print (i,matrix[0][i])
		if matrix[0][i]==1:
			one_position.append(i)
	for line in range(len(matrix)):
		aux_line = []
		for new_order in one_position:
			aux_line.append(matrix[line][new_order])
		for x in range(len(matrix[line])):
			if x not in one_position:
				aux_line.append(matrix[line][x])
		matrix[line] = aux_line

	return matrix

def excluyente(matrix):
	fastidia = False
	if len(matrix[0])==1:
		return False
	for x in range(len(matrix)):
		elements_in_line=collections.Counter(matrix[x][0:-1])
		# Mismo número de renglones en 0	
		if elements_in_line[0] == len(matrix[x][0:-1]) and matrix[x][-1] == 1:
			return False
		# Fastidia el único renglón típico de alguna columna anterior
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

def br_algorithm(matrix):
	
	#print_matrix(matrix)
	matrix = order_matrix(matrix)
	#print_matrix(matrix)

	queue =  [[i] for i,x in enumerate(matrix[0]) if x == 1]
	psi_star = []

	#while(queue):
	elements = queue.pop(0)
	aux_matrix = sub_matrix(matrix,elements)
	#print_matrix(aux_matrix)
	if(testor(aux_matrix) and tipico(aux_matrix)):
		psi_star.append(elements)
		# eliminar subconjuntos
	#elif(excluyente(aux_matrix)):
		# eliminar subconjuntos
	else:
		new_elements = []
		for x in range(len(matrix[0])):
			if(x not in elements):
				new_elements.append(elements+[x])
		
		queue = push_queue(queue,new_elements)
		print(queue)



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

	br_algorithm(matrix_1)

	#print(push_queue([[0],[1]],[[2,3],[4,5]]))
	#print(push_queue([[2, 3], [4, 5], [0], [1]],[[1,8,2],[1,8,3]]))

	"""matrix_1 = order_matrix(matrix_1)
	matrix_2 = order_matrix(matrix_2)

	for line in matrix_1:
		print (line)
	print("\n")
	
	for line in matrix_2:
		print (line)
	print("\n")


	matrix_1_excluyente = [ [1,0,0,0,0],
							[0,1,0,0,0],
							[0,0,0,1,1],
							[0,0,1,0,1],
							[1,0,1,0,1]]

	matrix_2_excluyente = [ [0,0,0,0],
							[1,0,0,0],
							[0,0,1,1],
							[0,1,0,1],
							[0,1,0,1]]

	matrix_3_excluyente = [[1],[0],[0],[0],[1]]

	matrix_4_excluyente = [[1,1],[0,0],[0,0],[0,1],[1,0]]

	print(excluyente(matrix_4_excluyente))

	matrix_1_testor = [ [1,0,0,0],
						[0,1,0,0],
						[0,0,0,1],
						[0,0,1,0],
						[1,0,1,0]]

	print(testor(matrix_1_testor))
	print(tipico(matrix_1_testor))"""

