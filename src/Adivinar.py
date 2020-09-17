import random

number = random.randint(1, 10)

player_name = input("Hola, cual es tu nombre?\n")



print('Hola, '+ player_name + '! Estoy pensando en un número entre 1 al 100:')


number_of_guesses = 0
while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('El número es mayor')
    if guess > number:
        print('El número es menor')
    if guess == number:
        break
if guess == number:
    print('Adivinaste el número en', number_of_guesses, 'intentos!')
else:
    print('You did not guess the number, The number was', number)