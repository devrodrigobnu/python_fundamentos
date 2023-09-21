from controller import create, read, search, update, delete


def menu():
    cond = "sim"
    while cond.lower() == "sim":
        var = int(
            input(
                "\n1-Create \n2-Read \n3-Search \n4-Update \n5-Delete \nOpção escolhida: "
            )
        )
        match var:
            case 1:
                pessoa = {}
                pessoa["Nome"] = input("Digite seu nome: ")
                pessoa["cpf"] = input("Digite seu CPF: ")
                pessoa["idade"] = int(input("Digite sua idade: "))
                pessoa["telefone"] = input("Digite seu telefone: ")
                create(pessoa)
            case 2:
                print(read())
            case 3:
                search(input("Digite o nome para listar: "))
            case 4:
                update(input("Digite o nome a ser atualizado: "))
            case 5:
                delete(input("Digite nome a ser deletado: "))
        cond = input("Deseja continuar? \nSim \nNão \nOpção escolhida: ").lower()


menu()
