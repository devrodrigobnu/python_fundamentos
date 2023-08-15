# 17 - Classe Hotel com Getters e Setters e construtor:
# Crie uma classe chamada Hotel. Defina um atributo nome (private) e estrelas (public). Crie métodos get_nome(), 
# set_nome(novo_nome) e get_estrelas()
# para acessar e modificar esses atributos.

class Hotel:
    
    def __init__(self, nome, estrelas):
        self.__nome = nome
        self.estrelas = estrelas
    
    @property
    def nome(self):
        return self.__nome

    def get_estrelas(self):
        ...

    def set_nome(self, novo_nome):
        ...

if __name__ == '__main__':
    ...