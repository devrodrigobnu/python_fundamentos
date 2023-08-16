# 4 - Crie uma classe abstrata Animal com um método emitir_som(). Crie subclasses Cachorro,
# Gato, Cavalo e Vaca que herdam de Animal e implementam seus próprios sons. Crie uma função
# que aceita uma lista de animais e faça-os emitir sons usando polimorfismo.
# Em seguida, crie contrutores para as subclasses dando um atributo nome e cor, e crie
# objetos dessas subclasses com cores e nomes distintos.
from abc import ABC, abstractmethod

class Animal:
    def __init__(self, nome, cor, idade):
        self.nome = nome
        self.cor = cor
        self.idade = idade

    @abstractmethod
    def emitir_som(self):
        pass
    def exibir_informacoes(self):
        pass
    
class Gato(Animal):
    def emitir_som(self):
        print('Miau, Miau!')

    def exibir_informacoes(self):
        print(f'O nome do gato é {self.nome} e a cor dele é {self.cor}')

class Cavalo(Animal):
    ...

class Vaca(Animal):
    ...


if __name__ == '__main__':
    gato_1 = Gato('Little Cat', 'Branca')
    gato_1.exibir_informacoes()
    gato_1.emitir_som()