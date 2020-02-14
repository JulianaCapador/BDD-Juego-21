#Juego 21
#Juliana Capador -Jorge Lucero

import random

#Cartas
cartas = []
#Jugadores
cartas_jugadores = []

#Repartir las cartas
while len(cartas) != 2:
	cartas.append(random.randint(1,11))
	if len(cartas) == 2:
		print("Repartido como x &",cartas[1])
#Cartasdel Jugador
while len(cartas_jugadores) != 2:
	cartas_jugadores.append(random.randint(1,11))
	if len(cartas_jugadores) == 2:
		print("Tu tienes ",cartas_jugadores)
#Suma de las cartas del repartidor
if sum(cartas) == 21:
	print("La suma de las cartas suma 21 y ganas")
elif sum(cartas) > 21:
	print("Has perdido")

#Suma de las cartas del jugador
while sum(cartas_jugadores or cartas) < 21:
	
	action_taken = str(input("¿Deseas parar (p) o tomar otra carta(t)?"))
	if action_taken == "t":
		cartas_jugadores.append(random.randint(1,11))
		print("La nueva suma es: "+str(sum(cartas_jugadores))+"de estas cartas",cartas_jugadores)
		cartas.append(random.randint(1,11))
	else:
		print("El repartidor tiene como total de "+str(sum(cartas))+" con ",cartas)
		print("tu tienes un total de "+str(sum(cartas_jugadores))+ " con ",cartas_jugadores)
		if sum(cartas) > sum(cartas_jugadores):
			print("Repartidor gana")
		else:
			print("Ganaste")
			break

if sum(cartas_jugadores) > 21:
	print("Ta pasaste, Repartidor gana")
	print ("El partidor tiene",cartas)
elif sum(cartas_jugadores) == 21:
	print("El repartidor tiene como total de "+str(sum(cartas))+" con ",cartas)
	print("has hecho 21, tú ganas")
#elif sum(cartas)==21:
#	print("El repartidor hizo 21, Tú pierdes gg")