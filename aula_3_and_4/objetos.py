class Pessoa:
    nome = 'rodrigo'
    idade = 32
    origem = 'Brasil'

    def dizer_ola(self):
        print(f'Olá, eu sou {Pessoa.nome}.')

    def pensar(self):
        print('Eu estou pensando.')

    def comprar(self):
        print('Compra realizada.')

    # getter para buscar nome
    def get_nome(self):
        return Pessoa.nome
    

    # getter para buscar idade
    def get_idade(self):
        return Pessoa.idade
    

    # setter para setar o nome
    def set_nome(self, nome_novo):
        Pessoa.nome = nome_novo

    # setter para setar o idade
    def set_idade(self, idade_nova):
        Pessoa.idade = idade_nova



# Instanciando objetos
pessoa_1 = Pessoa()
pessoa_2 = Pessoa()
# Chamando metodos da classe Pessoa
pessoa_1.comprar()
pessoa_2.comprar
pessoa_1.pensar()
pessoa_2.pensar()
# Chamando os getters
print(pessoa_1.get_nome())
print(pessoa_1.get_idade())
# Utilizando os setters
pessoa_1.set_nome('rodriguera')
print(pessoa_1.get_nome())
pessoa_2.set_idade(26)
print(pessoa_2.get_idade())