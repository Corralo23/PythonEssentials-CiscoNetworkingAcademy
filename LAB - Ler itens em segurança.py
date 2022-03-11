# Sua tarefa é escreveruma FUNÇÃO CAPAZ DE FAZER INPUT DE VALORES INTEIROS E DE VERIFICAR SE ELES ESTÃO
# DENTRODE UM INTERVALO ESPECIFICADO:
# A) aceitar três argumentos: um prompt, um limite inferior aceitável e um limite superior aceitável;
# b) se o utilizador inserir uma string que não é um valor inteiro, a função deve emitir a mensagem Error:
# wrong input, e pedir ao utilizador para inserir o valor novamente;
# c) se o utilizador introduzir um número que fica fora do intervalo especificado, a função deve emitir a mensagem Error:
# the value is not within permitted range (min..max) e pedir ao utilizador para inserir o valor novamente;
# d) se o valor de input for válido, devolve-o como um resultado.

def read_int(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
        except ValueError:
            print('Error: wrong input')
        if ok:
            ok = value >= min and value <= max
        if not ok:
            print('Error: the value is not within permitted range (' + str(min) + '..' + str(max) + ')')
    return value;

v = read_int('Enter a number from - 10 to 10: ', -10, 10)

print(f'The number is: {v}')