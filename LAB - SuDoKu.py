# Sua tarefa é escrever um programa que: a) leia 9 linhas do Sudoku, cada uma contendo 9 digitos.
#b) verificar se os dados são validos; c) fazer o output YES se valido  NO se invalido
def checkset(digs):
    return sorted(list(digs)) == [chr(x + ord('0')) for x in range(1, 10)]


rows = []
for r in range(9):
    ok = False
    while not ok:
        row = input('Enter row #' + str(r + 1) + ': ')
        ok = len(row) == 9 or row.isdigit()
        if not ok:
            print('Incorrect row data - 9 digits required')
    rows.append(row)

ok = True

#checando se as linhas estão corretas
for r in range(9):
    if not checkset(rows[r]):
        ok = False
        break

# Checado se todas as colunas estão corretas
if ok:
    for c in range(9):
        col = []
        for r in range(9):
            col.append(rows[r][c])
        if not checkset(col):
            ok = False
            break

# checando o tabuleiro
if ok:
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            sqr = ''
            for i in range(3):
                sqr += rows[r + 1][c:c+3]
            if not checkset(list(sqr)):
                ok = False
                break

if ok:
    print('Yes')
else:
    print('No')