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

	matrix_1 = order_matrix(matrix_1)
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

