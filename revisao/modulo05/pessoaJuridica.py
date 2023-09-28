from conta import Conta
class PessoaJuridica(Conta):
    __Segundo_titular = ''
    def __init__(self, titular, cnpj, saldo):
        super().__init__(1609, 'Pessoa Jurídica')
        self.__Titular = titular
        self.__Cnpj = cnpj
        self.__Saldo = saldo


    @property
    def Segundo_Titular(self):
        return self.__Segundo_titular
    @Segundo_Titular.setter
    def Segundo_Titular(self, segundo_titular):
        self.__Segundo_titular = segundo_titular

    @property
    def titular(self):
        return self.__Titular
    @titular.setter
    def titular(self, titular):
        self.__Titular = titular

    @property
    def cnpj(self):
        return self.__Cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__Cnpj = cnpj

    @property
    def saldo(self):
        return self.__Saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__Saldo = saldo


    def __str__(self):
        return f'{super().__str__()} \nPrimeiro Titular {self.titular}\nCPNJ: {self.cnpj}\nSaldo: {self.saldo}\nSegundo Titular: {self.Segundo_Titular}'
