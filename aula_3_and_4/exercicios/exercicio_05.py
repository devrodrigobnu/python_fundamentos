# 5 - Classe Triângulo:
# Crie uma classe chamada Triangulo que represente um triângulo. 
# A classe deve ter os atributos lado1, lado2 e lado3.
# Crie métodos para verificar se os lados formam 
# um triângulo válido (eh_valido()), calcular o perímetro (calcular_perimetro())
# e exibir o tipo do triângulo com base nos lados (tipo_triangulo()).


import os

class Triangulo:
    lado_1 = float(input('Digite o comprimento do lado_1: '))
    lado_2 = float(input('Digite o comprimento do lado_2: '))
    lado_3 = float(input('Digite o comprimento do lado_3: '))


    def eh_valido():
        if Triangulo.lado_1 + Triangulo.lado_2 > Triangulo.lado_3 and \
        Triangulo.lado_1 + Triangulo.lado_3 > Triangulo.lado_2 and \
        Triangulo.lado_2 + Triangulo.lado_3 > Triangulo.lado_1:
            return True
        else:
            return False

    def calcular_perimetro():
        if Triangulo.eh_valido():
            return Triangulo.lado_1 + Triangulo.lado_2 + Triangulo.lado_3
        else:
            return "Triângulo inválido"

    def exibir_tipo_triangulo():
        if Triangulo.eh_valido():
            if Triangulo.lado_1 == Triangulo.lado_2 == Triangulo.lado_3:
                return 'Triângulo Equilátero'
            elif Triangulo.lado_1 == Triangulo.lado_2 or \
            Triangulo.lado_1 == Triangulo.lado_3 or \
            Triangulo.lado_2 == Triangulo.lado_3:
                return 'Triângulo Isóceles'
            else:
                return 'Triângulo Escaleno'
        else:
            return 'Triângulo inválido'

if __name__ == '__main__':
    os.system('cls')
    print(f'Perímetro: {Triangulo.calcular_perimetro()}')
    print(f'Tipo de triângulo: {Triangulo.exibir_tipo_triangulo()}')
    