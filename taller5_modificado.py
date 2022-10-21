#TALLER 5 PYTHON 
#AUTOR(A): JUAN CAMILO PEREZ
# FECHA: 20-OCTUBRE-2022
from datetime import date
hoy =date.today()	#fecha actual
nombre=input('Digite su nombre:')
print("Bienvenido",nombre.title())	
print("Hoy es el dia: ", hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR MODIFICADO")
print()
num1=int(input("Digite el primer numero: "))
num2=int(input ("Digite el segundo numero mayor al anterior:"))
print("Se ejecuta el primer Ciclo FOR") 
for i in range(num1):
  print(i+1)
print('fin del primer Ciclo FOR')
print()
print("Ciclo del Primer al Segundo numero digitado") 
for i in range(num1,num2):
   print(i)
print('fin del ciclo')
print ()
print ("Ciclo del Primer al Segundo numero digitado con incrementos de 5")
for i in range(num1,num2, 5):
     print(i)
print ( 'fin del ciclo')
print ()
frase=input("Digite una frase : ") 
frase=frase.upper()
for character in frase:
   print(character)
print("Final del programa ciclo For")
