'''
Exercício 01 - Python para Zumbis
-------------
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
'''
while True:
    x = int(input('Digite uma nota (entre 0 e 10): '))
    if x < 0 or x > 10:
        print(f'Nota [{x}] é inválida!')
    else:
        break
