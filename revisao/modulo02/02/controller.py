def create(cliente):
    try:
        with open("pessoas.txt", "a") as arquivo:
            arquivo.write(f"{cliente}\n")
        print("Cliente adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar cliente: {str(e)}")


def read():
    nomes = []
    try:
        with open("pessoas.txt", "r") as arquivo:
            for name in arquivo:
                name = name.strip()
                nomes.append(name)
    except Exception as e:
        print(f"Erro ao ler clientes: {str(e)}")

    return nomes


def search(c):
    flag = False
    try:
        with open("pessoas.txt", "r") as arquivo:
            for line in arquivo:
                if c in line:
                    print(line)
                    flag = True

        if not flag:
            print("Cliente não encontrado!")
    except Exception as e:
        print(f"Erro ao pesquisar cliente: {str(e)}")


def update(cliente):
    try:
        flag = False
        with open("pessoas.txt", "r") as arquivo:
            lines = arquivo.readlines()

        with open("pessoas.txt", "w") as arquivo:
            for line in lines:
                if cliente in line:
                    novo_nome = input("Digite o novo nome: ")
                    nova_idade = input("Digite a nova idade: ")
                    nova_linha = f"nome: {novo_nome} idade : {nova_idade}\n"
                    arquivo.write(nova_linha)
                    flag = True
                else:
                    arquivo.write(line)

        if flag:
            print("Seu arquivo foi alterado com sucesso!")
        else:
            print("Cliente não encontrado!")
    except Exception as e:
        print(f"Erro ao atualizar cliente: {str(e)}")


def delete(pessoa):
    try:
        flag = False
        with open("pessoas.txt", "r") as arquivo:
            lines = arquivo.readlines()

        with open("pessoas.txt", "w") as arquivo:
            for line in lines:
                if pessoa not in line:
                    arquivo.write(line)
                else:
                    flag = True

        if flag:
            print("Cliente deletado com sucesso")
        else:
            print("Cliente não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar cliente: {str(e)}")
