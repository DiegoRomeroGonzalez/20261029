""" Lista = [10,9,8,7,6,5,4,3,2,1,0]

for number in range (10,-1, -1):
    if number == 5:
        print("...")
    if number < 8 and number > 3:
        continue
    print (number)
    if number == 0:
        print ("BOOM")


import time


for number in range(10,-1,-1):
    print(number)
    time.sleep(1)

    if number == 0:
        print ("Despierta vago")

    else:
        print (f"Te quedan {number} segundos para dormir")
        
"""


import random


Colores = ["rojo","amarillo", "verde", "azul", "negro"]
x = random.choice(Colores)

intentos = 3

Elige_color = input("Si no desactivas la bomba, saldrás volando. Elige un cable que cortar (rojo, amarillo, verde, azul, negro) ").strip().lower()

while intentos > 0:
    while Elige_color not in Colores:
        print ("Ese color no es válido")
        Elige_color = input("Elija un color válido: rojo, amarillo, verde, azul o negro ").strip().lower()

    if Elige_color == x:
        print("Has desactivado la bomba correctamente, vives.")
    break

    else:   
    intentos -= 1

    if intentos > 0:
        print(f"Color incorrecto. Te quedan {intentos} intentos")
        Elige_color = input("Vuelve a introducir un color: ").strip().lower()

if intentos == 0:
    print("¡BOOM! Has muerto")




