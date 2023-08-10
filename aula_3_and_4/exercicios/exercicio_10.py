# 10 - Classe Conta Bancária:
# Crie uma classe chamada ContaBancaria, com os atributos saldo (private), 
# titular (public), numero_conta (private). 
# Crie métodos get_saldo() e set_saldo(novo_saldo) para acessar e modificar o saldo.


class ContaBancaria:
    def __init__(self, saldo, titular, numero_conta):
        self.__saldo = saldo
        self.titular = titular
        self.numero_conta = numero_conta

    
    def get_saldo(self):
        return self.__saldo


    
    def set_saldo(self, novo_saldo):
        print(f'Setou saldo {self.__saldo} para {novo_saldo}')

if __name__ == '__main__':
    conta = ContaBancaria(1000, 'rodrigo', '123456')
    print(conta.get_saldo())

    conta.set_saldo(2000)
    