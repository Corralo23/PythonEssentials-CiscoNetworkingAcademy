# A sua tarefa é escrever um programa que responda a seguinte questão:
# os carateres que compõem a primeira string estão escondidos dentro da segunda string?
# Dica = utilizar dois argumentos da função POS()
palavra = str(input('Digite a palavra que deseja encontrar: ')).upper()
texto = str(input('Digite o texto em que deseja encontrar a palavra: ')).upper()

achou = True
inicio = 0

for p in palavra:
    pos = texto.find(p, inicio)
    if pos < 0:
        achou = False
        break
    inicio = pos + 1
if achou:
    print('Sim')
else:
    print('Não')