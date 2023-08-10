# 4 - Classe Funcionário:
# Crie uma classe chamada Funcionario com os atributos 
# nome (private), salario (private) e cargo (public).
 
# Crie métodos para definir o nome (set_nome(novo_nome)), 
# obter o nome (get_nome()), calcular
# aumento de salário (aumentar_salario(aumento)) e exibir 
# informações completas do
# funcionário (exibir_informacoes()). Crie um construtor e 
# trabalhe a 
# manipulação da classe e dos dados via objetos.



# Classe
class Funcionario:
    # Construtor
    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.cargo = cargo

    # Getters
    def get_nome(self):
        return self.__nome
    
    # Setters
    def set_nome(self, novo_nome):
        print(f'Setou nome {self.__nome} para {novo_nome}')
        self.__nome = novo_nome

    def aumentar_salario(self, aumento):
        print(f'Aumentando salário de {self.__salario} para {self.__salario + aumento}')
        self.__salario += aumento

    # Exibindo infos
    def exibir_informacoes(self):
        print(f'Nome: {self.__nome}, Salário: {self.__salario}, Cargo: {self.cargo}')


if __name__ == '__main__':
    funcionario_1 = Funcionario('Rodrigo', 10000, 'Dev. Jr')
    funcionario_1.exibir_informacoes()
    funcionario_1.set_nome('Carlos')
    funcionario_1.aumentar_salario(25000)
    funcionario_1.exibir_informacoes()

    

