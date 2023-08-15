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
    def depositar(self):
        pass
    def ver_saldo(self):
        pass
    def sacar(self):
        pass

# Subclasse
class ContaCorrente(Banco):
    def sacar(self):
        ...
    def depositar(self):
        ...
    
class ContaPoupanca(Banco):
    def sacar(self):
        ...
    def depositar(self):
        ...




if __name__ == '__main__':
    ...