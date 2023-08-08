# 6 - Classe Aluno:
# Crie uma classe chamada Aluno que represente um aluno. 
# A classe deve ter os atributos nome, matricula e notas (uma lista de notas).
# Crie métodos para calcular a média (calcular_media()) 
# e exibir o status do aluno com base na média (exibir_status()).
import os

class Aluno:
    
    nome = 'Rodrigo'
    matricula = 123456
    lista_notas = []

    def obter_notas():
        quantidade = int(input('Digite a quantidade de notas: '))
        for i in range(quantidade):
            while True:
                try:
                    nota = float(input(f'Digite a nota {i + 1}: '))
                    if 0 <= nota <= 10:
                        Aluno.lista_notas.append(nota)
                        break
                    else:
                        raise ValueError('Informe uma nota entre 0 e 10')
                except Exception as e:
                    print(f'Ocorreu um erro: {str(e)}')
                    print('Digite um número válido!')

    def calcular_media():
        if Aluno.lista_notas:
            soma = sum(Aluno.lista_notas)
            media = soma / len(Aluno.lista_notas)
            return media
        else:
            return 0
    
    def exibir_status():
        media = Aluno.calcular_media()
        print(f'Média do aluno {Aluno.nome}: {media:.2f}')
        if media >= 6.0:
            print('Aluno aprovado!')
        else:
            print('Aluno reprovado')

if __name__ == '__main__':
    os.system('cls')
    aluno = Aluno()
    Aluno.obter_notas()
    Aluno.exibir_status()