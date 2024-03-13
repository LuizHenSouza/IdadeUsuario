# Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
# A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará,
# no ano atual (2022).

# Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

import time, os

while(True):
    try:
        Nome = str(input("Digite seu nome: "))
        AnoNascimento = int(input("Digite seu ano de nascimento: "))
        if(AnoNascimento >= 1922 and AnoNascimento <= 2021):
            print("Nome: " + Nome)
            print("Idade: " + str((2022 - AnoNascimento)))
            time.sleep(2)
            break
        else:
            print("O ano informado não foi aceito pelo sistema!")
            time.sleep(2)
            os.system("cls")
    except:
        print("Um dos valores inseridos pelo usuário pode estar incorreto, tente novamente!")
        time.sleep(2)
        os.system("cls")