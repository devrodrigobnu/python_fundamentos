#  fazer 4 classes, 2 cada uma , no minimo 8 atributos  usar construtor getter setter e str, 
# nome das classes e atrbutos a gente escolhe


class Aluno:
    def __init__(self, nome, idade, media, situacao): #parametros de entrada
        #caracteristicas recebem os valores dos parametros
        self.__Nome : str        = nome
        self.__Idade : int       = idade
        self.__Media : float     = media
        self.__Situacao : str    = situacao

     
    @property
    def nome(self):
        return self.__Nome
    @nome.setter
    def nome(self, nome):
        self.__Nome = nome
     
    @property
    def idade(self):
        return self.__Idade
    @idade.setter
    def idade(self, idade):
        self.__Idade = idade
     
    @property
    def media(self):
        return self.__Media
    @media.setter
    def media(self, media):
        self.__Media = media
     
    @property
    def situacao(self):
        return self.__Situacao
    @situacao.setter
    def situacao(self, situacao):
        self.__Situacao = situacao



    def __str__(self):
        return f'{self.nome} {self.idade} {self.media} {self.situacao}'