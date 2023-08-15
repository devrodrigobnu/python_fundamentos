# 2 - Crie uma classe Banco com métodos abstratos depositar(), ver_saldo() e sacar() e 
# implemente a lógica de cada método. Crie subclasses ContaCorrente e ContaPoupanca
# que herdam da classe Banco e implementam os métodos de acordo com suas regras específicas.
# Por exemplo, a subclasse ContaPoupanca pode nao deter o método sacar().
# Crie atributos privados e publicos nas subclasses ContaCorrente e ContaPoupanca
# como self.nome, self.saldo, e self.numero_conta por exemplo. Crie objetos dessas
# classes com informações distintas, invoque os métodos e printe o resultado das
# operações. 

from abc import ABC, abstractmethod

# Classe Abastrata (modelo)
class Banco:
    def __init__(self, nome, saldo, conta):
        self.nome = nome
        self.saldo = saldo
        self.conta = conta

    @abstractmethod
    def depositar(self, valor):
        pass

    def ver_saldo(self):
        return self.saldo
    
    def sacar(self, valor):
        pass


# Subclasse
class ContaCorrente(Banco):
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de {valor}, feito com sucesso!')
        else:
            print('Valor insuficiente!')

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de {valor}, feito com sucesso!')
        else:
            print('Valor insuficiente!')

    

class ContaPoupanca(Banco):
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de {valor}, feito com sucesso!')
        else:
            print('Valor insuficiente!')

    def sacar(self, valor):
        print('Operação não permita para conta poupança')

if __name__ == '__main__':
    conta_1 = ContaCorrente(
        nome='Rodrigo',
        saldo=300,
        conta='123456'
    )

    conta_2 = ContaCorrente(
        nome='Felipe',
        saldo=400,
        conta='654321'
    )

    conta_1.depositar(500)
    saldo_atual = conta_1.ver_saldo()
    print(f'Saldo atual da conta 1: {saldo_atual}')

    conta_2.sacar(200)
    saldo_atual = conta_2.ver_saldo()
    print(f'Saldo atual da conta 2: {saldo_atual}')