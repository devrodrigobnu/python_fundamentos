from controller import criar_livro, listar_livro, atualizar_livro, deletar_livro


def menu():
    while True:
        print(
            "\nMenu: \n1-Adicionar Livro \n2-Listar Livro \n3-Atualizar Livro \n4-Deletar Livro \n5-Sair"
        )
        opcao = input("Escola uma opção: ")

        if opcao == "1":
            criar_livro()
        elif opcao == "2":
            listar_livro()
        elif opcao == "3":
            atualizar_livro()
        elif opcao == "4":
            deletar_livro()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
