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
        self.__saldo = saldo
        self.conta = conta

    @abstractmethod
    def depositar(self, valor):
        pass
    def ver_saldo(self):
        pass
    def sacar(self, valor):
        pass

# Subclasse
class ContaCorrente(Banco):
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de {valor} realizado.')
        else:
            print('Saldo insuficiente!')

    def depositar(self):
        ...
    def exibir_saldo(self):
        ...
    
class ContaPoupanca(Banco):
    def sacar(self):
        ...
    def depositar(self):
        ...




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