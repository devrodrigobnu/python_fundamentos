# 3 - Crie uma classe base Veiculo com atributos como marca, modelo e métodos como ligar()
# e desligar(), entre outros. Crie as subclasses Carro e Moto que herdam de Veiculo e
# implementam seus próprios métodos beaseando-se na abstratação de Veiculo. Em seguida,
# crie uma classe Garagem que aceita veículos e gerencia o estacionamento usando herança.
# Crie e trabalhe com os getters e setters para a classe Garagem.
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ligado):
        self.marca = marca
        self.modelo = modelo
        self.ligado = ligado
    
    @abstractmethod
    def ligar():
        pass
    @abstractmethod
    def desligar():
        pass
    @abstractmethod
    def exibir_informações():
        pass

class Carro(Veiculo):
    def ligar(self):
        if self.ligado == True:
            print('O carro já está ligado!')
        else:
            self.ligado = True
            print('Carro ligado com sucesso!')

    def desligar(self):
        if self.ligado == False:
            print('O carro já está desligado')
        else:
            self.ligado = False
            print('Carro desligado com sucesso!')    

    def exibir_informações(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo} ')


class Moto(Veiculo):
    def ligar(self):
        if self.ligado == True:
            print('A moto já está ligada!')
        else:
            self.ligado = True
            print('Moto ligada com sucesso!')

    def desligar(self):
        if self.ligado == False:
            print('a moto já está desligada!')
        else:
            self.ligado = False
            print('Moto desligada com sucesso!') 

    def exibir_informações(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo} ')

    

    
class Garagem():
    def __init__(self):
        self.veiculos_estacionados = []
    
    def estacionar(self, auto_nome):
        self.veiculos_estacionados.append(auto_nome)
        print(f'{auto_nome} estacionado com sucesso')

    def mostra_carros_estacionados(self):
        if len(self.veiculos_estacionados) > 0:
            print('GARAGEM: ')
            for indice, veiculo in enumerate(self.veiculos_estacionados):
                print(f'Veiculo {indice + 1}: {veiculo}')   
        else:
            print('Ainda não existem veículos na garagem!')


if __name__ == '__main__':
    carro_1 = Carro('Toyota', 'Corolla', False)
    carro_1.exibir_informações()
    carro_1.ligar()
    carro_1.desligar()
    print('--------------------------------------------------------------')
    moto_1 = Moto('Honda', 'CBR', False)
    moto_1.exibir_informações()
    moto_1.ligar()
    moto_1.desligar()
    print('--------------------------------------------------------------')
    garagem_objeto = Garagem()
    garagem_objeto.mostra_carros_estacionados()

    garagem_objeto.estacionar(f'Carro da mãe - {carro_1.marca}')
    garagem_objeto.estacionar(f'Moto do pai - {moto_1.marca}')



