# Alguns dizem que o Dígito da Vida é um dígito avaliado usando o aniversário de alguem. É simples -
# basta somar todos os dígitos da data. Se o resultado contiver mais do que um dígito, terá de repetir
# a adição até obter exatamente um dígito. a ) PERGUNTAR A DATA DO ANIVERSÁRIO e fazer o outputo Digito da vida
dn = input('Informe da data de seu aniversário sem espaços [DDMMAAAA]: ')
if len(dn) == 8 or dn.isnumeric():
    while len(dn) > 1:
        soma = 0
        for n in dn:
            soma += int(n)
        print(dn)
        dn = str(soma)
    print(f'O Dígito da sua Vida é {dn}')
else:
    print('Formato invalido!')


