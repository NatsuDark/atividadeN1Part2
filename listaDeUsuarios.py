def menuEscolhas(listaPrincipal):
    listaEscolhas = [1,2,3,4,5,6,7]
    print('''
    Bem vindo gestor,o que deseja fazer?
    (1) - Cadastrar novos usuários pelo seu nome completo e e-mail
    (2) - Exibir todos os usuários cadastrados, listando-os por ordem de cadastro.
    (3) - Exibir todos os usuários cadastrados, listando-os por ordem alfabética.
    (4) - Verificar se um usuário faz parte da lista de participantes, buscando-o pelo seu nome
    (5) - Remover um usuário cadastrado, buscando-o por seu email.
    (6) - Alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.
    (7) - Finalizar o Programa
    ''')
    escolha = int(input())
    if escolha in listaEscolhas:
        leitorEscolha(escolha, listaPrincipal)
    else:
        print("\033[1;31mEscolha inválida, insira uma escolha válida.\033[0;0m")
        menuEscolhas (listaPrincipal)

def leitorEscolha(escolha, listaPrincipal):
    print("\n\n","-"*25,"\n\n")
    if escolha == 1:
        escolha1(listaPrincipal)
    elif escolha == 2:
        escolha2(listaPrincipal)
    elif escolha == 3:
        escolha3(listaPrincipal)
    elif escolha == 4:
        escolha4(listaPrincipal)
    elif escolha == 5:
        escolha5(listaPrincipal)
    elif escolha == 6:
        escolha6(listaPrincipal)
    elif escolha == 7:
        quit()

def escolha1(listaPrincipal):
    print("Você escolheu a opção de cadastrar novos usuários pelo seu nome completo e e-mail.")
    nome = input("Por favor, insira o nome completo do usuário que deseja adicionar:\n")
    while (True):
        email = input("Insira o seu email:\n")
        if email.find("@") == -1:
            print("\033[1;31mDigite um e-mail valido!!\033[0;0m")
        else:
            break
    nome = nome.title()
    
    print("O nome \"%s\" e o e-mail \"%s\" serão adicionados ao sistema.\n" %(nome,email))
    if confirmarEscolha():
        listaPrincipal.append(nome)
        listaPrincipal.append(email)
        print("O nome \"%s\" e o e-mail \"%s\" foram adicionados ao sistema.\n" %(nome,email))
    else:
        print("\033[1;31mAÇÃO CANCELADA.\033[0;0m")
    voltarMenu(listaPrincipal)

def escolha2(listaPrincipal):
    pass:

def escolha3(listaPrincipal):
    pass:

def escolha4(listaPrincipal):
    pass:

def escolha5(listaPrincipal):
    pass:

def escolha6(listaPrincipal):
    pass:

def main():
    listaPrincipal = []
    menuEscolhas( listaPrincipal)

main()