"""Faça um programa que leia uma frase pelo teclado e mostre
1 Quantas vezes aparece a letra A
2 Em que posição ela aparece a primeira vez
3 em que posição ela aparece a ultima vez"""
frase = str(input('Digite uma frase? ')).strip().lower()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))
