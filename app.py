from tkinter import *
from novo_user import criar_novo_usuario
import sqlite3 as lite




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

        def realizar_consulta():
            conexao = lite.connect("users.db")
            cursor = conexao.cursor()
            result_entry = entry_resultado.get()
                
            if result_entry == "":
                    label_resultado["text"] = ""
                    label_msg_resultado["text"] = "Campo de busca vázio"
                    label_resultado["text"] = ""
                    label_msg_resultado["fg"] = "red"
                
            elif result_entry != "":
                if len(result_entry) != 11:
                 label_resultado["text"] = ""
                 label_msg_resultado["text"] = "Quantidade digitado inválido"
                 label_msg_resultado["fg"] = "red"

                elif len(result_entry) == 11:                       
                        cursor.execute(f"select nome  from usuario where cpf= {result_entry} ")
                        resultado =  cursor.fetchone()
                        if resultado:
                            label_msg_resultado["fg"] = "green"
                            label_msg_resultado["text"] = resultado[0]
                        else:
                            label_msg_resultado["text"] ="CPF não localizado"
                            label_msg_resultado["fg"] = "red"
                            
                     
                    
                

        janela_user =  Tk()
        janela_user.title("Usuário")
        janela_user.geometry("500x500")
        janela_user.resizable(height=False,width=False)
        label_user = Label(janela_user,text=f"Olá, {nome}", font="Arial 15")
        label_user.pack(pady=5)

        entry_resultado = Entry(janela_user, width=20, relief="solid")
        entry_resultado.pack(pady=5)

        button_consultar_users = Button(janela_user, text="Buscar usuário por CPF", fg="white", bg="black", command=realizar_consulta)
        button_consultar_users.pack(pady=10)
 
        label_resultado = Label(janela_user,  text="", font="Arial 15")
        label_resultado.pack()
         
        label_msg_resultado = Label(janela_user, text="", font="Arial 15")
        label_msg_resultado.pack()
        

        janela.destroy()
        
        janela_user.mainloop()
        

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

label_novo_user = Button(janela,text="Novo usuário", width=14, relief="solid", bg="black", fg="white", command=criar_novo_usuario)
label_novo_user.pack()

label_return_msg = Label(janela, text="", font="Arial 12")
label_return_msg.pack(pady=25)

janela = mainloop()
