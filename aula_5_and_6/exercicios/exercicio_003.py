# 3 - Crie uma classe base Veiculo com atributos como marca, modelo e métodos como ligar()
# e desligar(), entre outros. Crie as subclasses Carro e Moto que herdam de Veiculo e
# implementam seus próprios métodos beaseando-se na abstratação de Veiculo. Em seguida,
# crie uma classe Garagem que aceita veículos e gerencia o estacionamento usando herança.
# Crie e trabalhe com os getters e setters para a classe Garagem.

class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = False

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'{self.marca}{self.modelo}, ligado com sucesso!')
        else:
            print('Veículo encontra-se desligado')
            
    def desligar():
        ...

class Carro(Veiculo):
    ...

class Moto(Veiculo):
    ...