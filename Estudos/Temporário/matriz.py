matriz = []

tamL = int(input(f'Linhas: '))
tamC = int(input(f'Colunas: '))
if (tamL < 2):
    print ('Deve haver no mínimo duas Linhas!')
elif (tamC < 2):
    print ('Deve haver no mínimo duas Colunas!')
else:
    for l in range (tamL):
        linha = []
        for c in range (tamC):
            num = int(input(f'Valor para [{l}, {c}]: '))
            linha.append(num)
        matriz.append(linha)

    for x in range (tamC):
        print (f'{matriz[x]}')

    for l in range (tamL):
        somalinha = 0
        for c in range (tamC):
            somalinha += matriz[l][c]
        print (f'Soma da linha [{l}]: {somalinha}')

    for c in range (tamC):
        somacoluna = 0
        for l in range (tamL):
            somacoluna += matriz[l][c]
        print(f'Soma da coluna [{c}]: {somacoluna}')

    diagonal = 0
    for l in range(tamL):
        for c in range(tamC):
            if ( l == c ):
                diagonal += matriz[l][c]

    diagonals = 0
    for l in range(tamL):
        diagonals += matriz[l][tamC - 1 - l]

    print (f'Diagonal secundária: {diagonals}')

    print (f'Soma da diagonal: {diagonal}')