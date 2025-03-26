while True:
    n1 = float(input ('Digite sua nota no 1 bimestre ?'))
    if n1 <=10 and n1 >=0:
        break
    
while True:
    n2 = float(input ('Digte sua nota no 2 bimestre ?'))
    if n2 <= 10 and n2 >=0:
        break

while True:
    n3 = float(input ('Digte sua nota no 3 bimestre ?'))
    if n3 <= 10 and n3 >=0:
        break
  
while True:
    n4 = float(input ('Digte sua nota no 4 bimestre ?'))
    if n4 <= 10 and n4 >=0:
        break

mediafinal1 = (n1 + n2 + n3 + n4) / 4


print ('Sua média final foi {:.2f}'.format(mediafinal1))

#Se a média for maior que 5 aprovado se for menor que 2.9 reprovado se o aluno tirar 3 ou mais ele vai estar em recuperação
 
if (mediafinal1 >= 5):
    print('Você foi APROVADO')

elif (mediafinal1 >= 3):
    print('Você esta em recuperação !') 

else:
    print ('Você foi REPROVADO')  