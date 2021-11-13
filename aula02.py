from tkinter import *
from tkinter import font

teste = Tk()
teste.title("Teste Full")
teste.geometry('500x200+200+200')
teste.resizable(0, 0)
teste.state('zoomed')
teste['bg'] = "grey"


def clear():
    print("clear")


label_1 = Label(teste,
                text="Digite seu nome:",
                bg="yellow",
                fg="black",
                font="Sans-serif 20 italic")
label_1.pack()
label_2 = Label(teste, text="Digite sua idade:",
                font="Arial 20 bold",
                width=30,
                height=10)
label_2.pack()

label_3 = Label(teste, text="Frase 1",
                # definir a fonte e o tamanho
                font="Arial 30",
                # definir a borda
                borderwidth=9,
                # definir o tipo de borda
                relief="solid")
label_3.pack()
botao = Button(teste, text="Executar", command=clear, bd=10, relief="solid")
botao.pack()

botao = Button(teste, text="flat", command=clear, bd=10, relief="flat")
botao.pack()

botao = Button(teste, text="raised", command=clear, bd=10, relief="raised")
botao.pack()

teste.mainloop()
