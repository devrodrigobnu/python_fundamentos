# 3 - Classe Carro:
# Crie uma classe chamada Carro que simule um carro. 
# A classe deve ter os atributos marca, modelo e ano.
# Crie métodos para ligar (ligar()), desligar (desligar()) e 
# exibir as informações do carro (exibir_informacoes()).
import os

class CarroRodrigo:
    mensagem_input = '\n1 - Ligar'
    mensagem_input += '\n2 - Desligar'
    mensagem_input += '\n3 - Exibir Informações'
    mensagem_input += '\n4 - Sair'    
    mensagem_input += '\nInforme a operação: '
    
    marca = 'Citroen'
    modelo = 'C3'
    ano = 2014
    ligado = False


    def ligar():
        if not CarroRodrigo.ligado:
            CarroRodrigo.ligado = True
            print('VRUUUUUMMMMM, veículo ligado com sucesso!')
        else:
            print('Veiculo encontra-se desligado!')
    
    def desligar():
        if CarroRodrigo.ligado:
            CarroRodrigo.ligado = False
            print('Veículo desligado com sucesso!')
        else:
            print('Veículo encontra-se ligado!')
    
    def exibir_informações():
        print(f'\nInformações do carro:')
        print(f'Marca: {CarroRodrigo.marca}')
        print(f'Modelo: {CarroRodrigo.modelo}')
        print(f'Ano: {CarroRodrigo.ano}')

    def script():
        while True:
            try:
                opcao = input(CarroRodrigo.mensagem_input)
                if opcao == '1':
                    CarroRodrigo.ligar()
                elif opcao == '2':
                    CarroRodrigo.desligar()
                elif opcao == '3':
                    CarroRodrigo.exibir_informações()
                elif opcao == '4':
                    break
            except:
                print('\nInforme uma opção válida')
                
if __name__ == '__main__':
    os.system('cls')
    CarroRodrigo.script()

