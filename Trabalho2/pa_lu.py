"""
Disciplina: Cálculo Numérico
Autor: Zaion Luz

Método: PA = LU

Realiza a decomposição LU com
pivotamento parcial.

PA = LU
"""

import numpy as np

# Matriz de exemplo
A = np.array([
    [0, 2, 1],
    [1, -2, -3],
    [4, 1, 8]
], dtype=float)

# Obtém a ordem da matriz
n = len(A)

# Cria matriz identidade para P
P = np.eye(n)

# Cria matriz identidade para L
L = np.eye(n)

# Processo de pivotamento parcial
for k in range(n - 1):

    # Procura o maior elemento da coluna
    p = np.argmax(np.abs(A[k:, k])) + k

    # Se necessário, troca linhas
    if p != k:

        A[[k, p]] = A[[p, k]]

        P[[k, p]] = P[[p, k]]

        # Ajusta L caso já existam multiplicadores
        if k > 0:
            L[[k, p], :k] = L[[p, k], :k]

    # Eliminação
    for i in range(k + 1, n):

        # Calcula multiplicador
        m = A[i, k] / A[k, k]

        # Armazena em L
        L[i, k] = m

        # Atualiza linha
        A[i] = A[i] - m * A[k]

# A matriz resultante é U
U = A

print("Matriz P:")
print(P)

print("\nMatriz L:")
print(L)

print("\nMatriz U:")
print(U)