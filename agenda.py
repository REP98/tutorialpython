#!/usr/bin/python3.10
# -*- coding: UTF-8 -*-
# List
Cubes = [1, 8, 27, 64, 125, 0]
Cubes[5] = 6 ** 3 # Modificamos el 0
OtherCubes = [343, 512]
Cubes = Cubes + OtherCubes # Concatenamos listas
Cubes.append(9 ** 3) # Añadimos al final
print(Cubes) # imprime [1, 8, 27, 64, 125, 343, 512, 729]
segment = Cubes[2:5]
print(segment)
hex = [0, 1, 2, 3, 4, 5, 6, 7, ,8, 9, 'a', 'b', 'c', 'd', 'e', 'f']
hex[10:] = ['A', 'B', 'C', 'D', 'E', 'F'] # transformamos la letras a mayusculas
