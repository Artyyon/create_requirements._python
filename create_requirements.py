""" 
    Gerador de requeriments.txt
    Programa para criação do arquivo de requerimentos.
    

    Autor: Art
"""
import os

# Recuperando pip list
# https://techexpert.tips/pt-br/python-pt-br/python-executando-comandos-shell/

pip_list = os.popen('pip list')

content = pip_list.readlines()
content = [x. rstrip('\n') for x in content]

content = content[2:]

with open('requirements.txt', 'w') as arquivo:
    for x in content:
        palavra = x.split()
        if palavra == []:
            pass
        elif '[' in palavra[0]:
            pass
        else:
            arquivo.write(palavra[0] + '==' + palavra[1] + '\n')
