from tkinter import *
import sqlite3 as lite

def criar_novo_usuario():
    janela_novo_user = Tk()
    janela_novo_user.title("Cadastro")
    janela_novo_user.geometry("500x500")
    janela_novo_user.resizable(height=False, width=False)
    label_title_novo_user=Label(janela_novo_user,text="Cadastrar novo usuário", font="Arial 25")
    label_title_novo_user.pack(pady=25)
    label_return_novo_user = Label(janela_novo_user,font="Arial 12" , text="")
    try:
        con = lite.connect()
        label_return_novo_user["text"]= "Conectado ao Banco de Dados"
        label_return_novo_user["fg"] = "green"
        label_return_novo_user.pack()
    except:
        label_return_novo_user["text"] = "Erro ao conectar no Banco de Dados"
        label_return_novo_user["fg"] = "red"
        label_return_novo_user.pack()

        
    janela_novo_user= mainloop()