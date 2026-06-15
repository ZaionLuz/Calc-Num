"""
Disciplina: Cálculo Numérico
Autor: Zaion Luz

Método: Fatoração LU

A matriz é informada pelo usuário.
"""

import numpy as np

# Solicita a ordem da matriz
n = int(input("Ordem da matriz: "))

# Cria matriz vazia
A = np.zeros((n, n))

# Entrada dos elementos
print("Digite os elementos:")

for i in range(n):
    for j in range(n):

        # Lê elemento da matriz
        A[i][j] = float(
            input(f"A[{i+1}][{j+1}] = ")
        )

# Cria L identidade
L = np.eye(n)

# Copia A para U
U = A.copy()

# Eliminação de Gauss
for k in range(n - 1):

    for i in range(k + 1, n):

        m = U[i][k] / U[k][k]

        L[i][k] = m

        U[i] = U[i] - m * U[k]

print("\nL =")
print(L)

print("\nU =")
print(U)