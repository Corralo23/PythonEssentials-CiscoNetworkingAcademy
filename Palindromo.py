#LAB: Palíndromo
mesg = input('Digite a mensagem: ')
mesg = mesg.replace(' ', '')

if len(mesg)> 1 and mesg.upper() == mesg[:: - 1].upper():
    print('É um palíndromo')
else:
    print('Não é um palíndromo')