"""
Disciplina: Cálculo Numérico
Autor: Zaion Luz

Método: Cholesky

A = LLᵀ
"""

import numpy as np

# Matriz exemplo
A = np.array([
    [4, 2, 2],
    [2, 10, 4],
    [2, 4, 9]
], dtype=float)

# Executa decomposição
L = np.linalg.cholesky(A)

print("Matriz L:")
print(L)