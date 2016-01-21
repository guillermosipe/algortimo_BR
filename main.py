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
	column_num = len(matrix[0])

	while(queue):
	#for x in range(0, 3):
		elements = queue.pop(0)
		aux_matrix = sub_matrix(matrix,elements)
		queue_aux = queue[:]
		action = ""
		#print_matrix(aux_matrix)
		if(testor(aux_matrix) and tipico(aux_matrix)):
			psi_star.append(elements)
			queue = superset_delete(queue,elements)
			action = "testor y tipico"
		elif(excluyente(aux_matrix)):
			action = "excluyente"
			queue = superset_delete(queue,elements)
		else:
			action = "fuera"
			new_elements = []
			#for x in range(max(elements),column_num):
			for x in range(matrix_order.index(max(elements)),column_num):
				if(x not in elements):
					new_elements.append(elements+[x])
			queue = push_queue(queue,new_elements)
		#print(elements,"\n",action,"\n",queue_aux,"\n",queue,"\n\n")
	print("Testores Típicos:")	
	for testor_print in psi_star:
		print(sorted(testor_print),"\n")
		print_matrix(sub_matrix(matrix,testor_print))
	print("Número: ",len(psi_star))
	#print_matrix(psi_star)


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