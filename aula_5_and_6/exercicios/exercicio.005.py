
# 5 - Crie uma classe Alimento com atributos como nome e calorias. Crie subclasses Fruta, Legume
# e Carne que herdam de Alimento e implementam seus próprios atributos. Crie uma função que aceita 
# uma lista de alimentos e calcula o total de calorias usando polimorfismo. Para mais precisão no
# exercício, é ideal pesquisar as calorias dos alimentos e criar objetos das subclasses com seus 
# respectivos construtores e atributos.

from abc import ABC, abstractmethod

class Alimento(ABC):
    def __init__(self, calorias, nome):
        self.calorias = calorias
        self.nome = nome


class Fruta(Alimento):
    ...

class Legume(Alimento):
    ...

class Carne(Alimento):
    ...




def calcula_calorias(lista_calorias):
    soma_calorias = 0
    for caloria in lista_calorias:
        soma_calorias += caloria
    return soma_calorias






if __name__ == '__main__':
    cenoura = Legume(5, 'Cenoura')
    vagem = Legume(10, 'Vagem')
    beterraba = Legume(20, 'Beterraba')

    lista_legumes = [
        cenoura.calorias,
        vagem.calorias,
        beterraba.calorias
    ]
    caloria_total_legumes = calcula_calorias(lista_legumes)
    print(f'A soma de calorias de {cenoura.nome},', end='')
    print(f' {vagem.nome} e {beterraba.nome}', end='')
    print(f' é: {caloria_total_legumes}')



    frango = Carne(100, 'Filé de frango')
    bife = Carne(150, 'Patinho')
    picanha = Carne(200, 'Picanha')
    lista_carnes = [
        frango.calorias,
        bife.calorias,
        picanha.calorias,
    ] 
    caloria_total_carnes = calcula_calorias(lista_carnes)
    print(f'A soma de calorias de {frango.nome},', end='')
    print(f' {bife.nome} e {picanha.nome}', end='')
    print(f' é: {caloria_total_carnes}')



    banana = Fruta(50, 'Banana')
    melancia = Fruta(20, 'Melancia')
    maracuja = Fruta(60, 'Maracujá')
    lista_frutas = [
        banana.calorias,
        melancia.calorias,
        maracuja.calorias
    ]
    caloria_total_frutas = calcula_calorias(lista_frutas)
    print(f'A soma de calorias de {banana.nome},', end='')
    print(f' {melancia.nome} e {maracuja.nome}', end='')
    print(f' é: {caloria_total_frutas}')
