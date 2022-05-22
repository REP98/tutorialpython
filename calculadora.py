#!/usr/bin/python3.10
# -*- coding: UTF-8 -*-
# Calculadora básica
# Author Robert Pérez
# Tutorial Python en https://vzlaweb.blogspot.com

import sys

def helps():
    print("""\
 Por: Robert Pérez
 Para Tutoriales Python en VEB
 uso:
    ./calculadora.py [-s|r|mx|d] [--withfloat] num1 num2
 Opciones:
    -s indica suma
    -r indica resta
    -mx indica multiplicar
    -d indica dividir
    --withfloat indica si se muetra decimales de la división
 -------------------------
 Ejemplo:
    ./calculadora.py -s 2 4
    imprimira 6
 -------------------------
 Link del tutorial: https://vzlaweb.blogspot.com
    """)


print("Calculadora Básica Python")

if sys.argv[1] == "-s":
    suma = int(sys.argv[2]) + int(sys.argv[3])
    print(sys.argv[2] + " + " + sys.argv[3] + " = " + str(suma))
elif sys.argv[1] == "-r":
    resta = int(sys.argv[2]) - int(sys.argv[3])
    print(sys.argv[2] + " - " + sys.argv[3] + " = " + str(resta))
elif sys.argv[1] == "-mx":
    multi = int(sys.argv[2]) * int(sys.argv[3])
    print(sys.argv[2] + " * " + sys.argv[3] + " = " + str(multi))
elif sys.argv[1] == "-d":
    if len(sys.argv) > 4:
        div = int(sys.argv[2]) / int(sys.argv[3])
        print(sys.argv[2] + " / " + sys.argv[3] + " = " + str(div))
    else:
        div = int(sys.argv[2]) // int(sys.argv[3])
        print(sys.argv[2] + " // " + sys.argv[3] + " = " + str(div))
elif sys.argv[1] == "-h":
    helps()
else:
    print("Debe indicar un parametro de operación\n -------------------------")
    helps()
