from behave import *
import Blackjack

@given('Existe un maso de cartas con valores de 1 a 11')
def step_impl(context):
	context.cartas= []
	#assert (len(context.cartas) == 2)
	
@when('los jugadores tengan menos de 2 cartas')
def step_impl(context):
    assert (len(context.cartas and context.cartas_jugadores) < 2)
	
@then('El jugador obtiene las cartas')
def step_impl(context):
   print("funciona when")


@given('Las cartas que el jugador tenga y verificada la condición de alcanzar el valor exacto o cercano menor a 21.')
def step_impl(context):
    print("STEP: Given Las cartas que el jugador tenga y verificada la condición de alcanzar el valor exacto o cercano menor a 21.")


@given('Hayan mas cartas para tomar')
def step_impl(context):
    print("STEP: Given Hayan mas cartas para tomar")


@when('El jugador decide plantarse o tomar otra carta')
def step_impl(context):
    print("STEP: When El jugador decide plantarse o tomar otra carta")


@then('El repartidor debería entregar o no  una carta de acuerdo a la decisión del jugador')
def step_impl(context):
    print("STEP: Then El repartidor debería entregar o no  una carta de acuerdo a la decisión del jugador")


@given('La mano de cada jugador')
def step_impl(context):
   print("STEP: Given La mano de cada jugador")


@given('El valor de la suma de cada mano')
def step_impl(context):
    print("STEP: Given El valor de la suma de cada mano")


@when('Se compara el valor de la mano de cada jugador')
def step_impl(context):
    print("STEP: When Se compara el valor de la mano de cada jugador")


@then('El jugador con mayor puntaje gana el juego')
def step_impl(context):
    print("STEP: Then El jugador con mayor puntaje gana el juego")


@then('Si alguien mas obtiene el valor de 21 empatan')
def step_impl(context):
    print("STEP: Then Si alguien mas obtiene el valor de 21 empatan")