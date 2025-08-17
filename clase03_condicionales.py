#Objetivo: Crear un programa que determine si un usuario es mayor de edad.
#Requisitos:
#Pregúntale al usuario su edad usando input().
#Convierte la edad a un número entero (int).
#Usa una estructura if/else para determinar si la edad es mayor o igual a 18.
#Si es mayor o igual a 18, muestra el mensaje: "Eres mayor de edad, ya puedes pasar."
#Si es menor de 18, muestra el mensaje: "Eres menor de edad, no puedes pasar."
"""
user = input("Please, enter your name ")
print("Name entered correctly")
age_tex = input("Please, enter your age")
print("Age entered correctly")
age = int(age_tex)
adult = 18
if age >= adult:
    print("the user: ",user," Can pass")
else:
    print("the user: ",user," Can not pass")
 """

"""Objetivo: Crear un programa que pida un número al usuario y le diga si es positivo, negativo o cero.
Requisitos:
Pide al usuario que ingrese un número cualquiera usando input().
Convierte la entrada a un número entero (int).
Usa una estructura if-elif-else para determinar la naturaleza del número:
Si el número es mayor que 0, muestra el mensaje: "El número es positivo."
Si el número es menor que 0, muestra el mensaje: "El número es negativo."
Si no es ninguna de las anteriores (es decir, si es cero), muestra el mensaje: "El número es cero."""

print("The objective is to analyze whether a number is positive, negative or cero")
number_text = input("Please, enter a number:    ")
number = int(number_text)
print("Number entered correctly")
if number > 0:
    print("The number: ",number," is positive")
elif number < 0:
    print("The number: ",number," is negative")
else:
    print("The number: ",number," is cero")



