# 9 - Classe Pessoa:
# Crie uma classe chamada Pessoa com o atributo nome (public). 
# Implemente métodos set_nome(novo_nome) e get_nome() para manipular esse atributo.


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def get_nome(self):
        return self.nome
        
if __name__ == '__main__':

    pessoa = Pessoa('João')
    print(pessoa.get_nome()) 

    pessoa.set_nome('Mr_Robot')
    print(pessoa.get_nome())