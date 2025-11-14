import os
import time
import random

numero_secreto = random.randint(1, 10)

tentativas = 0
max_tentativas = 10
acertou = False

print("Bem vindo ao jogo de adivinhacao!")
print("Tente adivinhar o numero secreto entre 1 e 10.")

while tentativas < max_tentativas:
    try:
        palpite = int(input("Digite seu palpite: "))
    except ValueError:
        print("Por favor, digite um numero valido.")
        continue   

    tentativas += 1

    # verificacao do palpite
    if palpite == numero_secreto:
        acertou = True
        break 
    elif palpite < numero_secreto:
        print("Tente um numero maior.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print("Tente um numero menor.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

if acertou:
    print(f"Parabens! Voce acertou o numero {numero_secreto} em {tentativas} tentativas.")
else:
    print(f"Voce perdeu! O numero secreto era {numero_secreto}.")
