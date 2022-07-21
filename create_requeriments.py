""" 
    Gerador de requeriments.txt
    Programa para criação do arquivo de requerimentos.
    Execute 'make' caso no linux ou o 'exec.bat' caso no windows.
    Para executar em virtualizações do python você terá que alterar o arquivo .bat para funcionar no windows.

    Autor: Art
"""
import sys
import os

if len(sys.argv) == 1:
    print("Error: Falha em recuperar arquivo de entrada.")  # Arrumar depois
    exit()

param = sys.argv[1]

content = -1

with open(param) as arquivo:
    content = arquivo.readlines()
    content = [x. rstrip('\n') for x in content]

content = content[2:]

if content == -1:
    print("Error: arquivo 'saida.txt' com formato invalido")  # Arrumar depois
    exit()

with open('requirements.txt', 'w') as arquivo:
    for x in content:
        palavra = x.split()
        if palavra == []:
            pass
        elif '[' in palavra[0]:
            pass
        else:
            arquivo.write(palavra[0] + '==' + palavra[1] + '\n')

print("Sucesso: arquivo 'requeriments.txt' criado com sucesso.")
