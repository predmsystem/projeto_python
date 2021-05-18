"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
exe: Ana Maria de Souza
Primeiro = Ana
Ultimo = Souza"""
nome = str(input('Digite seu Nome completo: ')).strip()
n = nome.split()
print('Muito Prazer em te conhecer!')
print('Seu primeiro pome é: {}'.format(n[0]))
print('Seu último nome é: {} '.format(n[len(n)-1]))
