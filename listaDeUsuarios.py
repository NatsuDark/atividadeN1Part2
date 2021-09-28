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



def main():
    listaPrincipal = []
    menuEscolhas( listaPrincipal)

main()