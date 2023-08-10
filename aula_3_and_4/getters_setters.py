
class Animal:
    # CONSTRUTOR
    def __init__(self, raca, cor, idade, nome):
        self._raca = raca # protected
        self._cor = cor # protected
        self._idade = idade # protected
        self.__nome = nome # private
        print('Objeto instanciado com sucesso.')

    # PRIVATE -> __nome
    # PROTECTED -> _nome
    # PUBLIC -> nome


    # GETTERS com @property
    @property
    def raca(self):
        return 'Raça -> ' + self._raca
    
    @property
    def cor(self):
        return 'Cor -> ' + self._cor
    
    @property
    def idade(self):
        return f'Idade -> {self._idade}'
    
    @property
    def nome(self):
        return self.__nome
        


    # SETTERS com variavel.setter
    @raca.setter
    def raca(self, raca_nova):
        print(f'Setou {self.raca} para {raca_nova}')
        self._raca = raca_nova

    @cor.setter
    def cor(self, cor_nova):
        print(f'Setou {self.cor} para {cor_nova}')
        self._cor = cor_nova

    @idade.setter
    def idade(self, idade_nova):
        print(f'Setou {self.idade} para {idade_nova}')
        self._idade = idade_nova
        
    @nome.setter
    def nome(self, nome_novo):
        print(f'Setou nome {self.__nome} para {nome_novo}')
        self.__nome = nome_novo


if __name__ == '__main__':
    # INSTANCIAS (CRIACOES) DOS OBJETOS DA CLASSE ANIMAL
    leao = Animal('Leão da montanha', 'Bege', 15, 'simba')
    gato = Animal('siamês', 'preto', 11, 'tommy')
    pantera = Animal('pantera negra', 'preto', 19, 'king')
    # UTILIZAR GETTERS PARA CADA OBJETO
    print(leao.raca)
    print(leao.cor)
    print(leao.idade)

    print(gato.raca)
    print(gato.cor)
    print(gato.idade)

    print(pantera.raca)
    print(pantera.cor)
    print(pantera.idade)

    # UTILIZA SETTERS
    pantera.idade = 56
    print(pantera.idade)
    pantera.cor = 'branca'
    print(pantera.cor)

    gato.raca = 'persa'
    print(gato.raca)

    print(pantera.nome)
    print(leao.nome)
    print(gato.nome)
    
















# while True:
#     try:
#         metodo = input('Informe o (s para sair): ')

#         if metodo.lower() == 'get_raca':
#             print(Animal.get_raca())

#         elif metodo.lower() == 'get_cor':
#             print(Animal.get_cor())

#         elif metodo.lower() == 'get_idade':
#             print(Animal.get_idade())

#         elif metodo.lower() == 'set_raca':
#             raca = input('Informe a raça: ')
#             Animal.set_raca(raca)

#         elif metodo.lower() == 'set_cor':
#             cor = input('informe a cor: ')
#             Animal.set_cor(cor)

#         elif metodo.lower() == 'set_idade':
#             idade = input('Informe a idade: ')
#             Animal.set_idade(idade)
        
#         elif metodo == 's':
#             print('Parou!')
#             break

#     except Exception as erro:
#         print(f'Ocorreu um erro: {erro}')
