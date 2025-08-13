#Ejercicio 2: Calculadora de Edad Simple
#Objetivo: Crear un script que le pida al usuario su nombre y año de nacimiento para calcular su edad aproximada.
#Requisitos:
#Usa input() para preguntarle al usuario su nombre y guárdalo en una variable.
#Usa input() para preguntarle su año de nacimiento.
#Convierte el año de nacimiento (que será un string) a un número entero (int).
#Calcula la edad aproximada del usuario restando su año de nacimiento del año actual (puedes usar 2025).
#Muestra un mensaje de saludo personalizado que incluya su nombre y la edad que calculaste.

usuario = input("Por favor ingrese su nombre ")
print("Nombre ingresado correctamente")
nacimiento_texto = input("Por favor ingrese su año de nacimiento ")
nacimiento = int(nacimiento_texto)
print("Año ingresado correctamente")
anio_actual = 2025
edad = anio_actual - nacimiento
if nacimiento > anio_actual:
 print("¡Vaya! Parece que viajas en el tiempo. Ese año aún no ha llegado.")
else:
 print("Según el calculo ",usuario, "debe tener: ",edad," años")

