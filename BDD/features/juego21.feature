Feature: Juego de 21 BlackJack

Scenario: Repartir las cartas
    En la primera ronda no se pueden reaprtir mas de 2 cartas
    Se repartiran las dos cartas iniciales a los jugadores
  Given Existe un maso de cartas con valores de 1 a 11
    And hay mas de un jugador
   When los jugadores tengan menos de 2 cartas
   Then El jugador obtiene las cartas

Scenario: Jugar la ronda
  Given  Las cartas que el jugador tenga y verificada la condición de alcanzar el valor exacto o cercano menor a 21.
    And  Hayan mas cartas para tomar           
   When El jugador decide plantarse o tomar otra carta
   Then El repartidor debería entregar o no  una carta de acuerdo a la decisión del jugador 

 
Scenario: Escoger el ganador
  Gana el jugador cuyo valor de mano sea mayor que el de los demás y el valor sea menor o igual a 21
  El jugador que sobrepase el valor 21 automáticamente pierde

  Given La mano de cada jugador
    And El valor de la suma de cada mano
   When Se compara el valor de la mano de cada jugador
   Then El jugador con mayor puntaje gana el juego
    But Si alguien mas obtiene el valor de 21 empatan


