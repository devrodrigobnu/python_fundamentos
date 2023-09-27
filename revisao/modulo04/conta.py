class Conta:
    __Numero = 123
    def __init__(self, titular, cpf, saldo, limite):
        self.__Titular    : str = titular
        self.__Cpf        : str = cpf
        self.__Saldo      : str = saldo
        self.__Limite     : str = limite

    @property
    def numero(self):
        return self.__Numero
    
    # getter
    @property
    def titular(self):
        return self.__Titular
    # setter
    @titular.setter
    def titular(self, titular):
        self.__Titular = titular
    
    @property
    def cpf(self):
        return self.__Cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__Cpf = cpf
    
    @property
    def saldo(self):
        return self.__Saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__Saldo = saldo
    
    @property
    def limite(self):
        return self.__Limite
    @limite.setter
    def limite(self, limite):
        self.__Limite = limite
    

        
   # final de uma classe - saída
    def __str__(self):
        return f'{self.numero} {self.titular} {self.cpf} {self.saldo} {self.limite}'