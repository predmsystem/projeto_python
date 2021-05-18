"""Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome"""
nome = str(input('Digite seu Nome: ')).strip()
print('SILVA' in nome.upper())
