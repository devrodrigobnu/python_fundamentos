# 7 - Classe Banco:
# Crie uma classe chamada Banco que represente um banco. 
# A classe deve ter atributos para armazenar uma lista de 
# contas bancárias.
# Crie métodos para adicionar (criar_conta(titular, 
# saldo_inicial)), 
# remover (encerrar_conta(numero)), exibir o total 
#  de saldo de 
# todas as contas (total_saldo()).
import os

class Banco:
    mensagem_input = '\n1 - Criar conta'
    mensagem_input += '\n2 - Encerrar conta'
    mensagem_input += '\n3 - Exibir saldo de todas as contas'
    mensagem_input += '\n4 - Sair'
    mensagem_input += '\nInforme a operação: '

    lista_contas = []

    def criar_conta():
        try:
            titular = input('Digite o nome do titular: ')
            saldo_inicial = float(input('Digite o saldo inicial da conta: '))
            nova_conta = {'titular': titular, 'saldo': saldo_inicial }
            Banco.lista_contas.append(nova_conta)
            print('Conta criada com sucesso!')
        except ValueError:
            print('Entrada inválida!')

    def encerrar_conta():
        ...


    def exibir_total_contas():
        ...

    def script():
        while True:
            try:
                opcao = input(Banco.mensagem_input)
                if opcao == '1':
                    Banco.criar_conta()
                elif opcao == '2':
                    Banco.encerrar_conta()
                elif opcao == '3':
                    Banco.exibir_total_contas()
                elif opcao == '4':
                    break
                else:
                    print('Opcão inválida! escolha opções entre 1 e 4!')
            except ValueError:
                print('Informe uma opção válida!')            
                

if __name__ == '__main__':
    os.system('cls')
    Banco.script()
