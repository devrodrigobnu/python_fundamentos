# 12 - Classe Triângulo com Getters e Setters:
# Expanda o exercício da classe Triangulo.
# Torne os atributos lado1, lado2 e lado3 private. 
# Crie métodos get_lado1(), get_lado2() e get_lado3()
# para acessar os lados e métodos set_lado1(novo_lado), 
# set_lado2(novo_lado) e set_lado3(novo_lado) para modificar os lados. 
# No método eh_valido(),
# verifique se os lados formam um triângulo válido.

# Classe
class Triangulo:
    # Construtor
    def __init__(self, lado_1, lado_2, lado_3):
        self.__lado_1 = lado_1
        self.__lado_2 = lado_2
        self.__lado_3 = lado_3
    # Método
    def eh_valido(self):
        lado_1_valido = self.__lado_3 + self.__lado_2 > self.__lado_1
        lado_2_valido = self.__lado_1 + self.__lado_3 > self.__lado_2
        lado_3_valido = self.__lado_1 + self.__lado_2 > self.__lado_3

        return lado_1_valido is True and lado_2_valido is True and lado_3_valido is True
    #Getters
    def get_lado_1(self):
        return self.__lado_1
    def get_lado_2(self):
        return self.__lado_2
    def get_lado_3(self):
        return self.__lado_3
    #Setters
    def set_lado_1(self, novo_lado_1):
        print(f'Setou lado_1 {self.__lado_1} para {novo_lado_1}')
        self.__lado_1 = novo_lado_1
    def set_lado_2(self, novo_lado_2):
        print(f'Setou lado_2 {self.__lado_2} para {novo_lado_2}')
        self.__lado_2 = novo_lado_2
    def set_lado_3(self, novo_lado_3):
        print(f'Setou lado_3 {self.__lado_3} para {novo_lado_3}')

if __name__ == '__main__':
    # Instãncias 
    triangulo_1 = Triangulo(lado_1=3.1, lado_2=3.7, lado_3=5.2)
    triangulo_2 = Triangulo(lado_1=3, lado_2=3, lado_3=3)
    triangulo_3 = Triangulo(lado_1=3, lado_2=3, lado_3=5)
    print(f'Triângulo 1 é válido: {triangulo_1.eh_valido()}')
    print(f'Triângulo 2 é válido: {triangulo_2.eh_valido()}')
    print(f'Triângulo 3 é válido: {triangulo_3.eh_valido()}')

    # Utilizando Setters
    triangulo_1.set_lado_1(6)
    triangulo_1.set_lado_2(6)
    triangulo_1.set_lado_3(6)

    print(f'Triângulo 1 é válido: {triangulo_1.eh_valido()}')



