import random
import string

# Evalua el valor adivinado
def guess_val():
    if guess < val:
        print(b, 'es mayor')
    if guess > val:
        print(b, 'es menor')

# Define de forma aleatoria si se adivinará letras o números
def random_game():
    adiv = random.randint(0,1)
    if adiv == 0:
        a = random.randint(1, 100)
        b = "un número"
        c = "1 al 100"
    else:
        alpha = string.ascii_lowercase
        ran = random.randint(0,len(alpha)-1)
        a = alpha[ran]
        b = "una letra"
        c = "\'a\' a la \'z\'"
    return a, b, c


player_name = input("Hola, ¿cuál es tu nombre?\n")
val, tipo, rango = random_game()
print('¡Hola, '+ player_name +'! Estoy pensando en '+ tipo +' entre '+ rango +':')

number_of_guesses = 0
while True: #Para definir número de intentos máximo cambiar a while number_of_guesses < #
    if tipo == "un número":
        guess = int(input("Posible número: "))
        b = "El número" 
    else:
        guess = input("Posible letra: ")
        b = "La letra"
    number_of_guesses += 1
    guess_val()
    if guess == val:
        break

if guess == val:
    print('¡Adivinaste en', number_of_guesses, 'intentos!')
else: #solo se ejecutará cuando se defina un número de intentos máximo
    print('¡Número de intentos superados!', b, 'es', val) 