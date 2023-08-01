import os

def captura_dados():
    
    # Lendo dados do usuário
    texto_usuario = input('Informe um texto: ')
    print('Você escreveu:', texto_usuario)

    # Usando type para mostrar tipos de dados
    print(type(texto_usuario))

    # Convertendo strings para números inteiros
    inteiro_usuario = input('Informe um número: ')
    
    
    # try -> para tentar executar o código
    # e continuar caso haja erro
    try:
        inteiro_usuario = int(inteiro_usuario)
    except: 
        print('Erro ao tentar converter inteiro')
    print('Você escreveu:', inteiro_usuario)  
    print(type(inteiro_usuario))

    # Convertendo strings para números quebrados
    float_usuario = input('Informe um número float: ')
    try:
        float_usuario = float(float_usuario)
    except: 
        print('Erro ao tentar converter float!')
    print('Você escreveu:', float_usuario)  
    print(type(float_usuario))

if __name__ == '__main__':
    os.system('cls')
    print('Executando 1ª vez')
    captura_dados()
    print('Executando 2ª vez')    
    captura_dados()
    print('Executando 3ª vez')
    captura_dados()