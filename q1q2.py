#python3 q1q2.py
import random
def gerar_matriz_quadrada(dimensao, valor_minimo, valor_maximo):
    matriz = [[random.randint(valor_minimo, valor_maximo) for _ in range(dimensao)] for _ in range(dimensao)]
    return matriz

#FUNÇÃO SOLICITADA NA QUESTÃO 1
def inverter_diagonais(matriz):
    n = len(matriz)
    for i in range(n // 2):
        nor = i
        inv = n - 1 - i
        matriz[nor][nor], matriz[inv][inv] = matriz[inv][inv], matriz[nor][nor]
        matriz[nor][inv], matriz[inv][nor] = matriz[inv][nor], matriz[nor][inv]
    return matriz

#FUNÇÃO SOLICITADA NA QUESTÃO 2
def contar_submatrizes(matriz, submatriz):
    linhas_B, colunas_B = len(submatriz), len(submatriz[0])
    linhas_A, colunas_A = len(matriz), len(matriz[0])
    contador = 0
    for i in range(linhas_A - linhas_B + 1):
        for j in range(colunas_A - colunas_B + 1):
            achou_correspondencia = all(
                matriz[i + x][j:j + colunas_B] == submatriz[x]
                for x in range(linhas_B)
            )
            if achou_correspondencia:
                contador += 1
    return contador

def colorir_matriz(matriz, submatriz, cor='\033[91m'):
    linhas_B, colunas_B = len(submatriz), len(submatriz[0])
    linhas_A, colunas_A = len(matriz), len(matriz[0])
    matriz_colorida = [linha[:] for linha in matriz]
    for i in range(linhas_A - linhas_B + 1):
        for j in range(colunas_A - colunas_B + 1):
            achou_correspondencia = all(
                matriz[i + x][j:j + colunas_B] == submatriz[x]
                for x in range(linhas_B)
            )
            if achou_correspondencia:
                for x in range(linhas_B):
                    for y in range(colunas_B):
                        valor_original = matriz_colorida[i + x][j + y]
                        matriz_colorida[i + x][j + y] = f"{cor}{valor_original}\033[0m"
    return matriz_colorida

#  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  #  

print("\nEntrada Q1\n")
matriz_a = [ \
[7,8,9],
[4,5,6],
[1,2,3],
]
[print(linha) for linha in matriz_a]
matriz_invertida = inverter_diagonais(matriz_a)
print("\nSaida Q1\n")
[print(linha) for linha in matriz_invertida]

print("\nEntrada Q1\n")
matriz_temporaria = gerar_matriz_quadrada(9,1,9)
[print(linha) for linha in matriz_temporaria]
matriz_invertida = inverter_diagonais(matriz_temporaria)
print("\nSaida Q1\n")
[print(linha) for linha in matriz_invertida]


print("\nEntrada Q2\n")
matriz_temporaria = gerar_matriz_quadrada(12,1,2)
print("\nMatriz\n")
[print(linha) for linha in matriz_temporaria]
submatriz = [ \
[1,2],
[2,1],
]
print("\nSubmatriz\n")
[print(linha) for linha in submatriz]
contador = contar_submatrizes(matriz_temporaria,submatriz)
matriz_colorida = colorir_matriz(matriz_temporaria,submatriz)
print("\nSaida Q2\n")
print("\n{} submatrizes na matriz\n".format(contador))
print("\nIdentificacao visual\n")
for linha in matriz_colorida:
    print('[', end='')
    for elemento in linha:
        print(elemento, end=', ')
    print(']')






