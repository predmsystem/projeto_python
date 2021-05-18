from random import choice
num = int(input('Adivinhe o número de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
sort = choice(lista)
if num == sort:
  print('Parabéns você acertou! pois o número é {} exatamente'.format(sort))
else:
  print('Você errou! Tente novamente! Boa sorte! o valor aleatório foi: {}'.format(sort))
