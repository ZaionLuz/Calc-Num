"""
Disciplina: Cálculo Numérico
Autor: Zaion Luz

Método: PA = LU

A matriz é fornecida pelo usuário.
"""

import numpy as np

# Solicita ordem da matriz
n = int(input("Ordem da matriz: "))

# Cria matriz vazia
A = np.zeros((n, n))

# Entrada dos elementos
print("Digite os elementos da matriz:")

for i in range(n):
    for j in range(n):

        # Lê elemento da matriz
        A[i][j] = float(
            input(f"A[{i+1}][{j+1}] = ")
        )

# Cria matriz identidade para P
P = np.eye(n)

# Cria matriz identidade para L
L = np.eye(n)

# Processo de pivotamento parcial
for k in range(n - 1):

    # Localiza o maior pivô da coluna
    p = np.argmax(np.abs(A[k:, k])) + k

    # Troca linhas se necessário
    if p != k:

        A[[k, p]] = A[[p, k]]

        P[[k, p]] = P[[p, k]]

        if k > 0:
            L[[k, p], :k] = L[[p, k], :k]

    # Eliminação
    for i in range(k + 1, n):

        m = A[i, k] / A[k, k]

        L[i, k] = m

        A[i] = A[i] - m * A[k]

# Matriz triangular superior
U = A

print("\nMatriz P:")
print(P)

print("\nMatriz L:")
print(L)

print("\nMatriz U:")
print(U)