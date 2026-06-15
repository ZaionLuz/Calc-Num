"""
Disciplina: Cálculo Numérico
Autor: Zaion Luz

Método: Fatoração LU

Decompõe uma matriz A em:

A = LU
"""

import numpy as np

# Matriz de exemplo
A = np.array([
    [2, 3, 1],
    [4, 7, 7],
    [-2, 4, 5]
], dtype=float)

# Obtém a ordem da matriz
n = len(A)

# Cria matriz identidade para L
L = np.eye(n)

# Copia A para U
U = A.copy()

# Processo de eliminação
for k in range(n - 1):

    # Percorre as linhas abaixo do pivô
    for i in range(k + 1, n):

        # Calcula multiplicador
        m = U[i, k] / U[k, k]

        # Armazena em L
        L[i, k] = m

        # Atualiza linha de U
        U[i] = U[i] - m * U[k]

# Exibe resultados
print("Matriz L:")
print(L)

print("\nMatriz U:")
print(U)