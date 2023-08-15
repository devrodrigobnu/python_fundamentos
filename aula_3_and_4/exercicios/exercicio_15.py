# 15 - Classe Escola:
# Crie uma classe chamada Escola. Defina um atributo alunos como private 
# (uma lista vazia no construtor). Crie métodos para adicionar
# (adicionar_aluno(aluno)), remover (remover_aluno(aluno)) e exibir a 
# lista de alunos (exibir_alunos()).
# Crie um construtor e trabalhe a manipulação da classe e dos dados via objetos.



class Escola:
    def __init__ (self):
        self.alunos = []
        print('Objeto instanciado com sucesso.')

    
    def adicionar_aluno(self, nome_aluno):
        self.alunos.append(nome_aluno)
        print(f'O aluno {nome_aluno}, foi adicionado com sucesso!')

    
    def remover_aluno(self, nome_aluno):
        self.alunos.remove(nome_aluno)
        print(f'O aluno {nome_aluno}, foi removido com sucesso!')


    def exibir_alunos(self):
        print('Lista de aluno:')
        for aluno in self.alunos:
            print(aluno)


if __name__ == '__main__':
    minha_turma = Escola()
    minha_turma.adicionar_aluno('Rodrigo')

    minha_turma.remover_aluno('Rodrigo')
    
    minha_turma.exibir_alunos()