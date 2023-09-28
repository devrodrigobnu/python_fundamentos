from pessoaFisica import PessoaFisica

pf = PessoaFisica(
    input('Digite o nome do titular: '),
    input('Digite o cpf do titular: '),
    float(input('Digite o saldo inicial: '))
)

print(pf)

var = input('Você deseja cadastrar segundo titular? \nSim \nNão \nOpção escolhida: ')

if var == 'sim':
    pf.Segundo_Titular = input('Digite o segundo titular: ')
    print(pf)