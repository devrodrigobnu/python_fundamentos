# CLASSE MÃE
class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def correr(self):
        print(f'{self.nome} está correndo...')

    def comer(self):
        print(f'{self.nome} está se alimentando...')


# SUBCLASSE HERDANDO CLASSE ANIMAL
class Cachorro(Animal):
    def latir(self):
        print('Au au - I am a dog')
    
class Gato(Animal):
    def destruir_sofa(self):
        print('Seu sofá foi destruido')
    def miar(self):
        print('Miau Miau')

cao_1 = Cachorro('bryan', 'black')
cao_1.comer()
cao_1.correr()
cao_1.latir()
print('\n')
gato_1 = Gato('luna', 'branco')
gato_1.comer()
gato_1.correr()
gato_1.destruir_sofa()
gato_1.miar()


