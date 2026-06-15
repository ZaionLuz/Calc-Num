"""
Disciplina: Cálculo Numérico
Autor: Zaion Luz

Método: Gauss-Jacobi

Resolve sistemas lineares por
aproximações sucessivas.
"""

import numpy as np

# Matriz de coeficientes
A = np.array([
    [10, 2, 1],
    [1, 5, 1],
    [2, 3, 10]
], dtype=float)

# Vetor independente
b = np.array([
    7,
    -8,
    6
], dtype=float)

# Vetor inicial
x = np.zeros(len(A))

# Critério de parada
tolerancia = 1e-6

# Número máximo de iterações
max_iteracoes = 100

# Processo iterativo
for _ in range(max_iteracoes):

    x_novo = np.zeros(len(A))

    for i in range(len(A)):

        soma = 0

        for j in range(len(A)):

            if i != j:
                soma += A[i][j] * x[j]

        x_novo[i] = (
            b[i] - soma
        ) / A[i][i]

    erro = np.linalg.norm(x_novo - x)

    if erro < tolerancia:
        break

    x = x_novo

print("Solução aproximada:")
print(x)