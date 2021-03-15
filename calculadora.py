def entrada():
    numero1 = int(input('Digite o primeiro numero: '))
    numero2 = int(input('Digite o segundo numero: '))
    return numero1, numero2


print('{:*^20} Python Calculator {:*^20}\n'.format('*', '*'))
print('Selecione o numero da opção desejada:\n')
print('1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão')

selecionador = int(input('Digite sua opção(1/2/3/4): '))

if selecionador == 1:
    numero1, numero2 = entrada()

    soma = lambda n, m: n + m

    print(f'{numero1} + {numero2} = {soma(numero1, numero2)}')
elif selecionador == 2:
    numero1, numero2 = entrada()

    soma = lambda n, m: n - m

    print(f'{numero1} - {numero2} = {soma(numero1, numero2)}')
    pass
elif selecionador == 3:
    numero1, numero2 = entrada()

    soma = lambda n, m: n * m

    print(f'{numero1} * {numero2} = {soma(numero1, numero2)}')
    pass
elif selecionador == 4:
    numero1, numero2 = entrada()

    soma = lambda n, m: n / m

    print(f'{numero1} / {numero2} = {soma(numero1, numero2)}')
    pass
else:
    print('Essa opção não existe.')
