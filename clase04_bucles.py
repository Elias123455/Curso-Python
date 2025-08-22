#El bucle for es ideal para recorrer los elementos de una
# secuencia (como una lista de números o letras) y hacer algo con cada uno de ellos.
# Esto imprimirá los números del 0 al 4.
# range(5) genera la secuencia: 0, 1, 2, 3, 4
from clase03_condicionales import number_text

print("Inicio del bucle:")
for numero in range(5):
    print(f"Repetición número: {numero}")
print("Fin del bucle.")
######################################################################################
#En este ejemplo, la variable numero toma el valor de cada elemento
# de la secuencia range(5) en cada repetición (o "iteración") del bucle.

"""Ejercicio 4: La Tabla de Multiplicar ✖️
Objetivo: Crear un programa que le pida al usuario un número e imprima su tabla de multiplicar del 1 al 10.
Requisitos:
Pide al usuario que ingrese un número entero usando input(). No olvides convertirlo a int.
Usa un bucle for que se repita 10 veces. Te recomiendo usar range(1, 11) para generar los números del 1 al 10.
Dentro del bucle, en cada repetición, calcula el resultado de la multiplicación y muestra una línea de la tabla."""

print("Objetive is create a multiplication table with a selection number")
number_text = input("Please, enter a number: ")
number = int(number_text)
print("This is the table: ",number)
if number > 0:
#for (para cada) i(ingrediente) in (en la lista) range(1, 11) (de ingredientes del 1 al 10): (haz lo siguiente)
    for i in range(1,11):
        multiplicacion = number * i
        print(number,"*",i,"=",multiplicacion)
else:
    print("Cannot value number: 0")
