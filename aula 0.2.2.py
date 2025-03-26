def preço (frase):
    while True:
        valor= float(input(frase))
        if valor >= 0:
            break
    return valor

valor1 = preço ('Digite o valor do primeiro produto:') 
valor2 = preço ('Digite o valor do segundo produto:') 
valor3 = preço ('Digite o valor do terceiro produto:') 

mediaprodutos = (valor1 + valor2 + valor3) / 3

print ('As médias dos valores são {:.2f}'.format(mediaprodutos))