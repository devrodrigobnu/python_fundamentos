# 16 - Classe Animal com Default Visibility:
# Crie uma classe chamada Animal. Defina um atributo especie com
#  visibilidade default. 
# Crie métodos get_especie() e set_especie(nova_especie)
# para manipular esse atributo.

class Animal:
    def __init__(self, especie):
        self.especie = especie
    print('O objeto foi instanciado com sucesso')


    def get_especie(self):
        return self.especie
    

    def set_especie(self, nova_especie):
        print(f'Adicionou a especie {nova_especie}, com sucesso!')
        self.especie = nova_especie



if __name__ == '__main__':
    especie_1 = Animal('Baleia Jubarte')
    especie_2 = Animal('Baleia Azul')
    especie_3 = Animal('Baleia Orcinus')
    especie_4 = Animal('Baleia Minke')

    especie_1.set_especie('Doberman')
    especie_2.set_especie('Collie')
    especie_3.set_especie('Pastor Alemão')
    especie_4.set_especie('Chihuahua')

    print(especie_1.get_especie())
    print(especie_2.get_especie())
    print(especie_3.get_especie())
    print(especie_4.get_especie())