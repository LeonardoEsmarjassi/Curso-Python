while True:
    try:
        n1 = float(input('Digite sua nota no primeiro bimestre: '))
        if 0 <= n1 <= 10:  # Verifica se a nota está entre 0 e 10
            break  # Se a nota for válida, sai do laço
        else:
            print("Erro! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

while True:
    try:
        n2 = float(input('Digite sua nota no segundo bimestre: '))
        if 0 <= n2 <= 10:  # Verifica se a nota está entre 0 e 10
            break  # Se a nota for válida, sai do laço
        else:
            print("Erro! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

while True:
    try:
        n3 = float(input('Digite sua nota no terceiro bimestre: '))
        if 0 <= n3 <= 10:  # Verifica se a nota está entre 0 e 10
            break  # Se a nota for válida, sai do laço
        else:
            print("Erro! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

while True:
    try:
        n4 = float(input('Digite sua nota no quarto bimestre: '))
        if 0 <= n4 <= 10:  # Verifica se a nota está entre 0 e 10
            break  # Se a nota for válida, sai do laço
        else:
            print("Erro! Digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")

# Calculando a média final e a nota total
mediafinal1 = (n1 + n2 + n3 + n4) / 4
notatotal = (n1 + n2 + n3 + n4)

# Exibe a média e a nota total
print('Sua média final foi {:.2f} e sua nota total foi {:.2f}'.format(mediafinal1, notatotal))

# Condições de aprovação
if mediafinal1 >= 5:
    print('Você foi APROVADO')
elif mediafinal1 >= 3:
    print('Você está em recuperação!')
else:
    print('Você foi REPROVADO')
