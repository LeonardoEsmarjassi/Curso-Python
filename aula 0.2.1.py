# Cria uma função para diminuir meus codigos!

def PedirNota(frase):
    while True:
        nota = float(input(frase))
        if nota >= 0 and nota <= 10:
            break
    return nota    

# Vai pegar as notas e jogar pro meu comando acima 

n1 = PedirNota ('Digite sua nota no 1 bimestre: ')
n2 = PedirNota ('Digte sua nota no 2 bimestre: ')
n3 = PedirNota ('Digte sua nota no 3 bimestre: ')
n4 = PedirNota ('Digte sua nota no 4 bimestre: ')

# Vai somar a media final e dividir por 4 

mediafinal1 = (n1 + n2 + n3 + n4) / 4

# Vai mencionar qual foi minha media final 

print ('Sua média final foi {:.2f}'.format(mediafinal1))

#Se a média for maior que 5 aprovado se for menor que 2.9 reprovado se o aluno tirar 3 ou mais ele vai estar em recuperação
 
if (mediafinal1 >= 5):
    print('Você foi APROVADO')

elif (mediafinal1 >= 3):
    print('Você esta em recuperação !') 

else:
    print ('Você foi REPROVADO')  