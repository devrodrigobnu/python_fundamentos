# 1 - Classe Conta Bancária:
# Crie uma classe chamada ContaBancaria que simule uma conta bancária simples.
# A classe deve ter os atributos titular, saldo e numero. 
# Crie métodos para depositar (depositar(valor))
# e sacar (sacar(valor)) dinheiro da conta, além de um método para
# exibir o saldo atual (exibir_saldo()).

class ContaBancaria:
    mensagem_input = '\nInforme 1 para depositar'
    mensagem_input += '\nInforme 2 para sacar'
    mensagem_input += '\nInforme 3 para exibir saldo'
    mensagem_input += '\nInforme 4 para sair'
    mensagem_input += '\ninforme a operação: '
   
    titular_conta = 'Rodrigo'
    saldo_conta = 0
    numero_conta = 182

    def depositar(valor):
        try:
            valor = float(valor)
            ContaBancaria.saldo_conta += valor
        except:
            print('Informe um valor válido para depósito!')

    def sacar(valor):
        try:
            valor = float(valor)
            ContaBancaria.saldo_conta -= valor
        except:
            print('Informe um valor válido para sacar!')

    def exibir():
        print(f'\nTitular {ContaBancaria.titular_conta} com número de conta {ContaBancaria.numero_conta} tem saldo {ContaBancaria.saldo_conta}.')

    def script():
        while True:
            try:
                opcao = input(ContaBancaria.mensagem_input)
                if opcao == '1':
                    valor = input('Informe o valor: ')
                    ContaBancaria.depositar(valor)
                elif opcao == '2':
                    valor = input('Informe o valor: ')
                    ContaBancaria.sacar(valor)
                elif opcao == '3':
                    ContaBancaria.exibir()
                elif opcao == '4':
                    print('Volte sempre com dinheiro!!')
                    break
            except:
                print('Informe uma opção válida!!')
    
if __name__ == '__main__':
    ContaBancaria.script()