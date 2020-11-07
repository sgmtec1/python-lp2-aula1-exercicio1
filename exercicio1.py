"""
Escreva um programa que solicita ao usuário três valores
e exiba na tela a média dos valores digitados.
"""

a = float(input('Digite o primeiro numero: '))
b = float(input('Digite o segundo numero: '))
c = float(input('Digite o terceiro numero: '))
media = (a + b + c) / 3
print('Média dos numeros: ', media)

# Outras maneiras para formatar a saída:
# print('Média dos numeros: {}'.format(media))
# print(f'Média dos numeros: {media}')
