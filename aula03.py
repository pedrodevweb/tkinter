from tkinter import *
from tkinter import font

janela = Tk()
janela.title("Aula 03")
janela.geometry("600x500+0+0")
# bloquear alterações nas dimensões da página
janela.resizable(1, 1)

label1 = Label(
    janela, text="Frase de testes",
    font="Arial 20",
    width=40,
    height=3,
    # anchor serve para posicionar nos pontos cardeais
    anchor=NW,
    bd=2,
    relief='solid'
).pack()
label2 = Label(janela, text="kkkkkk", bd=3, relief=SOLID,
               width=40,
               height=3,
               anchor=NE,
               font="Times 20 bold italic")
label2.pack()
janela.mainloop()
