"""
Joguinho simples de adivinhação de Naipes do baralho

De onde vieram os emojis: https://unicode.org/emoji/charts/emoji-list.html
Idealizado e desenvolvido por James Felipe
github: SemajOliveira
instagram: instagram.com/james_felipe013/
Linkedin: https://br.linkedin.com/in/james-felipe-6a4a2a1a7
"""
from random import choice as c

while True:#Loop infinito
    # Naipes disponíveis 
    naipes = ['coringa', 'ouro', 'coracao', 'paus', 'espada']

    try: #verificação de erros
        #Apresentação
        print('\nNo meu baralho existem as cartas Coringa, ouro, coracao, paus e espada')
        print('\U0001F61C' * 50)
        o = input('Qual naipe estou pensando? ').strip().lower()

        # Verificação  de naipes para o vencedor
        a = c(naipes) #a == aleátorios
        if o == a:
            if a == 'coringa':
                print('Parabéns realmente pensei no naipe \U0001F0CF')
            elif a == 'ouro':
                print('Parabéns realmente pensei no naipe \U00002666')
            elif a == 'coracao':
                print('Parabéns realmente pensei no naipe \U00002665')
            elif a == 'paus':
                print('Parabéns realmente pensei no naipe \U00002663')
            elif a == 'espada':
                print('Parabéns realmente pensei no naipe \U00002660')
        # Verificação  de naipes para o perdedor        
        else:
            print('Que pena você errou  \U0001F62A')
            if a == 'coringa':
                print('Tinha pensado no naipe \U0001F0CF')
            elif a == 'ouro':
                print('Tinha pensado no naipe no naipe \U00002666')
            elif a == 'coracao':
                print('Tinha pensado no naipe no naipe \U00002665')
            elif a == 'paus':
                print('Tinha pensado no naipe no naipe \U00002663')
            elif a == 'espada':
                print('Tinha pensado no naipe no naipe \U00002660')
    except:
        print('Error \U0000274C')
    #Verificando se o jogador vai continuar jogando ou não    
    op = input('Você quer continuar jogando Sim/Não: ').strip().lower()
    if op == 'nao':
        print('Obrigado por ter Jogado \U0001F63B')
        break

    # Foi legal desenvolver, mas não gostei de perder