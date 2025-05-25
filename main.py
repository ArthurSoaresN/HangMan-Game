import os
import random
import time

def play():
    print('Play again?')
    print('1.yes')
    print('2.no')
    play_again = int(input())

    if play_again == 1:
        clear()
        jogo_forca()
    else:
        print('Never Gonna Give You Up')
        exit()

def winner(secret_word):
    clear()
    print('Well done')
    print(f'Answer was: {secret_word}')

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def numb_erros(chances):
    if chances == 6:
        print(' ____')
        print('|')
        print('|')
        print('|')
        print('|')
        print()

    elif chances == 5:
        print(' ____')
        print('|   0 ')
        print('|  ')
        print('|  ')
        print('|')
        print()

    elif chances == 4:
        print(' ____')
        print('|   0 ')
        print('|   |')
        print('|  ')
        print('|')
        print()

    elif chances == 3:
        print(' ____')
        print('|   0 ')
        print('|  /|')
        print('|  ')
        print('|')
        print() 

    elif chances == 2:
        print(' ____')
        print('|   0 ')
        print('|  /|\\')
        print('|  ')
        print('|')
        print()

    elif chances == 1:
        print(' ____')
        print('|   0 ')
        print('|  /|\\')
        print('|  / ')
        print('|')
        print()

    elif chances == 0 :
        print(' ____')
        print('|   0 ')
        print('|  /|\\')
        print('|  / \\')
        print('|')
        print()

    else:
        print('erro')

def hangman_game():
