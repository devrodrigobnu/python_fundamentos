# 10 - Classe Conta Bancária:
# Crie uma classe chamada ContaBancaria, com os atributos saldo (private), 
# titular (public), numero_conta (private). 
# Crie métodos get_saldo() e set_saldo(novo_saldo) para acessar e modificar o saldo.


class ContaBancaria:
    def __init__(self, saldo, titular, numero_conta):
        self.__saldo = saldo
        self.__numero_conta = numero_conta
        self.titular = titular

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo
if __name__ == '__main__':
    conta_1 = ContaBancaria(100, 'bruno', '15')
    conta_2 = ContaBancaria(200, 'bruna', '16')

    print(conta_1.titular)
    print(f'Saldo: {conta_1.saldo}')

    print(conta_2.titular)
    print(f'Saldo: {conta_2.saldo}')

    print('\n')

    conta_1.saldo = 500
    conta_2.saldo = 600
    print(f'Saldo: {conta_1.saldo}')
    print(f'Saldo: {conta_2.saldo}')
    