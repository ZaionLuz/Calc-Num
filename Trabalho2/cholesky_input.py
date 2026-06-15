"""
Disciplina: Cálculo Numérico
Autor: Zaion Luz

Método: Cholesky

A matriz é informada pelo usuário.
"""

import numpy as np

# Ordem da matriz
n = int(input("Ordem da matriz: "))

# Cria matriz vazia
A = np.zeros((n, n))

# Entrada dos dados
print("Digite os elementos:")

for i in range(n):
    for j in range(n):

        A[i][j] = float(
            input(f"A[{i+1}][{j+1}] = ")
        )

try:

    # Calcula Cholesky
    L = np.linalg.cholesky(A)

    print("\nL =")
    print(L)

except:

    print(
        "\nA matriz não admite Cholesky."
    )