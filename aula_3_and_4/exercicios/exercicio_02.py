# 2 - Classe Livro:
# Crie uma classe chamada Livro que represente um livro.
# A classe deve ter os atributos titulo, autor e ano. 
# Crie um método para exibir as informações do livro 
# (exibir_informacoes()).
import os 

class Livro:
    titulo = 'A Song of Ice and Fire'
    autor = 'George R. R. Martin'
    ano = 1996

    def exibir_informações():
        print(f'\nInformações do livro:')
        print(f'Título: {Livro.titulo}')
        print(f'Autor: {Livro.autor}')
        print(f'Ano de Edição: {Livro.ano}')

    
if __name__ == '__main__':
    Livro.exibir_informações()