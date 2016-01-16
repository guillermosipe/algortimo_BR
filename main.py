#!/usr/bin/python

# -------------------------------------------------------------------------------------
# ---------------------------- Libraries ----------------------------------------------
# -------------------------------------------------------------------------------------

import os

# -------------------------------------------------------------------------------------
# ---------------------------- Functions ----------------------------------------------
# -------------------------------------------------------------------------------------

def order_matrix(matrix):
	new_matrix = []
	#for line in matrix:
	one_position = []
	for i in range(len(matrix[0])):
		#print (i,matrix[0][i])
		if matrix[0][i]==1:
			one_position.append(i)
	print (one_position)
	for line in range(len(matrix)):
		aux_line = []
		for new_order in one_position:
			aux_line.append(matrix[line][new_order])
		for x in range(len(matrix[line])):
			if x not in one_position:
				aux_line.append(matrix[line][x])
		matrix[line] = aux_line

	return matrix

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

