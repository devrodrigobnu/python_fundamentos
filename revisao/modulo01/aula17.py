from time import sleep

situacao = 'Reprovado'

while situacao == 'Reprovado':
#1 Bloco
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite seu sobrenome: ')
    idade = int(input('Digite sua idade: '))
#2 Bloco
    lista_notas = []
    for lista in range(4):
        nota = float(input('Digite sua nota: '))
        lista_notas.append(nota)
    media = sum(lista_notas) / len(lista_notas)
#3 Bloco
    if media < 7:
        situacao = 'Reprovado'
        print(f'Infelizmente você {situacao} com a media de {media}')

    if media >= 7:
        for c in range(0,5):
            print('*')
            sleep(1.5)
            situacao = 'Aprovado'
        print(f'Parabéns, você foi {situacao} com a média {media}')
#4 Bloco
    dicionario = {
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Idade": idade,
        "Lista_notas": lista_notas,
        "Media": media,
        "Situacao": situacao
    }
#5 Bloco
    var = input('Você deseja saber um relatório completo sobre o aluno? \n1-Sim \n2-Não \nOpção: ')
    if var == "sim":
        print(f'''\n{dicionario['Nome']} 
        \n{dicionario['Sobrenome']}
        \n{dicionario['Idade']}
        \n{dicionario['Lista_notas']}
        \n{dicionario['Media']}
        \n{dicionario['Situacao']}
''')



    
