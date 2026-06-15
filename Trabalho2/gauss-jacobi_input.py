"""
Disciplina: Cálculo Numérico
Autor: Zaion Luz

Método: Gauss-Jacobi

Os coeficientes do sistema são
informados pelo usuário.
"""

import numpy as np

# Ordem do sistema
n = int(input("Ordem da matriz: "))

# Cria matriz de coeficientes
A = np.zeros((n, n))

# Entrada dos coeficientes
print("Digite os elementos da matriz:")

for i in range(n):
    for j in range(n):

        A[i][j] = float(
            input(f"A[{i+1}][{j+1}] = ")
        )

# Cria vetor b
b = np.zeros(n)

# Entrada do vetor independente
print("\nDigite o vetor b:")

for i in range(n):

    b[i] = float(
        input(f"b[{i+1}] = ")
    )

# Aproximação inicial
x = np.zeros(n)

# Critério de parada
tolerancia = 1e-6

# Número máximo de iterações
max_iteracoes = 100

# Método de Gauss-Jacobi
for _ in range(max_iteracoes):

    x_novo = np.zeros(n)

    for i in range(n):

        soma = 0

        for j in range(n):

            if i != j:
                soma += A[i][j] * x[j]

        x_novo[i] = (
            b[i] - soma
        ) / A[i][i]

    erro = np.linalg.norm(x_novo - x)

    if erro < tolerancia:
        break

    x = x_novo

print("\nSolução aproximada:")

for i in range(n):
    print(f"x{i+1} = {x[i]:.6f}")