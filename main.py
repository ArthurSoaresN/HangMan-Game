import os
import random
import time

def play():
    print('Play again?')
    print('1.Yes')
    print('2.No')
    play_again = int(input())

    if play_again == 1:
        clear()
        hangman_game()
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
    word_list = [
'pineapple','pumpkin','needle','lettuce','yellow','friendship','loving','ring','learn','blue','banana','battle','kiss','bicycle','doll','beautiful',
'butterfly','bright','chair','dog','path','shirt','pen','car','house','castle','cherry','hat','chocolate','rain','city','rabbit','cup','crown','kitchen',
'child','crystal','dentist','diamond','money','elephant','energy','ladder','school','mirror','star','family','fantasy','lighthouse','happiness','party',
'forest','flower','fruit','fork','cat','sunflower','globe','guitar','horizon','window','garden','play','newspaper','reading','lemon','book','moon','monkey',
'magic','watermelon','table','mountain','strawberry','music','nature','ship','cloud','glasses','gold','egg','word','paper','fish','popcorn','planet','plate',
'beach','lung','painting','radio','fox','clock','river','soap','wisdom','salt','shoe','seed','smile','sun','phone','scissors','tiger','tomato','work','train',
'universe','grape','cow','candle','travel','guitar','zebra']
    secret_word = random.choice(word_list).lower()
    hidden_word = ['_' for _ in secret_word]
    word_size = len(secret_word)
    tryin = 'zero'
    chances = 6
    
    while chances > 0:
        print(f'You have {chances} chances')
        print('Guess the word:', ' '.join(hidden_word))
        tryin = str(input('Letter: ').lower())
        numb_erros(chances)
        print()
    
        cont = 0
        for i in range (word_size):
            if tryin == secret_word[i]:
                hidden_word[i] = tryin
            else:
                cont += 1

        if cont == word_size:
            chances -= 1
          
        if ''.join(hidden_word) == secret_word:
            winner(secret_word)
            play()   

    clear()
    print('Game Over :(')
    print(f'Answer was: {secret_word}')
    print()
    play()

clear() 

decision = 0
print ('----------------------')
print ('---  Hangman Game  ---')
print ('----------------------')

print('1. Play')
print('2. Quit')

decision = int(input('>>> '))

if decision == 1:
    clear()
    hangman_game()
elif decision == 2:
    clear()
    exit()