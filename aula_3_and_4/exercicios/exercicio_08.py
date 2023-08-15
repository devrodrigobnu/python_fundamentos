# 8 - Classe Produto:
# Crie uma classe chamada Produto que represente um produto em uma loja. 
# A classe deve ter os atributos: nome (private), preco
# e codigo (public). Crie um construtor para inicializar esses atributos e 
# métodos get_nome(), get_preco() e set_preco(novo_preco) para
# acessar e modificar o preço."

class Produto:
    #CONSTRUTOR
    def __init__(self, nome, preco, codigo):
        self.__nome = nome
        self.preco = preco
        self.codigo = codigo
        

    #GETTERS
    @property
    def nome(self):
        return self.__nome
    
    
    def get_preco(self):
        return self.preco
    
    # SETTERS
    def set_preco (self, preco_novo):
        print(f'\nSetou {self.preco} para {preco_novo}')
        self.preco = preco_novo


if __name__ == '__main__':

    #INSTANCIAS
    produto_1 = Produto('Citroen C3', 2000, 'Tendance')
    produto_2 = Produto('Peugeot 307', 3000, 'Sedan Pressence ')   
    produto_3 = Produto('Amarok', 4000, 'Highline CD 4 Motion')
  
    # UTILIZAR SETTERS
    produto_1.set_preco(1500)
    print(produto_1.get_preco())

    produto_2.set_preco(1400)
    print(produto_2.get_preco())

    produto_3.set_preco(1500)
    print(produto_3.get_preco())