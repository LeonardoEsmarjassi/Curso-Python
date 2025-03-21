while True:
    n1 = float(input ('Digite sua nota no primeiro bimestre ?'))
    if n1 <=10 and n1 >=0:
        break


#Se o aluno não colocar um numero de 0 a 10 ira aparecer isso 

if(n1 > 10):
    n1 = float(input ('Erro digite a sua nota do primeiro bimestre novamente'))
    


while True:
    n2 = float(input ('Digte sua nota no segundo bimestre ?'))
    if n2 <= 10 and n2 >=0:
        break


#Se o aluno não colocar um numero de 0 a 10 ira aparecer isso 

if(n2 > 10):
    n2 = float(input ('Erro digite a sua nota do segundo bimestre novamente'))



while True:
    n3 = float(input ('Digte sua nota no terceiro bimestre ?'))
    if n3 <= 10 and n3 >=0:
        break


#Se o aluno não colocar um numero de 0 a 10 ira aparecer isso 

if(n3 > 10):
    n3 = float(input ('Erro digite a sua nota do terceiro bimestre novamente'))


  
while True:
    n4 = float(input ('Digte sua nota no quarto bimestre ?'))
    if n4 <= 10 and n4 >=0:
        break


#Se o aluno não colocar um numero de 0 a 10 ira aparecer isso 
 
if(n4 > 10):
    n4=float(input ('Erro digite a sua nota do quarto bimestre novamente'))




mediafinal1 = (n1 + n2 + n3 + n4) / 4

notatotal = (n1 + n2 + n3 + n4)

print ('Sua média final foi {:.2f} e sua nota total foi {:.2f}'.format(mediafinal1, notatotal))

#Se a média for maior que 5 aprovado se for menor que 2.9 reprovado se o aluno tirar 3 ou mais ele vai estar em recuperação
 
if (mediafinal1 >= 5):
    print('Você foi APROVADO')

elif (mediafinal1 >= 3):
    print('Você esta em recuperação !') 

else:
    print ('Você foi REPROVADO')  
