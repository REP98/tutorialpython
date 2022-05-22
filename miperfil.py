#!/usr/bin/python3.10
# -*- coding: UTF-8 -*-
# Tutorial Python
# Por: Robert Pérez

# la función input detiene el script a la espera de la interacción del usuario
name = input("Cual es tu primer nombre: ")
lastname = input("Cual es tu primer apellido: ")
sex = input("""
Indica tu sexo por la letra en mayuscula
F = Femenino
M = Masculino
O = Otros
:
""")

print("Pensando ....")
sexo = ""
if sex == "F":
    sexo = "Sra"
elif sex == "M":
    sexo = "Sr"
else:
    sexo = "Sr@"
print("Hola ",sexo)
print("Se llamas "+ name + " " + lastname )
print("Su nombre tiene " + str(len(name)) + " letras")
print("Su apellido tiene " + str(len(lastname)) + " letras")
print("Sus iniciales son: "+name[0] + "." + lastname[0])
print("Su nombre y apellido termina en: "+name[-1]+" y " + lastname[-1])

print("Quieres jugar con tu nombre")

ints = int(input("Ingresa un numero entre 0 y " + str(len(name) -1)+ ": "))
ends = int(input("Ingresa un número mayor que el anterior y menor que "+str(len(name) -1)+": "))
print("Resultado de tu nombre: ",name[ints:ends])
print("Adios ...")
           
