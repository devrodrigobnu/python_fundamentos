# Realizando importações de bibioletas
# por padrão, elas serão importadas no começo
# dos arquivos/programas .py
import os
import time
# .system serve para enviar comandos para o terminal
# entre outras funções ...
os.system('cls')
os.system('python --version')
# O taskkill serve para parar o arquivo executável
# responsável por rodar uma aplicação ou sistema
# os.system('taskkill /f /im chrome.exe')

# suicidio cmd
# os.system('taskkill /f /im cmd.exe')

# tipos de dados em python
numero_inteiro_1: int = 5
numero_inteiro_2: int = 5500
numero_inteiro_3: int = 100
print(f'\nDados das variáveis do tipo int: {numero_inteiro_1}, {numero_inteiro_2}, {numero_inteiro_3} ')

nome: str = 'Rodrigo'
sobrenome: str = 'Luchtenberg'
texto_aleatorio: str = 'Hahahaha'
print(f'\nDados das variáveis do tipo str: {nome}, {sobrenome}, {texto_aleatorio}')

salario_dev: float = 1.545
nota_aluno: float = 7.5
temperatura: float = 33.9
print(f'\nDados das variáveis do tipo float: {salario_dev}, {nota_aluno}, {temperatura}')
print(f'Arredondando a variável salario_dev: {round(salario_dev, 2)}')

tipo_verdade: bool = True
tipo_falso: bool = False
numero_1_eh_maior_que_numero_2: bool = numero_inteiro_1 > numero_inteiro_2
print(f'\nDados das variáveis do tipo bool: {tipo_verdade}, {tipo_falso}, {numero_1_eh_maior_que_numero_2}')

# Criando uma lista com os dados das variáveis
lista_de_dados: list = [
    numero_inteiro_1, # 1
    numero_inteiro_2, # 2
    numero_inteiro_3, # 3
    nome,             # 4
    sobrenome,        # 5
    texto_aleatorio,  # 6
    salario_dev,      # 7
    nota_aluno,       # 8
    temperatura,      # 9
    tipo_verdade,     # 10
    tipo_falso,       # 11
    numero_1_eh_maior_que_numero_2 # 12
]

print(f'\nMostrando o dado da posição 0: {lista_de_dados[0]}')
print(f'\nMostrando o dado da posição 3: {lista_de_dados[3]}')
print(f'\nMostrando o dado da posição 7: {lista_de_dados[7]}')

print('esperando...')
time.sleep(5)
os.system('cls')

for item in lista_de_dados:
    print(item)
