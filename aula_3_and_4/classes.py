

class ClasseCachorro:
    raca = 'Pastor Alemão'
    idade = 5
    
    def latir(latidas):
        for latida in range(latidas):
            print('au au')
    def comer(comida, horario):
        print(f'au au, comi {comida}, au au em horario {horario}')
    
    def mostrar_info_dog():
        print(f'O cachorro é da raça {ClasseCachorro.raca} e tem {ClasseCachorro.idade} anos!')
        
class ClassePessoa:
    # atributos = variáveis
    nome = 'Rodrigo'
    idade = 32
    altura = 1.87
    peso = 91.0
    pais_origem = 'Brasil'
    genero = 'Masculino'

    # métodos - funções
    def dizer_ola():
        print(f'Olá, eu sou {ClassePessoa.nome}')

    def mostrar_dados():
        print(f'Eu tenho {ClassePessoa.idade} anos, {ClassePessoa.altura} de altura, {ClassePessoa.peso}kg e meu gênero é {ClassePessoa.genero}.')

    def mostrar_origem():
        print(f'Eu venho de/do/da {ClassePessoa.pais_origem}')

ClasseCachorro.latir(10)
ClasseCachorro.comer('raçao', '10:00')
ClasseCachorro.mostrar_info_dog()

ClassePessoa.dizer_ola()
ClassePessoa.mostrar_dados()
ClassePessoa.mostrar_origem()