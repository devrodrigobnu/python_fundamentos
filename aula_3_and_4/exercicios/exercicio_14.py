# 7 - Classe Veículo:
# Crie uma classe chamada Veiculo com os atributos 
# marca (private), modelo (private) e ano (private). 
# Crie um construtor para inicializar 
# esses atributos. Implemente métodos get_marca(), get_modelo() e 
# exibir_informacoes().

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

        
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_ano(self):
        return self.__ano
    
    def exibir_informacoes(self):
        print(f'Marca: {self.__marca}')
        print(f'Modelo: {self.__modelo}')
        print(f'Ano: {self.__ano}')


if __name__ == '__main__':
    veiculo_1 = Veiculo('Citroen C3', 'Tendance', 2014)
    veiculo_1.exibir_informacoes()