from tkinter import *


janela = Tk()
janela.geometry('500x500')
janela.title("login")
janela.resizable(height=False, width=False)

def validar():
    nome = entry_nome.get()
    senha = entry_senha.get()

    return_msg = label_return_msg

    if nome == "root" and senha == "root":
        return_msg["fg"] = "green"
        return_msg["text"] = "Acesso concedido"
        entry_nome.delete(0, END)
        entry_senha.delete(0,END)

    elif nome =="" or senha == "":
        label_return_msg["text"] = "Nome ou senha não podem ser vázios"
        label_return_msg["fg"] = "orange"

    elif nome !="root" or senha !="root":
        label_return_msg["text"] = "Nome ou senha incorreto"
        label_return_msg["fg"] = "red"  



label_title=Label(text="Login", font="Arial 25")
label_title.pack(pady=25)

frame_nome = Frame(janela, width=170, height=80)
frame_nome.pack(pady=15)

frames_senha = Frame(janela,  width=170 , height=80)
frames_senha.pack()

label_nome = Label(frame_nome, text="Nome : ",  font="Arial 13")
label_nome.place( y=10)

entry_nome = Entry(frame_nome, relief="solid", width=25)
entry_nome.place( y=35)

label_senha = Label(frames_senha, text="Senha : ",  font="Arial 13")
label_senha.place( y=10)

entry_senha = Entry(frames_senha, relief="solid", width=25, show="*")
entry_senha.place( y=35)

label_button= Button(janela, text="Acessar", width=14, relief="solid", bg="black", fg="white", command=validar)
label_button.pack(pady=14)

label_return_msg = Label(janela, text="", font="Arial 12")
label_return_msg.pack()

janela = mainloop()
