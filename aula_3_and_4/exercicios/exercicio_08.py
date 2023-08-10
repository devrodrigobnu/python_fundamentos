# 1 - Classe Produto:
# Crie uma classe chamada Produto que represente um produto em uma loja. 
# A classe deve ter os atributos: nome (private), preco
# e codigo (public). Crie um construtor para inicializar esses atributos e 
# métodos get_nome(), get_preco() e set_preco(novo_preco) para
# acessar e modificar o preço."

class Produto:
    #CONSTRUTOR
    def __init__(self, nome, preco, codigo):
        self.__nome = nome
        self._preco = preco
        self.codigo = codigo
        print('Objeto instanciado com sucesso.')

    #GETTERS
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self._preco
    
    # SETTERS
    @preco.setter
    def preco (self, preco_novo):
        print(f'\nSetou {self._preco} para {preco_novo}')
        self._preco = preco_novo


if __name__ == '__main__':

    #INSTANCIAS
    produto_1 = Produto('Citroen C3', 38.900, 'Tendance')
    produto_2 = Produto('Peugeot 307', 54.900, 'Sedan Pressence ')   
    produto_3 = Produto('Amarok', 189.900, 'Highline CD 4 Motion')
    
    # UTILIZAR SETTERS
    produto_1.preco = 41.900
    print(f'Produto 1 - Preço: {produto_1.preco:.3f}')

    produto_2.preco = 56.900
    print(f'Produto 2 - Preço: {produto_2.preco:.3f}')

    produto_2.preco = 191.900
    print(f'Produto 3 - Preço: {produto_3.preco:.3f}')