from tkinter import *

# função que irá pegar a chave
def cryptoKey(text):
    print(text)

# função que irá descriptografar o texto
def descryptoKey(text):
    print(text)

menu_inicial = Tk()

menu_inicial.title("window")

menu_inicial['bg'] = "blue"

chave_label = Label(menu_inicial, text='Chave Criptográfica')
chave_label.grid(column=0, row=0)
codigo = Entry(menu_inicial, width=100)
codigo.grid(column=0, row=1)

botao = Button(menu_inicial, text="Enviar Chave", command=lambda: cryptoKey(codigo.get()))
botao.grid(column=0, row=2)

text = Label(menu_inicial, text='Texto')
text.grid(column=0, row=3)
codigo2 = Entry(menu_inicial, width=100)
codigo2.grid(column=0, row=4)

botao2 = Button(menu_inicial, text="Enviar para Despitografar", command=lambda: descryptoKey(codigo.get()))
botao2.grid(column=0, row=5)

menu_inicial.mainloop()