# inicio fim passo

# Ordem crescente de 5 em 5
for c in range(0, 101, +5):
    print(c)

# Ordem decrescente de 20 em 20
for c in range(101, 1, -20):
    print(c)

# Ordem decrescente com input diminuindo 1 em 1
numero = int(input('Digite um número >> '))
for c in range(numero, 0, -1):
    print(c)