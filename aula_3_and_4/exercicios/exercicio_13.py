# 13 - Classe Livro com Construtor:
# Crie uma classe Livro com construtor que aceite os parâmetros titulo, autor e ano. Crie métodos get_titulo(), get_autor()
# e get_ano() para acessar esses atributos. 

# Classe
class Livro:
    # Construtor
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        print('Objeto instanciado com sucesso.')

    # Getter
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_ano(self):
        return self.ano
    
if __name__ == '__main__':
    livro_1 = Livro('titulo_1', 'autor_1', 1990)
    

    print(livro_1.titulo)
    print(livro_1.autor)
    print(livro_1.ano)