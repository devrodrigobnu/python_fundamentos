import os # Operation System - Permite usar comandos do terminal

def mostrar_dados():
    # Exibindo dados
    print('Número', 5)
    print(f'Número {5}')
    print('String', 'Hello')
    print('String ' + 'Hi')
    print('Float', 1.5)
    print(f'Float {55.47}')
    print('Boolean', False)
    print('Boolean', True)

if __name__ == '__main__': 
    os.system('cls')
    mostrar_dados()
    