# 4 - Classe Agenda:
# Crie uma classe chamada Agenda que represente uma agenda de contatos. 
# A classe deve ter um atributo para armazenar uma lista de contatos.
# Crie métodos para adicionar (adicionar_contato(nome, telefone)), 
# remover (remover_contato(nome)), e exibir todos os contatos (exibir_contatos()).
import os 

class AgendaRodrigo:
    mensagem_input = '\n1 - Adicionar contatos'
    mensagem_input += '\n2 - Remover contatos'
    mensagem_input += '\n3 - Exibir contatos'
    mensagem_input += '\n4 - Sair'
    mensagem_input += '\nInforme a operação: '

    lista_contatos = []

    def adicionar_contato():
        nome = input('Digite o nome do contato: ')
        telefone = input('Digite o telefone do contato: ')
        AgendaRodrigo.lista_contatos.append({'Nome': nome, 'Telefone': telefone})
        print(f'Contato {nome}, adicionado com sucesso')
        
    def remover_contato():
        nome = input('Digite o nome do contato a ser removido: ')
        for contato in AgendaRodrigo.lista_contatos:
            if contato['Nome'] == nome:
                AgendaRodrigo.lista_contatos.remove(contato)
                print(f'Contato {nome} removido com sucesso!')
                break
    
    def exibir_contatos():
        for contato in AgendaRodrigo.lista_contatos:
            print(f'Nome: {contato["Nome"]}, Telefone: {contato["Telefone"]}')

    def script():
        while True:
            try:
                opcao = input(AgendaRodrigo.mensagem_input)
                if opcao == '1':
                    AgendaRodrigo.adicionar_contato()
                elif opcao == '2':
                    AgendaRodrigo.remover_contato()
                elif opcao == '3':
                    AgendaRodrigo.exibir_contatos()
                elif opcao == '4':
                    break
                else:
                    print('Opção inválida! Escolha opções entre 1 e 4!!')
            except ValueError: 
                print('Informe uma opção válida!')


        
if __name__ == '__main__':
    os.system('cls')
    AgendaRodrigo.script()