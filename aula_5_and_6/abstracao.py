from abc import ABC, abstractmethod

class PessoaAbstrata(ABC):
    @abstractmethod
    def gastar_dinheiro():
        pass

    @abstractmethod
    def respirar():
        pass

    @abstractmethod
    def falar():
        pass


class Atleta(PessoaAbstrata):
    def gastar_dinheiro():
        print('Eu gasto pouco dinheiro!')
    def falar():
        print('Queremos um aumento!')
    def respirar():
        print('Estou respirando profudamente!')

class Artista(PessoaAbstrata):
    def gastar_dinheiro():
        print('Eu gasto muito dinheiro!')
    def falar():
        print('Sou rico demais!')
    def respirar():
        print('Eu sou pago até pra respirar!')

Artista.gastar_dinheiro()
Atleta.gastar_dinheiro()
print('\n')
Artista.falar()
Atleta.falar()
print('\n')
Artista.respirar()
Atleta.respirar()

