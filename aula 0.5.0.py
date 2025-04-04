import tkinter as tk

#Comando Adição

def fnAdição():
    x = float(entrynumero1.get())
    y = float(entrynumero2.get())
    resultado = x + y
    lblResultado.config(text=f'A soma é {resultado}')

#Comando Subtração

def fnSubtração():
    x = float(entrynumero1.get())
    y = float(entrynumero2.get())
    resultado = x - y
    lblResultado.config(text=f'A Subtração é {resultado}')

#Comando Multiplicação

def fnMultiplicação():
    x = float(entrynumero1.get())
    y = float(entrynumero2.get())
    resultado = x * y
    lblResultado.config(text=f'A multiplicação é {resultado}')

#Comando Divisão

def fnDivisão():
    x = float(entrynumero1.get())
    y = float(entrynumero2.get())
    resultado = x / y
    lblResultado.config(text=f'A divisão é {resultado}')

# Desenhar a janela,Titulo janela e Tamanho da janela 

janela = tk.Tk() # Desenhe uma janela
janela.title('Calculadora - A Super Calculadora ✔') # Nome da página
janela.geometry ('1920x1080') # Tamanho da janela


ibiTitulo = tk.Label(janela,
                     text='Calculadora',
                     font=('Old English Text Mt',62),
                     bg='white',
                     width=1080)
ibiTitulo.pack(padx=5,pady=5)

#PRIMEIRO NUMERO

lblNumero1 = tk.Label(janela,
                      text = ('Digite um número:'),
                      font= ('Old English Text Mt',30))
lblNumero1.pack(padx=5,pady=5)

entrynumero1=tk.Entry(janela,
                      width=50,
                      font=('Old English Text Mt',20))
entrynumero1.pack(padx=5,pady=5)

#SEGUNDO NUMERO 

lblNumero2 = tk.Label(janela,
                      text = ('Digite o segundo número:'),
                      font= ('Old English Text Mt',30))
lblNumero2.pack(padx=5,pady=5)

entrynumero2=tk.Entry(janela,
                      width=50,
                      font=('Old English Text Mt',20))
entrynumero2.pack(padx=5,pady=5)

#Botão Adição

btnAdicao = tk.Button(janela,
                      text=('Adição'),
                      font=('Old English Text Mt',20),
                      bg='white',
                      width=10,
                      command=fnAdição)
btnAdicao.pack(padx=5,pady=5)

#Botão Subtração

btnSub = tk.Button(janela,
                      text=('Subtração'),
                      font=('Old English Text Mt',20),
                      bg='white',
                      width=10,
                      command=fnSubtração)
btnSub.pack(padx=5,pady=5)

#Botão Multiplicação

btnMult = tk.Button(janela,
                      text=('Multiplicação'),
                      font=('Old English Text Mt',20),
                      bg='white',
                      width=10,
                      command=fnMultiplicação)
btnMult.pack(padx=5,pady=5)

#Botão Divisão

btnDivisão = tk.Button(janela,
                      text=('Divisão'),
                      font=('Old English Text Mt',20),
                      bg='white',
                      width=10,
                      command=fnDivisão)
btnDivisão.pack(padx=5,pady=5)

#Resultado

lblResultado=tk.Label(janela,
                      text='0,00',
                      font=('Old English Text Mt',30))
lblResultado.pack(padx=5,pady=5)


janela.mainloop() # Mainloop mantém o programa rodando