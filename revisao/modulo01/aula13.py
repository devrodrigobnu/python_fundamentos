from time import sleep

inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

for cronometro in range(inicio, fim, -passo):
    sleep(1)
    print(cronometro)