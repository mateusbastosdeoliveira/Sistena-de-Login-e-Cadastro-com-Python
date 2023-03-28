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
        con = lite.connect("users.db")
        label_return_novo_user["text"]= "Conectado ao Banco de Dados"
        label_return_novo_user["fg"] = "green"
        label_return_novo_user.pack()
        

        def Cadastrar():
            nome =entry_nome.get()
            data_nasc = entry_data.get()
            cpf = entry_cpf.get()
            endereco = entry_endereco.get()
            quant = len(nome)
            quant_cpf  = len(cpf)
            

            if nome == "" or data_nasc == "" or cpf == "" or endereco == "":
                 label_return_msg["text"] = "Campo(s) vázio(s)"
                 label_return_msg["fg"] = "red" 

            elif quant < 5:
                label_return_msg["text"] = "Nome deve conter mais que 5 caracteres"

            elif quant_cpf != 11:
                label_return_msg["text"] = "Quantidade de CPF inválido, deve ter 11 digitos"
                label_return_msg["fg"] = "red" 
              
                
            elif nome != "" or data_nasc != "" or cpf != "" or endereco != "":

                with con:
                    cursor = con.cursor()
                    cursor.execute("insert into usuario(nome, data_nascimento, cpf, endereco) values( ?, ?, ?,?)", (nome, data_nasc, cpf, endereco))


                label_return_msg["text"] = "Usuário cadastrado"
                label_return_msg["fg"] = "green"
                entry_nome.delete(0, END)
                entry_data.delete(0, END)
                entry_cpf.delete(0, END)
                entry_endereco.delete(0, END)             


    except:
        label_return_novo_user["text"] = "Erro ao conectar no Banco de Dados"
        label_return_novo_user["fg"] = "red"
        label_return_novo_user.pack()

    def Voltar():
        janela_novo_user.destroy()

    label_nome = Label(janela_novo_user,text="Nome : ",  font="Arial 13")
    label_nome.pack(pady=5)
    entry_nome = Entry(janela_novo_user, relief="solid", width=25)
    entry_nome.pack(pady=2)

    label_data = Label(janela_novo_user,text="Data de Nascimento : ",  font="Arial 13")
    label_data.pack(pady=5)
    entry_data = Entry(janela_novo_user, relief="solid", width=25)
    entry_data.pack(pady=2)
    
    label_cpf = Label(janela_novo_user,text="CPF : ",  font="Arial 13")
    label_cpf.pack(pady=5)
    entry_cpf = Entry(janela_novo_user, relief="solid", width=25)
    entry_cpf.pack(pady=2)

    label_endereco = Label(janela_novo_user,text="Endereço : ",  font="Arial 13")
    label_endereco.pack(pady=5)
    entry_endereco = Entry(janela_novo_user, relief="solid", width=25)
    entry_endereco.pack(pady=2)

    label_button= Button(janela_novo_user, text="Cadastrar", width=14, relief="solid", bg="black", fg="white", command=Cadastrar)
    label_button.pack(pady=10)

    label_button= Button(janela_novo_user, text="Voltar", width=14, relief="solid", bg="black", fg="white", command=Voltar)
    label_button.pack(pady=2)

    label_return_msg = Label(janela_novo_user, text="", font="Arial 12")
    label_return_msg.pack(pady=25)
        
    janela_novo_user= mainloop()
