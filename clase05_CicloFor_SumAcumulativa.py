"""Objetivo: Crear un programa que calcule la suma de todos los números desde 1 hasta un número que
 elija el usuario. Por ejemplo, si el usuario ingresa 5, el programa debe calcular 1 + 2 + 3 + 4 + 5 y 
 mostrar el resultado.         Requisitos:
Pide al usuario que ingrese un número entero positivo. Vamos a llamarlo numero_limite.
Crea una variable para guardar la suma total, inicializada en 0. Por ejemplo: suma_total = 0.
Usa un bucle for que recorra todos los números desde 1 hasta numero_limite (incluido).
 Pista: Si tu variable es numero_limite, necesitarás usar range(1, numero_limite + 1).
Dentro del bucle, en cada repetición, añade el número actual a tu variable suma_total. 
La línea sería algo como: suma_total = suma_total + numero_actual.
Después de que el bucle termine, imprime el resultado final."""""

print("program start: ")
number_text = input("Please, Enter a positive number: ")
limited_number = int(number_text)
print("number entered correctly")
if limited_number > 0:
    for i in range(1, limited_number + 1):
      final_result = 0
      final_result = final_result + i
      print("=",final_result)
elif limited_number < 0:
    print("Cannot value negative number")
else:
   print("Cannot value number: 0")