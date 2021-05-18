"""Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
exe: digite um número: 1834
unidade: 4
dezenas: 3
centena: 8
milhar: 1
EXEMPLO 01:
num = int(input('Divite um valor Inteiro: '))
n = str(num)
print('Analizando o número {}'.format(num))
print('Unidades {}'.format(n[3]))
print('Dezenas {}'.format(n[2]))
print('Centenas {}'.format(n[1]))
print('Milhar {}'.format(n[0]))
"""
num = int(input('Divite um valor Inteiro: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número {}'.format(num))
print('Unidades {}'.format(u))
print('Dezenas {}'.format(d))
print('Centenas {}'.format(c))
print('Milhar {}'.format(m))
