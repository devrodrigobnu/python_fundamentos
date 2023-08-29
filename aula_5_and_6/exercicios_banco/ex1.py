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
        return self.idade
    
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
    def criar_tabela(Alunos):
        cursor = Alunos.conexao.cursor()
        
        sql_string = f'''
            cursor.execute('INSERT INTO Alunos (nome, idade, nota) VALUES (?, ?, ?)', (nome, idade, nota))
        '''
        cursor.execute(sql_string)
        Alunos.conexao.commit()
        cursor.close()
        print(f'Tabela {Alunos} criada com sucesso!')

    @staticmethod
    def criar_aluno(nome, idade, nota):
        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO Alunos (nome, idade, nota) VALUES (?, ?, ?)', (nome, idade, nota))   
        conexao.commit()
        conexao.close()

    @staticmethod
    def buscar_aluno_por_id(id):
        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM Alunos WHERE id = ?', (id))
        resultado = cursor.fetchone()
        conexao.close()
        if resultado:
            return Alunos(*resultado)
        return None
    
    @staticmethod
    def listar_alunos():
        conexao = sqlite3.connect('escola.db')
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM Alunos')
        resultados = cursor.fetchall()
        conexao.close()
        alunos = [Alunos(*resultado) for resultado in resultados]
        return alunos


def main():
    while True:
        print("\nMenu:")
        print("1 - Criar Aluno")
        print("2 - Buscar Aluno por ID")
        print("3 - Listar Alunos")
        print("4 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            nota = float(input("Digite a nota do aluno: "))
            Alunos.criar_aluno(nome, idade, nota)
            print("Aluno criado com sucesso!")

        elif escolha == "2":
            id_busca = int(input("Digite o ID do aluno: "))
            aluno = Alunos.buscar_aluno_por_id(id_busca)
            if aluno:
                print(f"Detalhes do aluno:\nID: {aluno.get_id()}\nNome: {aluno.get_nome()}\nIdade: {aluno.get_idade()}\nNota: {aluno.get_nota()}")
            else:
                print("Aluno não encontrado.")

        elif escolha == "3":
            alunos = Alunos.listar_alunos()
            print("Lista de Alunos:")
            for aluno in alunos:
                print(f"ID: {aluno.get_id()}, Nome: {aluno.get_nome()}, Idade: {aluno.get_idade()}, Nota: {aluno.get_nota()}")

        elif escolha == "4":
            print("Encerrando a aplicação.")
            break

        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()