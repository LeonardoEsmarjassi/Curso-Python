#CRIAR UMA JANELA

import tkinter

root = tkinter.Tk()
root.title('Hello World Gráfico')
root.geometry('1920x1080')

 
#FRASE INICIAL


labelFrase = tkinter.Label(root,
                           text='Olá Developer',
                           font=('Old English Text MT' ,62),
                           fg = '#FF1333',
                           bg='white')
labelFrase.pack(padx=5,pady=5)


#FRASE DIGITE SEU NOME


labelNome = tkinter.Label(root,
                          text ='Digite seu nome',
                          font=('Old English Text MT' ,26),
                          fg = '#FF1333',
                          bg='white')
                          


labelNome.pack(padx=5,pady=5)

entryNome = tkinter.Entry(root,width=50)
entryNome.pack(padx=5,pady=5)


#BOTÃO GRAVAR 


buttonGravar = tkinter.Button(root,
                        text='Gravar',
                        command=None)

buttonGravar.pack(padx=10, pady=10)



root.mainloop()