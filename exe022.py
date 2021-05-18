###"""Crie um Programa que leia o nome completo de uma pessoa e mostre
##1 O nome com todas as letras Maiúsculas
##2 o nome com todas as letras Minúsculas
#3 Quantas letras ao todos (sem Considerar espaços)
#4 quantas letras tem o primeiro nome
nome = str(input('O seu nome completo: '))
nome2 = nome.split()
print('Seu Nome em Maiúsculo: ', nome.upper())
print('Seu nome em Minúsculo: ', nome.lower())
nome1 = nome.replace(" ","")
print('Seu nome ao todo tem letras ',len(nome1.strip()))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome2[0], len(nome2[0].strip())))
