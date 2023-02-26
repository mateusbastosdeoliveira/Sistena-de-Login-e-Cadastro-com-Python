cadastro_nome = str(input("Cadastre um Nome : "))

validacao_senha = False

while validacao_senha == False:
    cadastro_senha = str(input("Cadastre uma Senha : "))
    quant_senha = len(cadastro_senha)
    if quant_senha >= 5:
        validacao_senha = True
        check_credenciais = False
        while check_credenciais == False:
            check_nome = str(input("Digite o nome cadastrado : "))
            check_senha = str(input("Digite a senha cadastrada : "))
            if check_nome == cadastro_nome and check_senha == cadastro_senha:
                check_credenciais = True
                print("Acesso concedido!")
            else:
                print("Nome ou senha incorretos, tente novamente")
                check_credenciais = False

    else:
        print("Senha deve conter mais que 5 caracteres,tente novamente")
        validacao_senha = False







    