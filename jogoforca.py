
import os
import random
import time

def jogar():
    print('Deseja jogar novamente?')
    print('1.Sim')
    print('2.Não')
    jogar_novamente = int(input())

    if jogar_novamente == 1:
        limpar_tela()
        jogo_forca()
    else:
        print('Campeoes nao trapaceiam! Ate a proxima')
        exit()
def ganhou(palavra_secreta):
    limpar_tela()
    print('Parabéns você acertou')
    print(f'Palavra: {palavra_secreta}')
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')    
def numero_erros(chances):
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
def jogo_forca ():
    palavras_possiveis = [
        'abacaxi','abobora','agulha','alface','amarelo','amizade','amoroso','anel','aprender','azul','banana','batalha','beijo','bicicleta','boneca',
        'bonito','borboleta','brilhante','cadeira','cachorro','caminho','camisa','caneta','carro','casa','castelo','cereja','chapel','chocolate',
        'chuva','cidade','coelho','copo','coroa','cozinha','cristal','dentista','diamante','dinheiro','elefante','energia','escada','escola','espelho',
        'estrela','familia','fantasia','farol','felicidade','festa','floresta','flor','fruta','garfo','gato','girassol','globo','guitarra','horizonte',
        'janela','jardim','jogar','jornal','leitura','livro','lua','macaco','magia','mesa','montanha','morango','natureza','navio','nuvem','ouro','ovo',
        'palavra','papel','peixe','pipoca','planeta','prato','praia','pulmao','quadro','raposa','rio','sabedoria','sal','sapato','semente','sorriso','sol',
        'telefone','tesoura','tigre','tomate','trabalho','trem','universo','uva','vaca','vela','viagem','zebra']
    palavra_secreta = random.choice(palavras_possiveis).lower()
    palavra_oculta = ['_' for _ in palavra_secreta]
    tamanho_palavra = len(palavra_secreta)
    tentativa = 'zero'
    chances = 6
    
    while chances > 0:
        print(f'Voce tem {chances} chances')
        # f -> fstring (Formatted Srting Literals)
        # f antes das aspas da string e pode inserir variáveis diretamente dentro das chaves {} 
        print('Advinhe a palavra oculta:', ' '.join(palavra_oculta))
        tentativa = str(input('Letra: ').lower())
        numero_erros(chances)
        print()
    
        contador = 0
        for i in range (tamanho_palavra):
            if tentativa == palavra_secreta[i]:
                palavra_oculta[i] = tentativa
            else:
                contador += 1

        if contador == tamanho_palavra:
            chances -= 1
          
        if ''.join(palavra_oculta) == palavra_secreta:
            ganhou(palavra_secreta)
            jogar()   

    limpar_tela()
    print('Fim de Jogo :(')
    print(f'A palavra era: {palavra_secreta}')
    print()
    jogar()

limpar_tela() 

decisao = 0
print ('---------------------')
print ('--- jogo da forca ---')
print ('---------------------')

print('1. Jogar')
print('2. Sair')

decisao = int(input('>>> '))

if decisao == 1:
    limpar_tela()
    jogo_forca()
elif decisao == 2:
    limpar_tela()
    exit()

