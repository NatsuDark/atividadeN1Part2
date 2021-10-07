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
    print('''
    Você escolheu a opção de exibir todos os usuários cadastrados, listando-os por ordem de cadastro.
    Atualmente, temos cadastrados esses usuários:
    ''')
    for nomes in listaPrincipal[::2]:
        print(nomes)
    voltarMenu(listaPrincipal)

def escolha3(listaPrincipal):
    print('''
    Você escolheu a opção de exibir todos os usuários cadastrados, listando-os por ordem alfabética.
    Atualmente, temos cadastrados esses usuários:
    ''')
    listaNomesAlfabetico = sorted(listaPrincipal[::2])
    for nomes in listaNomesAlfabetico:
        print(nomes)
    voltarMenu(listaPrincipal)

def escolha4(listaPrincipal):
    print("Você escolheu a opção de verificar se um usuário faz parte da lista de participantes, buscando-o pelo seu nome.")
    nomeProcurado = input("insira o nome completo que deseja verificar:\n")
    nomeProcurado = nomeProcurado.title()
    if nomeProcurado in listaPrincipal:
        print("\033[1;92mO usuário procurado está na lista!\033[0;0m")
    else:
        print("\033[1;31mO usuário procurado não está na lista!\033[0;0m")
    voltarMenu(listaPrincipal)

def escolha5(listaPrincipal):
    print("Você escolheu a opção de remover um usuário cadastrado, buscando-o por seu email.")
    removerEmail = input("Digite o e-mail do usuário que deseja remover:\n")
    if removerEmail in listaPrincipal:
        contador = listaPrincipal.index(removerEmail)
        
        print("O nome \"%s\" e o e-mail \"%s\" serão removidos do sistema.\n" %(listaPrincipal[contador-1], listaPrincipal[contador]))
        if confirmarEscolha():
            print("O nome %s e o email %s foram removidos da lista." %(listaPrincipal.pop(contador-1),listaPrincipal.pop(contador-1)))
        else:
            print("\033[1;31mAÇÃO CANCELADA.\033[0;0m")
    else:
        print("\033[1;31mEsse e-mail não está no sistema!\033[0;0m")
    voltarMenu(listaPrincipal)

def escolha6(listaPrincipal):
    print("Você escolheu a opção de alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.")
    localizarEmail = input("Digite o e-mail do usuário que deseja alterar:\n")
    if localizarEmail in listaPrincipal:
        contador = listaPrincipal.index(localizarEmail)
        print("Encontramos o nome \"%s\" registrado com o e-mail dado." %listaPrincipal[contador-1])
        alterarNome = input("Insira o nome alterado do usuário:\n")
        alterarNome = alterarNome.title()

        print("O nome \"%s\" será alterado para \"%s\".\n"  %(listaPrincipal[contador-1],alterarNome))
        if confirmarEscolha():
            print("\033[1;92mO nome \"%s \"foi alterado para \"%s\".\033[0;0m" %(listaPrincipal[contador-1],alterarNome))
            listaPrincipal[contador-1] = alterarNome
        else:
            print("\033[1;31mAÇÃO CANCELADA.\033[0;0m")
    else:
        print("\033[1;31mEsse e-mail não está no sistema!\033[0;0m")
    voltarMenu(listaPrincipal)

def main():
    listaPrincipal = []
    menuEscolhas( listaPrincipal)

main()