import sqlite3

print('Testando entrada no arquivo')

try:
    conn = sqlite3.connect('banco_de_dados.sqlite3')
    print('Você acessou seu banco.')
except Exception:
    print('Você não está conseguindo criar o arquivo banco')

if conn is not None:
    print('Você estabilizou sua conexão')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE pessoa (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(15) NOT NULL, 
        idade INTEGER NOT NULL, 
        altura VARCHAR(20)
    )
''')
    print('Sua tabela de pessoas foi cadastrada')

    cursor.execute('''
    CREATE TABLE usuarios (
        nome VARCHAR(15) NOT NULL,
        nickname VARCHAR(30) PRIMARY KEY NOT NULL,
        senha VARCHAR(30) NOT NULL
    )
''')