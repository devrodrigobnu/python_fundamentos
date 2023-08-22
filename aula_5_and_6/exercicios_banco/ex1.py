# 1 - Neste exercício, você vai criar uma aplicação de gerenciamento de alunos usando SQLite3 e programação orientada
# a objetos (POO) em Python. A aplicação permitirá criar, visualizar, atualizar e excluir registros de alunos em uma
# tabela chamada Alunos no banco de dados. Utilize a biblioteca sqlite3 para criar um banco de dados chamado escola.db.

# Crie uma tabela chamada Alunos com os seguintes campos: id, nome, idade e nota. Crie uma classe chamada Aluno.
# Crie os atributos id, nome, idade e nota na classe. Implemente o construtor __init__() para receber os valores dos atributos.
# Crie métodos de getters (get_id(), get_nome(), get_idade(), get_nota()) para acessar os valores dos atributos.
# Crie métodos de setters (set_nome(), set_idade(), set_nota()) para definir os valores dos atributos.
# Crie um método estático na classe Aluno chamado criar_aluno() que aceita os valores de nome, idade e nota como parâmetros.
# Este método deve criar uma instância da classe Aluno com os valores passados e inserir um registro na tabela Alunos com esses valores.
# Crie um método estático chamado buscar_aluno_por_id() que aceita um ID como parâmetro e retorna uma instância de Aluno com os valores
# correspondentes da tabela Alunos. Crie um método estático chamado listar_alunos() que consulta a tabela Alunos e retorna uma lista de
# instâncias de Aluno. Crie um loop principal que exibe um menu para o usuário com opções como "Criar Aluno", "Buscar Aluno por ID", "Listar Alunos"
# e "Sair". Implemente a lógica para cada opção do menu, chamando os métodos correspondentes da classe Aluno. Na opção "Criar Aluno", solicite ao
# usuário que insira nome, idade e nota e, em seguida, chame o método criar_aluno(). Na opção "Buscar Aluno por ID", peça ao usuário para inserir
# um ID e exiba os detalhes do aluno correspondente usando o método buscar_aluno_por_id(). Na opção "Listar Alunos", liste todos os alunos usando o
# método listar_alunos(). Ao sair do loop principal, feche a conexão com o banco de dados.

import sqlite3
import os

class Alunos:
    def __init__(self, id, nome, idade, nota):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.nota =  nota

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome
    
    def get_idade(self):
        return self.nome
    
    def get_nota(self):
        return self.nota
    
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_idade(self, nova_idade):
        self.idade = nova_idade

    def set_nota(self, nota_nova):
        self.nota = nota_nova

    @staticmethod
    def criar_conexao(nome_base):
        Alunos.conexao = sqlite3.connect(nome_base)
        print('Conexão estabelecida com sucesso.')
        return Alunos.conexao

    @staticmethod
    def criar_tabela(nome_tabela_nova):
        cursor = Alunos.conexao.cursor()
        pass
    

def database_manager():
    conn = Alunos.criar_conexao('escola.db')

    menu_interface = '''
1 - 