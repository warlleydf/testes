import os
import random

palavras_secretas = ['amarelo', 'vermelho', 'cadeira', 'elefante', 'teclado', 'hospital', 'novela', 'acidente', 'celular']

def reiniciar_jogo():
    return random.choice(palavras_secretas), '', '', 0

def jogar_jogo():
    continuar_jogo = True
    
    while continuar_jogo:
        palavra_secreta, letras_acertadas, letras_erradas, qtd_tentativas = reiniciar_jogo()
        
        while True:
            letra_digitada = input('Por Favor Digite Uma letra: ').lower()
            qtd_tentativas += 1

            if letra_digitada.isdigit():
                print('ERRO - Não digite Números')
                continue
            if len(letra_digitada) > 1:
                print('ERRO - Digite APENAS uma letra por vez.')
                continue

            if letra_digitada in palavra_secreta:
                letras_acertadas += letra_digitada
            else:
                letras_erradas += letra_digitada
            
            palavra_formada = ''

            for letra_secreta in palavra_secreta:
                if letra_secreta in letras_acertadas:
                    palavra_formada += letra_secreta
                else:
                    palavra_formada += '*'
                
            os.system('cls')
            print('Palavra Secreta: ', palavra_formada)

            if palavra_formada == palavra_secreta:
                print()
                print('PARABÉNS VOCÊ ACERTOU A PALAVRA SECRETA.')
                contador_letras_erradas = sum(1 for letra in letras_erradas if letra.isalpha())
                print(f'Você digitou o total de {qtd_tentativas} letras e errou {contador_letras_erradas} letras')
                print()

                reiniciar = input('Você gostaria de jogar novamente? (S/N): ').lower()
                if reiniciar != 's':
                    print('Jogo Encerrado')
                    print()
                    continuar_jogo = False
                else:
                    print('Jogo Reiniciado')
                    print()
                break
            
            print('Essas letras você já tentou e estão erradas: ', letras_erradas)

while True:
    jogar_jogo()
    break