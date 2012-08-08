import os
from util import *
from matrix import *

matrix_input = []
fobj = open("source.csv", "r")
for line in fobj:
	s = Util.replace_string(line)
	matrix_input.append(s.split(";"))
fobj.close()

matrix = Matrix(matrix_input)

#Hilfsfunktionen zum testen
print("Matrix:")
print(matrix)
print("Zeilen 1 der Matrix:")
print(matrix.get_row(0))
print("Spalten 1 der Matrix:")
print(matrix.get_col(0))
print("Anzahl Zeilen der Matrix:")
print(matrix.get_row_count())
print("Anzahl Spalten der Matrix:")
print(matrix.get_col_count())
print("Determinate der Matrix:")
print(Util.det(matrix.get_values()))


