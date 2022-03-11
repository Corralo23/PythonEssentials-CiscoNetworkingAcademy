#Um anagrama é uma palavra formada pelo rearranjo das letras de uma palavra,
# usando todas as letras originais exatamente uma vez.
# Escrever um programa que: a) pede ao utilizados dois textos separado
# b) virifica se os textos introduzidos são anagramas e imprime o resultado
texto1 = str(input('Digite o primeiro texto: '))
texto2 = str(input('Digite o segundo texto: '))

t1 = ''.join(sorted(list(texto1.upper().replace(' ', ''))))
t2 = ''.join(sorted(list(texto2.upper().replace(' ', ''))))

if len(t1) > 0 and t1 == t2:
    print('É um ANAGRAMA!!!!')
else:
    print('Não é Anagrama')