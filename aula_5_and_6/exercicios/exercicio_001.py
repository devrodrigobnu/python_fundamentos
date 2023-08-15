# 1 - Crie uma classe abstrata chamada Animal com métodos emitir_som()), comer() e mover().
# Crie subclasses Cachorro, Cavalo e Gato que herdam da classe Animal e implementam
# seus próprios métodos, printando frases diferentes.  
# Crie e trabalhe com os getters e setters para as subclasses.
from abc import ABC, abstractmethod



# CLASSE ABSTRATA (MODELO)
class Animal:
    def __init__(self, especie, idade, peso, cor):
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.cor = cor

    @abstractmethod
    def emitir_som(self):
        pass
    def comer(self):
        pass
    def mover(self):
        pass
    def exibir_informacoes(self):
        pass


# SUBCLASSE
class Cachorro(Animal):
    def emitir_som(self):
        print('Au au')
    def comer(self):
        print('O cachorro comeu a ração!')
    def mover(self):
        print('O cachorro se moveu!')
    def exibir_informacoes(self):
        print(f'Espécie {self.especie}')

class Cavalo(Animal):
    def emitir_som(self):
        print('Relincho: Neighhhhhh!')
    def comer(self):
        print('O cavalo comeu o pasto!')
    def mover(self):
        print('O cavalo se moveu para as montanhas!')
    def exibir_informacoes(self):
        print(f'Espécie {self.especie}')

class Gato(Animal):
    def emitir_som(self):
        print('Miau Miau')
    def comer(self):
        print('O gato comeu o peixe!')
    def mover(self):
        print('O gato se moveu para o telhado!')
    def exibir_informacoes(self):
        print(f'Espécie {self.especie}') 

if __name__ == '__main__':
    cavalo_1 = Cavalo(
        especie='Machador',
        idade=10,
        peso=155.50,
        cor='Marrom'
    )
    cavalo_2 = Cavalo(
        especie='Machador',
        idade=12,
        peso=160.50,
        cor='Preto'
    )
    gato_objeto = Gato(
        especie='Siamês',
        idade=6,
        peso=2.5,
        cor='Laranja'
    )
    cachorro_objeto = Cachorro(
        especie='Labrador',
        idade=8,
        peso=22,
        cor='Branco'
    )
cavalo_1.exibir_informacoes()
cavalo_1.emitir_som()
cavalo_1.mover()
cavalo_1.comer()
print('-------------------------------------------------------------------')
cavalo_2.exibir_informacoes()
cavalo_2.emitir_som()
cavalo_2.mover()
cavalo_2.comer()
print('-------------------------------------------------------------------')
gato_objeto.exibir_informacoes()
gato_objeto.emitir_som()
gato_objeto.mover()
gato_objeto.comer()
print('-------------------------------------------------------------------')
cachorro_objeto.exibir_informacoes()
cachorro_objeto.emitir_som()
cachorro_objeto.mover()
cachorro_objeto.comer()