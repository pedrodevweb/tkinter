from tkinter import *

# iniciar a janela principal
menu_inicial = Tk()
menu_inicial['bg'] = '#202024'


# mudar o nome da janela
menu_inicial.title("Primeiro App")


def cmd_Click():
    print("Digite seu nome")
    nome = input()
    print(nome)


# botão
btn = Button(menu_inicial, text="Executar",
             command=cmd_Click)
btn.pack()


# definir as medidas e o local inicial da janela
# menu_inicial.geometry('500x250+200+200')

# deixar as dimensões fixas, usar valores boleanos
menu_inicial.resizable(width=1, height=1)

# definir dimensões mínimas e máximas
#menu_inicial.minsize(500, 250)
#menu_inicial.maxsize(700, 400)

# fazer a aplicação cobrir toda a tela
menu_inicial.state("zoomed")


# chamar a janela
menu_inicial.mainloop()
