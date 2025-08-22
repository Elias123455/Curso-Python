"""Lección 5: Bucles while (Repitiendo hasta que algo cambie)
El bucle while (mientras) ejecuta un bloque de código una y otra vez mientras una condición sea verdadera (True).
Piensa en él como un niño preguntando "¿Ya llegamos?". El viaje (el bucle) continúa mientras la respuesta sea no


Ejercicio 6: El Número Secreto
Nombre de archivo sugerido: clase06_numero_secreto.py

Objetivo: Crear un juego simple donde el usuario debe adivinar un número secreto.
El programa no se detendrá hasta que el usuario adivine el número.

Requisitos:
Crea una variable llamada numero_secreto y asígnale un número entero cualquiera (por ejemplo, 7).
Crea otra variable para guardar el número que el usuario ingresa, por ejemplo, numero_usuario.
 Puedes inicializarla en 0.
Usa un bucle while que se siga ejecutando mientras numero_usuario sea diferente de numero_secreto.
Dentro del bucle, pídele al usuario que adivine el número con input(). No olvides convertir su respuesta a int.
Después de que el bucle termine (lo que solo ocurrirá cuando el usuario adivine), imprime un mensaje de felicitaciones."""

import random
number_text = input("enter a number from 1 to 5      ")
number_user = int(number_text)
secret_number = random.randint(1, 5)
while number_user != secret_number:
    print(f"number {number_user} is not correct,try again  ")
    number_text = input("enter a number from 1 to 5      ")
    number_user = int(number_text)

print(f"Congratulation,number {number_user} is the secret number ")

