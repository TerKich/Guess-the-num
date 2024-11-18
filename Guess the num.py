# Guess the num
from random import *

found = False
random_number = randint(1, 50)
attempt = 10

start = input('Game guess the number - a game in which you need to guess a number from 1 to 50, will you write more than the number you chose or less than the most mysterious number \n\nReady? you have only 10 devices (write “ready”): ')

if start == 'ready':
    while found != True:
        guess = int(input('Enter a number from 1 to 50: '))
        
        if attempt == 0:
            choice = input('youve run out of tries. want to try again? (no/yes): ')
            if choice == 'yes':
                print(guess)
                attempt = 10
            else:
                break
        elif guess == random_number:
            print('Well done, you guessed it right.')
            break
        elif guess > random_number: 
            attempt -= 1
            print('Your number is greater than the mysterious one. ' + 'you still have ' + str(attempt) + ' attempts')
            continue
        elif guess < random_number: 
            attempt -= 1
            print('Your number is less than the mysterious one. ' + 'you still have ' + str(attempt) + ' attempts')
            continue
