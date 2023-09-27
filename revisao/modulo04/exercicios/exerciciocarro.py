#  fazer 4 classes, 2 cada uma , no minimo 8 atributos  usar construtor getter setter e str, 
# nome das classes e atrbutos a gente escolhe


class Carro:
    def __init__(self, marca, modelo, cor, placa): #parametros de entrada
        #caracteristicas recebem os valores dos parametros
        self.__Marca : str    = marca
        self.__Modelo : str   = modelo
        self.__Cor : str      = cor
        self.__Placa : str    = placa

     
    @property
    def marca(self):
        return self.__Marca
    @marca.setter
    def marca(self, marca):
        self.__Marca = marca
     
    @property
    def modelo(self):
        return self.__Modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__Modelo = modelo
     
    @property
    def cor(self):
        return self.__Cor
    @cor.setter
    def cor(self, cor):
        self.__Cor = cor
     
    @property
    def placa(self):
        return self.__Placa
    @placa.setter
    def placa(self, placa):
        self.__Placa = placa



    def __str__(self):
        return f'{self.marca} {self.modelo} {self.cor} {self.placa}'